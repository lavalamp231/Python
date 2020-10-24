# This scripts purpose is to gather do a nmap_version_detection scan of the IPs in the 192.168.0.* subnet and create a spreadsheet. 

import os
import nmap3
import pandas as pd
import socket
import time

# Gathering all the IPs in 192.168.0.* and then appending them into an empty list called ips

ips = []
nm = nmap3.Nmap()
nm_scan = nmap3.NmapScanTechniques()
#host_discovery_results = nm_scan.nmap_idle_scan("192.168.0.*")
host_discovery_results = nm_scan.nmap_ping_scan("192.168.0.*")
#print(host_discovery_results)

for item in host_discovery_results:
    print(item)
    ip_address = item['addresses'][0]['addr']
    ips.append(ip_address)

