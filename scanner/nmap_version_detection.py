# This scripts purpose is to gather do a nmap_version_detection scan of the IPs in the 192.168.0.* subnet and create a spreadsheet. 

import os
import nmap3
import pandas as pd
import socket
import time

# Gathering all the IPs in 192.168.0.* and then appending them into an empty list called ips

ips = []
nm = nmap3.Nmap()
port_scan_results = nm.scan_top_ports("192.168.0.*")

for r in port_scan_results:
    if '192.168.0' in r:
        ips.append(r)

# Creating a dataframe with the below column names

column_names = ['Hostnames', 'Hosts', 'Protocols' ,'Ports' ,'Names', 'State']
df = pd.DataFrame(columns=column_names)

# from the IPs in the ips list we create a sepeate list of each item then filter out each item to create a dictionary to then be appended
# to the dataframe. 

for ip in ips:
    result = nm.nmap_version_detection(ip)
    try:
        host_names = socket.gethostbyaddr(ip)
        host_names = host_names[0]
    except Exception:
        host_names = str('Unknown')
    for key in result:
        protocols = key['protocol']
        state = key['state']
        ports = key['port']
        names = key['service']['name']
        my_dict = {'Hostnames': host_names, 'Hosts': ip, 'Protocols': protocols, 'Ports': ports, 'Names': names, 'State': state}
        print(my_dict)
        df = df.append(my_dict, ignore_index=True)
        print(df)

# Creating a excel sheet from the dataframe. Will create the spreadsheet from current working directory. 
cwd = os.getcwd()
excel_location = (cwd +'\\nmap_version_detection.xlsx')

# putting an exception to deal with if the excel sheet is already openeded.
try:
    df.to_excel(excel_location)
except:
    time.sleep(30)
    print('check if excel sheet is opened')
    df.to_excel(excel_location)
