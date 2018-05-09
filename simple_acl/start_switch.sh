#!/bin/sh
#sudo simple_switch -i 1@veth1 -i 2@veth3 --pcap --thrift-port 9090 --nanolog ipc:///tmp/bm-0-log.ipc --device-id 0 arp.json --log-console

simple_switch -i 1@s1-eth1 -i 2@s1-eth2 -i 11@cpu-veth-1 --pcap --thrift-port 22222 --nanolog ipc:///tmp/bm-0-log.ipc --device-id 0 bng.jsonsudo simple_switch -i 1@s1-eth1 -i 2@s1-eth2 -i 11@cpu-veth-1 --pcap --thrift-port 22222 --nanolog ipc:///tmp/bm-0-log.ipc --device-id 0 bng.json
