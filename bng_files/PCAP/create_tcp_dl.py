#!/usr/bin/env python

import os
import string
import sys
import random
from random import shuffle
import argparse
from random import randint

from scapy.all import *

#Parse the number of entries
parser = argparse.ArgumentParser(description='IPv4 PCAP generator.')
parser.add_argument('num', metavar='n', type=int,
                   help='Number of entries')
args = parser.parse_args()


pkts = []
f = 0
entries = args.num
ipdst = []
ipsrc = []
macsrc = []
macdst = []
macsrc_h = []
macdst_h = []
#pktsize = [18, 82, 210, 466, 978, 1234, 1472] #Don't update the pktsizes original
#pktsize = [0 ,46, 174,430 ,942, 1198, 1436] #Don't update the pktsizes
pktsize = [6, 70, 198, 454, 966, 1222, 1460] #Don't update the pktsizes

#The next code generates random IPv6 and MAC address
#########
k = []
for i in range(16):
    k.append(i)
shuffle(k)
r = []
i = 0
for i in range(1,254):
    r.append(i)
shuffle(r)

ju = []
i = 0
for i in range(1,254):
    ju.append(i)
shuffle(ju)

u = []
i = 0
for i in range(65535):
    u.append(i)
shuffle(u)
v = []
i = 0
for i in range(65535):
    v.append(i)
shuffle(v)
l = 0
macsrc_c = ""
macdst_c = ""
macsrc_hex = ""
macdst_hex = ""
macsrc_hex2 = ""
macdst_hex2 = ""
ipsrc_c = ""
ipdst_c = ""
for m in range(entries):
	macsrc_c = "f0:76:1c:"
	macdst_c = "f0:76:1c:"
	macsrc_hex = "0xf0:0x76:0x1c:"
	macdst_hex = "0xf0:0x76:0x1c:"
	macsrc_hex2 = "f0:76:1c:"
	macdst_hex2 = "f0:76:1c:"
	l = 0
	n = 0
	for i in range(6):
		if l == 2:
			n = 0
			macsrc_c = macsrc_c + ":" + format(k[0], '01x')
			macdst_c = macdst_c + ":" + format(k[1], '01x')
			if n == 0:
				macsrc_hex = macsrc_hex + ":" + format(k[0], '#01x')
				macdst_hex = macdst_hex + ":" + format(k[1], '#01x')
				n = 1
			l = 0
		else:
			macsrc_c = macsrc_c + format(k[0], '01x')
			macdst_c = macdst_c + format(k[1], '01x')
			if n == 0:
				macsrc_hex = macsrc_hex + format(k[0], '#01x')
				macdst_hex = macdst_hex + format(k[1], '#01x')
				n = 1
			else:
				macsrc_hex = macsrc_hex + format(k[0], '01x')
				macdst_hex = macdst_hex + format(k[1], '01x')
		l = l + 1
		shuffle(k)
	macdst.append(macdst_c)
	macsrc.append(macsrc_c)
	macdst_h.append(macdst_hex)
	macsrc_h.append(macsrc_hex)
for m in range(entries):
	l = 0
	ipsrc_c = ""
	ipdst_c = ""
	for i in range(4):
		if l == 1:
			ipdst_c = ipdst_c + "." + str(r[0])
			ipsrc_c = ipsrc_c + "." + str(r[1])
			l = 0
		else:
			ipdst_c = ipdst_c + str(r[0])
			ipsrc_c = ipsrc_c + str(r[1])
		l = l + 1
		shuffle(r)
	ipdst.append(ipdst_c)
	ipsrc.append(ipsrc_c)

# print macsrc
# print macdst
# print macsrc_h
# print macdst_h
# print ipdst
# print ipsrc
#########
i = 0
print "entries : "+ str(entries)
for i in range(0, 7):
    p = 0
    ip_count = 0
    for p in range(0, entries):
        index2 = randint(1,entries)
        ip_block = range(1,50)
        
        #pkts.append(Ether(dst='aa:1b:eb:df:44:3d',src='00:44:00:00:00:00')/IP(dst='4.0.0.11',src='4.0.0.10')/GRE()/IP(dst='192.168.0.10',src='10.0.0.    10')/TCP(sport=20, dport=80)/Raw(RandString(size=pktsize[i])))
        #pkts.append(Ether(dst='aa:1b:eb:df:44:3d',src=macsrc[p])/IP(dst='4.0.0.1',src='4.0.0.10')/GRE()/IP(dst=ipdst[p],src=ipsrc[p])/TCP(sport=20, dport=80)/Raw(RandString(size=pktsize[i])))
        #pkts.append(Ether(dst='aa:1b:eb:df:44:3d',src=macsrc[p])/IP(dst='192.168.0.1',src='192.168.0.'+str(p+1))/TCP(sport=20, dport=str(p+100) )/Raw(RandString(size=pktsize[i])))
        pkts.append(Ether(dst='aa:1b:eb:df:44:3d',src=macsrc[p])/IP(dst='192.168.0.1',src='192.168.0.'+str(p+1))/TCP(sport=20, dport=(p+100) )/Raw(RandString(size=pktsize[i])))

        if f == 0:
           if ip_count < 50: ip_count += 1  	
           else: ip_count = 0 		     
           #FILE = "echo " + str(ipdst[p]) + " " + macdst_h[p] + " 1 >> PCAP/trace_trPR_ipv4_" + str(entries) + "_random.txt"  
           #FILE = "echo "+str(macsrc[p])+" 10.0.0."+str(p+1) +" 4.0.0."+str(p+102)+" "+str(p+100)+ " 10.0.0."+str(ip_block[ip_count]) + " 1 >> PCAP/trace_trPR_nat_dl_" + str(entries) + "_random2.txt"  
           FILE = "echo "+str(macsrc[p])+" 10.0.0."+str(p+1) +" 4.0.0."+str(p+102)+ " " +str(p+100)+ " 1 >> PCAP/trace_trPR_bng_dl_" + str(entries) + "_random2.txt"  
           os.system(FILE)

		  #FILE2 = "echo " + macsrc[p] + " 0 >> PCAP/trace_trPR_l2_" + str(entries) + "_random.txt"
		  #os.system(FILE2)
		  #FILE2 = "echo " + macdst[p] + " 1 >> PCAP/trace_trPR_l2_" + str(entries) + "_random.txt"
		  #os.system(FILE2)
	#pname = "./PCAP/nfpa.trPR_ipv4_%d_random.%dbytes.pcap" % (entries, pktsize[i]+42+4) #Update the name depending of the Use-Case, use the same format
	pname = "./PCAP/nfpa.trPR_bng_dl_%d_random.%dbytes.pcap" % (entries, pktsize[i]+54+4) #Update the name depending of the Use-Case, use the same format
    #pnamec = "PCAP/nfpa.trPR_gre_%d_random.%dbytes.pcap" % (entries, pktsize[i]+42+4)
    #pnamec = "PCAP/nfpa.trPR_tcp_%d_random.%dbytes.pcap" % (entries, pktsize[i]+78+4)  #14 (eth) + 20 (ip4) + 20 (tcp) = 54
    #copy = "scp " + pnamec + " macsad@10.1.1.29:/home/macsad/nfpa/PCAP"
    wrpcap(pname,pkts)
    #os.system(copy)
    del pkts[:] #Don't delete this line
    f = 1
#copy = "scp PCAP/trace_trPR_l2_" + str(entries) + "_random.txt" + " root@10.1.1.27:/root/Fabricio/mac_ipv6_gyn/traces/"
#os.system(copy)
#copy = "scp PCAP/trace_trPR_ipv4_" + str(entries) + "_random.txt" + " root@10.1.1.27:/root/Fabricio/mac_ipv6_gyn/traces/"
#os.system(copy)
