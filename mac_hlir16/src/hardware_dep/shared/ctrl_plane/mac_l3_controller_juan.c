#include "controller.h"
#include "messages.h"
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define MAX_MACS 1000000

controller c;

//void fill_ipv4_fib_lpm_table(uint8_t ip[4], uint8_t port, uint8_t mac[6])
//{
//	char buffer[2048]; /* TODO: ugly */
//	struct p4_header* h;
//	struct p4_add_table_entry* te;
//	struct p4_action* a;
//	struct p4_action_parameter* ap,* ap2;
//	struct p4_field_match_exact* exact; // TODO: replace to lpm
//
//  //  printf("LPM table update \n"); 
//
//	h = create_p4_header(buffer, 0, 2048);
//	te = create_p4_add_table_entry(buffer,0,2048);
//	strcpy(te->table_name, "ipv4_fib_lpm");
//
//	exact = add_p4_field_match_exact(te, 2048);
//	strcpy(exact->header.name, "ipv4.dstAddr");
//	memcpy(exact->bitmap, ip, 4);
//	exact->length = 4*8+0;
//
//	a = add_p4_action(h, 2048);
//	strcpy(a->description.name, "fib_hit_nexthop");
//
//	ap = add_p4_action_parameter(h, a, 2048);
//	strcpy(ap->name, "dmac");
//	memcpy(ap->bitmap, mac, 6);
//	ap->length = 6*8+0;
//
//	ap2 = add_p4_action_parameter(h, a, 2048);
//	strcpy(ap2->name, "port");
//	ap2->bitmap[0] = port;
//	ap2->bitmap[1] = 0;
//	ap2->length = 2*8+0;
//
//	netconv_p4_header(h);
//	netconv_p4_add_table_entry(te);
//	netconv_p4_field_match_exact(exact);
//	netconv_p4_action(a);
//	netconv_p4_action_parameter(ap);
//	netconv_p4_action_parameter(ap2);
//
//	send_p4_msg(c, buffer, 2048);
//}
//


uint8_t macs[MAX_MACS][6];
uint8_t portmap[MAX_MACS];
uint8_t ips[MAX_MACS][4];
int mac_count = -1;

int read_macs_and_ports_from_file(char *filename) {
	FILE *f;
	char line[200];
	int values[6];
	int values_ip[4];
	int port;
	int i;

	f = fopen(filename, "r");
	if (f == NULL) return -1;

	while (fgets(line, sizeof(line), f)) {
		line[strlen(line)-1] = '\0';
		//TODO why %c?
		if (11 == sscanf(line, "%d.%d.%d.%d %x:%x:%x:%x:%x:%x %d",
					&values_ip[0], &values_ip[1], &values_ip[2], &values_ip[3],
					&values[0], &values[1], &values[2],
					&values[3], &values[4], &values[5], &port) )
		{
			if (mac_count==MAX_MACS-1)
			{
				printf("Too many entries...\n");
				break;
			}

			++mac_count;
			for( i = 0; i < 6; ++i )
				macs[mac_count][i] = (uint8_t) values[i];
			for( i = 0; i < 4; ++i )
				ips[mac_count][i] = (uint8_t) values_ip[i];
			portmap[mac_count] = (uint8_t) port;

		} else {
			printf("Wrong format error in line %d : %s\n", mac_count+2, line);
			fclose(f);
			return -1;
		}

	}

	fclose(f);
	return 0;
}


void set_default_action_nat_up()
{
	char buffer[2048]; /* TODO: ugly */
	struct p4_header* h;
	struct p4_set_default_action* sda;
	struct p4_action* a;

	h = create_p4_header(buffer, 0, sizeof(buffer));

	sda = create_p4_set_default_action(buffer,0,sizeof(buffer));
        strcpy(sda->table_name, "nat_up");

	a = &(sda->action);
	strcpy(a->description.name, "nat_to_nat");

	netconv_p4_header(h);
	netconv_p4_set_default_action(sda);
	netconv_p4_action(a);

	send_p4_msg(c, buffer, sizeof(buffer));

	printf("########## \n");
	printf("\n");
	printf("Table name: %s\n", sda->table_name);
	printf("default action: %s\n", a->description.name);
}

void set_default_action_meta_info()
{
	char buffer[2048]; /* TODO: ugly */
	struct p4_header* h;
	struct p4_set_default_action* sda;
	struct p4_action* a;

	h = create_p4_header(buffer, 0, sizeof(buffer));

	sda = create_p4_set_default_action(buffer,0,sizeof(buffer));
        strcpy(sda->table_name, "meta_info");

	a = &(sda->action); 
	strcpy(a->description.name, "set_meta_info");

	netconv_p4_header(h);
	netconv_p4_set_default_action(sda);
	netconv_p4_action(a);

	send_p4_msg(c, buffer, sizeof(buffer));

	printf("########## \n");
	printf("\n");
	printf("Table name: %s\n", sda->table_name);
	printf("Default action: %s\n", a->description.name);
}

void set_default_action_decap_process()
{
	char buffer[2048]; /* TODO: ugly */
	struct p4_header* h;
	struct p4_set_default_action* sda;
	struct p4_action* a;

	h = create_p4_header(buffer, 0, sizeof(buffer));

	sda = create_p4_set_default_action(buffer,0,sizeof(buffer));
        strcpy(sda->table_name, "decap_process_outer");

	a = &(sda->action);
	strcpy(a->description.name, "decap_gre_inner_ipv4");

	netconv_p4_header(h);
	netconv_p4_set_default_action(sda);
	netconv_p4_action(a);

	send_p4_msg(c, buffer, sizeof(buffer));

	printf("##########\n");
	printf("\n");
	printf("Table name: %s\n", sda->table_name);
	printf("Default action: %s\n", a->description.name);
}


//void fill_meta_info(uint8_t port )
void fill_meta_info(uint8_t smac[6])
{
    char buffer[2048]; /* TODO: ugly */
    struct p4_header* h;
    struct p4_add_table_entry* te;

    struct p4_action* a;
    //struct p4_action_parameter* ap;

    struct p4_field_match_exact* exact;
    printf("meta_info table updatee \n");

    h = create_p4_header(buffer, 0, 2048);
    te = create_p4_add_table_entry(buffer,0,2048);
    strcpy(te->table_name, "meta_info");

    exact = add_p4_field_match_exact(te, 2048);
    strcpy(exact->header.name, "hdr.ethernet.srcAddr"); // key
    exact->bitmap[0] = smac;
	exact->bitmap[1] = 0;
    exact->length = 6*8+0;

   	a = add_p4_action(h, 2048);
	strcpy(a->description.name, "set_meta_info");
//
//	ap = add_p4_action_parameter(h, a, 2048);
//	strcpy(ap->name, "smac");
//	memcpy(ap->bitmap, smac, 6);
//	ap->length = 6*8+0;

    netconv_p4_header(h);
    netconv_p4_add_table_entry(te);
    netconv_p4_field_match_exact(exact);
    netconv_p4_action(a);
    //netconv_p4_action_parameter(ap);

    send_p4_msg(c, buffer, 2048);
}


void fill_if_info(uint8_t port )
{
    char buffer[2048]; /* TODO: ugly */
    struct p4_header* h;
    struct p4_add_table_entry* te;

    struct p4_action* a;
    //struct p4_action_parameter* ap;

    struct p4_field_match_exact* exact;
    printf("fill_info table update \n");

    h = create_p4_header(buffer, 0, 2048);
    te = create_p4_add_table_entry(buffer,0,2048);
    strcpy(te->table_name, "if_info");

    exact = add_p4_field_match_exact(te, 2048);
    strcpy(exact->header.name, "meta.routing_metadata.if_index"); // key
    exact->bitmap[0] = port;
	exact->bitmap[1] = 0;
    exact->length = 2*8+0;
    a = add_p4_action(h, 2048);
    strcpy(a->description.name, "set_if_info");

    netconv_p4_header(h);
    netconv_p4_add_table_entry(te);
    netconv_p4_field_match_exact(exact);
    netconv_p4_action(a);
    //netconv_p4_action_parameter(ap);

    send_p4_msg(c, buffer, 2048);

}


void fill_smac(uint8_t smac[6] )
{
    char buffer[2048]; /* TODO: ugly */
    struct p4_header* h;
    struct p4_add_table_entry* te;

    struct p4_action* a;
    struct p4_action_parameter* ap;

    struct p4_field_match_exact* exact;
    printf("fill_smac table update \n");

    h = create_p4_header(buffer, 0, 2048);
    te = create_p4_add_table_entry(buffer,0,2048);
    strcpy(te->table_name, "smac");



    exact = add_p4_field_match_exact(te, 2048);
    strcpy(exact->header.name, "hdr.ethernet.srcAddr"); // key
    exact->bitmap[0] = smac;
    exact->bitmap[1] = 0;
    exact->length = 2*8+0;
    
    a = add_p4_action(h, 2048);
    strcpy(a->description.name, "set_meta_info");
    
    ap = add_p4_action_parameter(h, a, 2048);
    strcpy(ap->name, "smac");
    memcpy(ap->bitmap, smac, 6);
    ap->length = 6*8+0;

    netconv_p4_header(h);
    netconv_p4_add_table_entry(te);
    netconv_p4_field_match_exact(exact);
    netconv_p4_action(a);
    netconv_p4_action_parameter(ap);
    send_p4_msg(c, buffer, 2048);

}

void fill_decap_process(uint8_t port )
{
    char buffer[2048]; /* TODO: ugly */
    struct p4_header* h;
    struct p4_add_table_entry* te;

    //struct p4_action* a;
    //struct p4_action_parameter* ap;

    struct p4_field_match_exact* exact;
    printf("fill decap process update \n");

    h = create_p4_header(buffer, 0, 2048);
    te = create_p4_add_table_entry(buffer,0,2048);
    strcpy(te->table_name, "decap_process_outer");

    exact = add_p4_field_match_exact(te, 2048);
    strcpy(exact->header.name, "meta.routing_metadata.if_index"); // key
    exact->bitmap[0] = port;
    exact->bitmap[1] = 0;
    exact->length = 2*8+0;

    netconv_p4_header(h);
    netconv_p4_add_table_entry(te);
    netconv_p4_field_match_exact(exact);
    //netconv_p4_action(a);
    //netconv_p4_action_parameter(ap);

    send_p4_msg(c, buffer, 2048);

}


void fill_nat_up(uint8_t port, uint8_t ip[4], uint8_t srctcp[2])
{
	char buffer[2048];
	struct p4_header* h;
        struct p4_add_table_entry* te;
	struct p4_action* a;
        struct p4_action_parameter* ap,* ap2;

        struct p4_field_match_exact* exact;

	h = create_p4_header(buffer, 0, 2048);
        te = create_p4_add_table_entry(buffer,0,2048);
        strcpy(te->table_name, "nat_up");
        
        printf("Filllll Table name: %s", te->table_name);

        exact = add_p4_field_match_exact(te, 2048);
	strcpy(exact->header.name, "meta.routing_metadata.is_ext_if");
        exact->bitmap[0] = port;
	exact->bitmap[1] = 0;
	exact->length = 1*8+0;
        printf("Table match: %s -> ", exact->bitmap);

        a = add_p4_action(h, 2048);
	strcpy(a->description.name, "nat_hit_int_to_ext");

        printf("action: %s -> ", a->description.name );

        ap = add_p4_action_parameter(h, a, 2048);
	strcpy(ap->name, "srcAddr");
        memcpy(ap->bitmap, ip, 4);
        ap->length = 4*8+0;
        
        printf("%s ->", ap->name);
	for(int i = 0; i < 4; i++){
                printf("%d.",ap->bitmap[i]);
        }	


	ap2 = add_p4_action_parameter(h, a, 2048);
	strcpy(ap2->name, "srcPort");
	memcpy(ap2->bitmap, srctcp, 2);
	ap2->length = 2*8+0;

        printf("%s ->", ap2->name);
	for(int i = 0; i < 4; i++){
                printf("%d.",ap2->bitmap[i]);
        }	
	printf("\n");



	netconv_p4_header(h);
        netconv_p4_add_table_entry(te);
	netconv_p4_field_match_exact(exact);
	netconv_p4_action(a);
	netconv_p4_action_parameter(ap);
	netconv_p4_action_parameter(ap2);



	send_p4_msg(c, buffer, 2048);

	printf("########## \n");
	printf("\n");
	printf("Table name: %s\n", te->table_name);
	printf("Action: %s\n", a->description.name);
}
 

// -----------------------------------------------------------------------

void dhf(void* b) {
	printf("Unknown digest received\n");
}

void init() {
         printf("Set default actions.\n");
 
        uint8_t mac[6] = {0xa0, 0x36, 0x9f, 0x3e, 0x94, 0xea};
	uint8_t port = 1;

	uint8_t ip2[4] = {192,168,0,1};
	uint8_t stcp[2] = {10};
        uint8_t mac2[6] = {0xa0, 0x36, 0x9f, 0x3e, 0x94, 0xe8};
	uint8_t port2 = 0;
        uint8_t smac[6] = {0xa0, 0x36, 0x9f, 0x3e, 0x94, 0xea};  //a0:36:9f:3e:94:ea

        set_default_action_meta_info(); 
        set_default_action_decap_process(); 
        set_default_action_nat_up();
        fill_meta_info(smac);
        //fill_meta_info(port);

        fill_if_info(port2);
        fill_if_info(port);

        fill_nat_up(port2,ip2,stcp);
        fill_nat_up(port,ip2,stcp);


         printf("\n");
 
 }




 int main(int argc, char* argv[])
 {
         if (argc>1) {
                 if (argc!=2) {
                         printf("Too many arguments...\nUsage: %s <filename(optional)>\n", argv[0]);
                         return -1;
                 }
                 printf("Command line argument is present...\nLoading configuration data...\n");
                 if (read_macs_and_ports_from_file(argv[1])<0) {
                         printf("File cannnot be opened...\n");
                         return -1;
                 }
         }
 
         printf("Create and configure controller...\n");
         c = create_controller_with_init(11111, 3, dhf, init);
 
         printf("MACSAD controller started...\n");
         execute_controller(c);
 
         printf("MACSAD controller terminated\n");
         destroy_controller(c);
 
         return 0;
 }




