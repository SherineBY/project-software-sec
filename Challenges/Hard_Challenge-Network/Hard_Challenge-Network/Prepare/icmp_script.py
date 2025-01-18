from scapy.all import *

hidden_message_part_2 = "CTF_part_2_hidden"
packet = IP(dst="8.8.8.8")/ICMP()/hidden_message_part_2
wrpcap("icmp_hidden.pcap", [packet])
