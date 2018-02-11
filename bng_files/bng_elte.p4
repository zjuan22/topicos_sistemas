#include <core.p4>
#include <v1model.p4>
#include "include/standard_headers.p4"

/***********************  C O N S T A N T S  *****************************/
const bit<16> ETHERTYPE_IPV4 = 0x0800;
const bit<16> ETHERTYPE_ARP  = 0x0806;
const bit<8>  IPPROTO_ICMP   = 0x01;

/***********************  H E A D E R S  *********************************/

const bit<16> ARP_HTYPE_ETHERNET = 0x0001;
const bit<16> ARP_PTYPE_IPV4     = 0x0800;
const bit<8>  ARP_HLEN_ETHERNET  = 6;
const bit<8>  ARP_PLEN_IPV4      = 4;


struct headers {
    ethernet_t   ethernet;
    ethernet_t   ethernet_decap;
    arp_t        arp;
    ipv4_t       ipv4;
    gre_t        gre;
    tcp_t        tcp;
    icmp_t       icmp;
    @name("inner_ipv4") 
    ipv4_t       inner_ipv4;
    @name("inner_ethernet") 
    ethernet_t   inner_ethernet;
    @name("inner_tcp") 
    tcp_t        inner_tcp;
    @name("inner_icmp") 
    icmp_t       inner_icmp;
}

/***********************  M E T A D A T A  *******************************/
struct routing_metadata_t {
    bit<32> nhgroup;

    bit<32> dst_ipv4;
    bit<32> src_ipv4;
    bit<48>  mac_da;
    bit<48>  mac_sa;
    bit<9>   egress_port;
    bit<48>  my_mac;

    bit<32> nhop_ipv4;
    bit<1>  do_forward;
    bit<16> tcp_sp;
    bit<16> tcp_dp;

    bit<8>  if_index;    
    bit<32> if_ipv4_addr;
    bit<48> if_mac_addr;
    bit<1>  is_ext_if;
    
    bit<32> tunnel_id;
    bit<5>  ingress_tunnel_type;
    bit<1>  tcp_inner_en;
    bit<16> lkp_inner_l4_sport;
    bit<16> lkp_inner_l4_dport;

    bit<32>  dst_inner_ipv4;
    bit<32>  src_inner_ipv4;

    bit<32> meter_tag;

}

struct metadata {
    @name(".routing_metadata") 
    routing_metadata_t routing_metadata;
}



/***********************  P A R S E R  ***********************************/
parser ParserImpl(packet_in packet, out headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    @name(".start") state start {
        transition parse_ethernet;
    }
    @name ("parse_ethernet") state parse_ethernet {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            ETHERTYPE_IPV4 : parse_ipv4;
            ETHERTYPE_ARP  : parse_arp;
            default        : accept;
        }
    }
    @name ("parse_arp") state parse_arp {
        packet.extract(hdr.arp);
        transition accept;
    }

    @name("parse_ipv4") state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            IPPROTO_ICMP : parse_icmp;
            8w0x6 :         parse_tcp;
            8w47 :         parse_gre;
            default      : accept;
        }
    }
    @name("parse_icmp") state parse_icmp {
        packet.extract(hdr.icmp);
        transition accept;
    }    
    @name("parse_tcp") state parse_tcp {
        packet.extract<tcp_t>(hdr.tcp);
        transition accept;
    }
    @name("parse_gre") state parse_gre {
        packet.extract<gre_t>(hdr.gre);
        transition select(hdr.gre.C, hdr.gre.R, hdr.gre.K, hdr.gre.S, hdr.gre.s, hdr.gre.recurse, hdr.gre.flags, hdr.gre.ver, hdr.gre.proto) {
            (1w0x0, 1w0x0, 1w0x0, 1w0x0, 1w0x0, 3w0x0, 5w0x0, 3w0x0, 16w0x800): parse_gre_ipv4;
            default: accept;
        }
    }
    @name(".parse_gre_ipv4") state parse_gre_ipv4 {
        transition parse_inner_ipv4;
    }

    @name(".parse_inner_ipv4") state parse_inner_ipv4 {
        packet.extract(hdr.inner_ipv4);
        transition select(hdr.inner_ipv4.fragOffset, hdr.inner_ipv4.ihl, hdr.inner_ipv4.protocol) {
            (13w0x0, 4w0x5, 8w0x1): parse_inner_icmp;
            (13w0x0, 4w0x5, 8w0x6): parse_inner_tcp;
            /*(13w0x0, 4w0x5, 8w0x11): parse_inner_udp;*/
            default: accept;
        }
    }
    @name(".parse_inner_icmp") state parse_inner_icmp {
        packet.extract(hdr.inner_icmp);
        transition accept;
    }

    @name(".parse_inner_tcp") state parse_inner_tcp {
        packet.extract(hdr.inner_tcp);
        transition accept;
    }

    @name(".parse_inner_ethernet") state parse_inner_ethernet {
        packet.extract(hdr.inner_ethernet);
        transition select(hdr.inner_ethernet.etherType) {
            16w0x800: parse_inner_ipv4;
            default: accept;
        }
    }
}
@name("mac_learn_digest") struct mac_learn_digest {
    bit<8> in_port;    /* 9 bits?, it doesnt compile with other value like 16, why? */
    bit<48> mac_sa;
}


/**************  I N G R E S S   P R O C E S S I N G   ******************/
control ingress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    
    /***************************** set metadata  **************************/
    action set_meta_info() {
        
        /*meta.routing_metadata.if_index = (bit<8>)standard_metadata.ingress_port;*/

        /*inner metadata */
        meta.routing_metadata.dst_inner_ipv4= hdr.inner_ipv4.dstAddr; 
        meta.routing_metadata.src_inner_ipv4= hdr.inner_ipv4.srcAddr;

        meta.routing_metadata.mac_da = hdr.ethernet.dstAddr;
        meta.routing_metadata.mac_sa = hdr.ethernet.srcAddr;

        meta.routing_metadata.lkp_inner_l4_sport = hdr.inner_tcp.srcPort;
        meta.routing_metadata.lkp_inner_l4_dport = hdr.inner_tcp.dstPort;
        
        /*meta.routing_metadata.tcp_sp = hdr.tcp.srcPort;
        meta.routing_metadata.tcp_dp = hdr.tcp.dstPort;*/
    }
    @name(".meta_info") table meta_info {
       /* key = { meta.routing_metadata.if_index: exact;} */
        key = { hdr.ethernet.srcAddr: exact; }
        actions = {set_meta_info; }
    default_action = set_meta_info();     
    }

    /***************************** Drop  **************************/
     @name(".drop")action drop() {
        /*mark_to_drop();*/

    }
    /***************************** set IF info and others  **************************/
    /*action set_if_info(bit<32> ipv4_addr, bit<48> mac_addr, bit<1> is_ext) { */
    action set_if_info() {
        
        
        meta.routing_metadata.if_ipv4_addr = 0x7fef4800 ;
        meta.routing_metadata.if_mac_addr = 0x010101010100;
        meta.routing_metadata.is_ext_if = 0x1;
        standard_metadata.egress_port = 1;

    }
    @name(".if_info") table if_info {
        key = { meta.routing_metadata.if_index: exact;}
        actions = {   drop;  set_if_info; }
    default_action = set_if_info();     
   
    }
    /***************************** process mac learn  *****************************/
   
    @name(".generate_learn_notify") action generate_learn_notify() {
        digest<mac_learn_digest>(32w1024, {meta.routing_metadata.if_index, hdr.ethernet.srcAddr });
    }
    @name(".smac") table smac {
        actions = {
            generate_learn_notify;
        }
        key = {
            /*standard_metadata.ingress_port: exact;*/
            hdr.ethernet.srcAddr: exact;
            /*hdr.ethernet.isValid()                : exact;*/
        }
        size = 512;
    }
    
    /***************************** tunnel control decap *****************************/
    @name("decap_gre_inner_ipv4") action decap_gre_inner_ipv4(bit <32> tunnel_id) {
           /*hdr.ipv4= hdr.inner_ipv4;  */
           /*hdr.ipv4.dstAddr =  meta.routing_metadata.dst_inner_ipv4;
           hdr.ipv4.srcAddr =  meta.routing_metadata.src_inner_ipv4;

           hdr.inner_ipv4.setInvalid();
           hdr.ethernet.etherType = 16w0x800;
           hdr.gre.setInvalid();
               hdr.ipv4.protocol = 8w0x6;
               hdr.tcp.setValid();

               hdr.tcp.srcPort = meta.routing_metadata.lkp_inner_l4_sport;  
               hdr.tcp.dstPort = meta.routing_metadata.lkp_inner_l4_dport;   
               hdr.tcp.dstPort = hdr.inner_tcp.dstPort;  doestn compile 
               
           meta.routing_metadata.dst_ipv4 = hdr.ipv4.dstAddr; */
           /* new decap */  
           meta.routing_metadata.tunnel_id = tunnel_id;         
           meta.routing_metadata.dst_ipv4 = meta.routing_metadata.dst_inner_ipv4;

           hdr.ethernet.setInvalid();
           hdr.ipv4.setInvalid();
           hdr.gre.setInvalid();
           hdr.ethernet_decap.setValid();
           hdr.ethernet_decap.dstAddr =  meta.routing_metadata.mac_da; 
           hdr.ethernet_decap.srcAddr =  meta.routing_metadata.mac_sa;
           hdr.ethernet_decap.etherType = 16w0x800;
           
    }
    
    @name("tunnel_decap_process_outer") table decap_process_outer {
        actions = {decap_gre_inner_ipv4; drop; }
        key ={ hdr.ethernet.srcAddr: exact;}
        
        size = 1024;
        default_action = drop();
    } 
    /***************************** firewall UL control *****************************/
    @name(".fw_drop_up") table fw_drop_up {
        actions = { drop; }
        key = {
            hdr.ipv4.dstAddr   : exact;
            hdr.tcp.dstPort    : exact;
        }
        size = 128;
    }
    
    /***************************** Nat control *****************************************/
    @name(".nat_miss_ext_to_int") action nat_miss_ext_to_int() {
        meta.routing_metadata.do_forward = 1w0;
        mark_to_drop();
    }
    @name(".nat_hit_int_to_ext") action nat_hit_int_to_ext(bit<32> srcAddr, bit<16> srcPort) {
        meta.routing_metadata.do_forward = 1w1;
        /*meta.src_ipv4 = srcAddr; */
        hdr.inner_ipv4.srcAddr= srcAddr;
        /*meta.tcp_sp = srcPort;*/
        /*meta.routing_metadata.dst_ipv4 = hdr.inner_ipv4.dstAddr;  ver esta assig en control decap */
        hdr.inner_tcp.srcPort = srcPort;
    }
    @name(".nat_hit_ext_to_int") action nat_hit_ext_to_int(bit<32> dstAddr, bit<16> dstPort) {
        meta.routing_metadata.do_forward = 1w1;
        meta.routing_metadata.dst_ipv4 = dstAddr; /* to lpm */
        hdr.ipv4.dstAddr = dstAddr;
        /*meta.src_ipv4 = hdr.ipv4.srcAddr;*/
        hdr.tcp.dstPort = dstPort;
        /*meta.tcp_dp = dstPort; */

    }
    @name(".nat_to_nat") action nat_to_nat() {
       /* meta.routing_metadata.do_forward = 1w1; */
    }

    @name(".nat_up") table nat_up {
        actions = {
            nat_to_nat;
            nat_hit_int_to_ext;
        }

        key = { meta.routing_metadata.is_ext_if: exact;}
        size = 1024;

        default_action = nat_to_nat();     
    }

    /*@name(".nat") table nat {
        actions = {
            drop;
            nat_miss_ext_to_int;
            nat_hit_int_to_ext;
            nat_hit_ext_to_int;
            nat_no_nat;
        }
        key = {
        
            meta.routing_metadata.is_ext_if: exact;
            hdr.ipv4.isValid() : exact;
            hdr.tcp.isValid()  : exact;    this two doesnt compile
            hdr.ipv4.srcAddr   : ternary;
            hdr.ipv4.dstAddr   : ternary;
            hdr.tcp.srcPort    : ternary;
            hdr.tcp.dstPort    : ternary;
        }
        size = 128;
        default_action = nat_no_nat();
    }*/
    
    /***************************** tunnel control encap *****************************/
    

    @name(".ipv4_gre_rewrite") action ipv4_gre_rewrite(bit<32> gre_srcAddr, bit<32> gre_dstAddr) {
           
      hdr.ethernet.etherType = 16w0x800;
      /*hdr.gre.proto = hdr.ethernet.etherType; */
      /*f_insert_inner_ipv4_header(8w02);*/
            
      hdr.inner_tcp.setValid(); 
      /*hdr.inner_tcp = hdr.tcp; it doesnt compile */

      hdr.inner_tcp.srcPort = meta.routing_metadata.tcp_sp;
      hdr.inner_tcp.dstPort = meta.routing_metadata.tcp_dp;

      hdr.tcp.setInvalid(); 

      /*meta.dst_ipv4 = hdr.ipv4.dstAddr; 
      meta.src_ipv4 = hdr.ipv4.srcAddr;  this doesnt compile with macsad */

      hdr.inner_ipv4.setValid();

      /*hdr.inner_ipv4 = hdr.ipv4;  it doestn compile*/

      hdr.inner_ipv4.dstAddr = meta.routing_metadata.dst_ipv4;
      hdr.inner_ipv4.srcAddr = meta.routing_metadata.src_ipv4;

      hdr.ipv4.setInvalid();
      
      hdr.ipv4.setValid();
      hdr.ipv4.protocol = 8w47;
      hdr.ipv4.ttl = 8w64;
      hdr.ipv4.version = 4w0x4;
      hdr.ipv4.ihl = 4w0x5;
      hdr.ipv4.identification = 16w0;
      hdr.ipv4.srcAddr = gre_srcAddr;
      hdr.ipv4.dstAddr = gre_dstAddr;

      hdr.gre.setValid();
      hdr.gre.proto = 16w0x800;
      

    }

      @name(".tunnel_encap_process_outer") table tunnel_encap_process_outer {
        actions = {ipv4_gre_rewrite; }
        key = {  hdr.ipv4.dstAddr       : exact; }
        size = 1024;
    }
    /***************************** firewall DW control *****************************/
    @name(".fw_drop_dw") table fw_drop_dw {
        actions = {
            drop;
        }
        key = {
            hdr.inner_ipv4.dstAddr   : exact;
            hdr.inner_tcp.dstPort    : exact;
        }
        size = 128;
    }
    
    /************** forwarding ipv4 ******************/
      
    @name(".rewrite_src_mac") action rewrite_src_mac(bit<48> smac) {
        hdr.ethernet.srcAddr = smac;
        hdr.ethernet_decap.srcAddr = smac;
    } 
          
    @name(".set_nhop") action set_nhop(bit<32> nhop_ipv4, bit<9> port) {
        
        standard_metadata.egress_spec = port;
        hdr.inner_ipv4.ttl = hdr.ipv4.ttl + 8w255;
    }
    
    @name(".ipv4_lpm") table ipv4_lpm {
        /*key     = {hdr.inner_ipv4.dstAddr  : lpm; } */
        key = {hdr.inner_ipv4.dstAddr: lpm;} 
        /*key     = { meta.routing_metadata.dst_ipv4 : lpm; }  */
        actions = { set_nhop; drop;  }
        size = 512; 
        default_action = drop();
    }

    @name(".sendout") table sendout {
        actions = {drop; rewrite_src_mac; }
        key = {  standard_metadata.egress_port: exact; }
        size = 512;
    }    
    
   




 
    /************** APPLY ******************/
    apply {
        meta_info.apply();
        if_info.apply();
        smac.apply();  
        /* ------ decap-------  */ 
        if(hdr.ipv4.protocol== 8w47){
           decap_process_outer.apply();
           nat_up.apply();  

           /*fw_drop_up.apply();*/
        }

        ipv4_lpm.apply(); 
        sendout.apply();
        /*ipv4_forward.apply();*/

        /*if(meta.routing_metadata.is_ext_if == 1){
           tunnel_encap_process_outer.apply();
           fw_drop_dw.apply();

        }
         
        if (meta.routing_metadata.do_forward == 1w1 && hdr.ipv4.ttl > 8w0) {
           meta.routing_metadata.my_mac = 0x000102030405; 
           ipv4_lpm.apply();
           ipv4_forward.apply();
        }*/ 

    }
    
    
}

control egress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    apply {
        }
}

control DeparserImpl(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.ipv4);
    }
}
/************   C H E C K S U M    V E  I F I C A T I O N   *************/
control verifyChecksum(inout headers hdr, inout metadata meta) {
    apply {
    }
}

control computeChecksum(inout headers hdr, inout metadata meta) {
    apply {
    }
}

V1Switch(ParserImpl(), verifyChecksum(), ingress(), egress(), computeChecksum(), DeparserImpl()) main;
