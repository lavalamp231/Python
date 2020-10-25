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
host_discovery_results = nm_scan.nmap_ping_scan("192.168.0.*")

for item in host_discovery_results:
    ip_address = item['addresses'][0]['addr']
    ips.append(ip_address)


def get_ip_info(ip):
    nm = nmap3.Nmap()
    nm_scan = nmap3.NmapScanTechniques()
    host_discovery_results = nm_scan.nmap_ping_scan(ip)
    for item in host_discovery_results:
        ip_address = item['addresses'][0]['addr']
        try:
            mac_address = item['addresses'][1]['addr']
        except Exception:
            mac_address = str('not_available')
        try:
            vendor = item['addresses'][1]['vendor']
        except Exception:
            vendor = str('not_available')
        hostnames = item['hostname']
        if not hostnames:
            hostnames = 'unknown'
        else:
            hostnames = hostnames[0]
            hostnames = hostnames['name']
        my_dict = {'Hostnames': hostnames, 'IPs': ip_address, 'mac_address': mac_address, 'Vendor': vendor}
        return my_dict

# Creating a dataframe with the below column names

column_names = ['Hostnames', 'IPs', 'Protocols' ,'Ports' ,'Names', 'State', 'MACaddress', 'Vendor']
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
        print(key)
        protocols = key['protocol']
        state = key['state']
        ports = key['port']
        names = key['service']['name']
        macad = get_ip_info(ip)['mac_address']
        vendor_info = get_ip_info(ip)['Vendor']
        my_dict = {'Hostnames': host_names, 'IPs': ip, 'Protocols': protocols, 'Ports': ports, 'Names': names, 'State': state, 'MACaddress': macad, 'Vendor': vendor_info}
        #print(my_dict)
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
