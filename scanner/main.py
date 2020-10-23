import os
import nmap3
import xlsxwriter

nm = nmap3.Nmap()
results = nm.scan_top_ports("192.168.0.*")
host_r = results["192.168.0.10"]

ips = []

# for host in host_r:
#     print(host)

for r in results:
    if '192.168.0' in r:
        ips.append(r)
print(ips)

for item in ips:
    port_info = (results[item])
    # for element in port_info:
    #     print(element['name'])
