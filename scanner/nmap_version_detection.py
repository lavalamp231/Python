import os
import nmap3
import pandas as pd
import socket

cwd = os.getcwd()
excel_location = (cwd +'\\nmap_version_detection.xlsx')

ips = []

nm = nmap3.Nmap()
port_scan_results = nm.scan_top_ports("192.168.0.*")

for r in port_scan_results:
    if '192.168.0' in r:
        ips.append(r)

column_names = ['Hosts', 'Protocols' ,'Ports' ,'Names', 'State']
df = pd.DataFrame(columns=column_names)

for ip in ips:
    result = nm.nmap_version_detection(ip)
    for key in result:
        protocols = key['protocol']
        state = key['state']
        ports = key['port']
        names = key['service']['name']
        my_dict = {'Hosts': ip, 'Protocols': protocols, 'Ports': ports, 'Names': names, 'State': state}
        print(my_dict)
        df = df.append(my_dict, ignore_index=True)
        print(df)

df.to_excel(excel_location)
