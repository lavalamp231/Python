import os
import nmap3
import pandas as pd

cwd = os.getcwd()
excel_location = (cwd +'\\os_scan.xlsx')

ips = []

# Gathering all the IPs in 192.168.0.* and then appending them into an empty list

nm = nmap3.Nmap()
port_scan_results = nm.scan_top_ports("192.168.0.*")

for r in port_scan_results:
    if '192.168.0' in r:
        ips.append(r)

column_names = ['Hosts', 'Names']
df = pd.DataFrame(columns=column_names)

for ip in ips:
    os_detection_results = nm.nmap_os_detection(ip)
    print(ip)
    #print(os_detection_results)
    for key in os_detection_results:
        #print(key['name'])
        names = key['name']
        my_dict = {'Hosts': ip, 'Names': names}
        print(my_dict)
        df = df.append(my_dict, ignore_index=True)
    
df.to_excel(excel_location)
# From the IP list I am getting the result of each IP 
