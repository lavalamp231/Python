import os
import nmap3
import pandas as pd

cwd = os.getcwd()
excel_location = (cwd +'\\port_scan.xlsx')

ips = []



# Gathering all the IPs in 192.168.0.* and then appending them into an empty list

nm = nmap3.Nmap()
results = nm.scan_top_ports("192.168.0.*")
host_r = results["192.168.0.10"]

for r in results:
    if '192.168.0' in r:
        ips.append(r)

# From the IP list I am getting the result of each IP 
column_names = ['Hosts', 'Protocols' ,'Ports' ,'State', 'Service']
df = pd.DataFrame(columns=column_names)

for item in ips:
    port_info = (results[item])
    #print(port_info)
    for element in port_info:
        print(element)
        hosts = element['host']
        protocols = element['protocol']
        ports = element['portid']
        state = element['state']
        service = element['service']['name']
        my_dict = {'Hosts': hosts, 'Protocols': protocols, 'Ports': ports, 'State': state, 'Service': service}
        df = df.append(my_dict, ignore_index=True)

df.to_excel(excel_location)


