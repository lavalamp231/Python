# This scripts purpose is to gather do a port scan of the IPs in the 192.168.0.* subnet and create a spreadsheet. 

import os
import nmap3
import pandas as pd


# Doing a 'scan_top_ports' scan to gather all the IPs in 192.168.0.* and then appending them into an empty list called "ips"

ips = []

nm = nmap3.Nmap()
results = nm.scan_top_ports("192.168.0.*")

# Filtering for IPs that start with 192.168.0

for r in results:
    if '192.168.0' in r:
        ips.append(r)


# Creating a dataframe with the below column names
column_names = ['Hosts', 'Protocols' ,'Ports' ,'State', 'Service']
df = pd.DataFrame(columns=column_names)

# from the IPs in the ips list we create a sepeate list of each item then filter out each item to create a dictionary to then be appended
# to the dataframe. 

for item in ips:
    port_info = (results[item])
    for element in port_info:
        print(element)
        hosts = element['host']
        protocols = element['protocol']
        ports = element['portid']
        state = element['state']
        service = element['service']['name']
        my_dict = {'Hosts': hosts, 'Protocols': protocols, 'Ports': ports, 'State': state, 'Service': service}
        df = df.append(my_dict, ignore_index=True)

# Creating a excel sheet from the dataframe. Will create the spreadsheet from current working directory. 

cwd = os.getcwd()
excel_location = (cwd +'\\port_scan.xlsx')

df.to_excel(excel_location)