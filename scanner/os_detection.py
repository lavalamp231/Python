# This scripts purpose is to gather do a OS scan of the IPs in the 192.168.0.* subnet and create a spreadsheet. 

import os
import nmap3
import pandas as pd

# Gathering all the IPs in 192.168.0.* and then appending them into an empty list called ips

ips = []
nm = nmap3.Nmap()
port_scan_results = nm.scan_top_ports("192.168.0.*")

for r in port_scan_results:
    if '192.168.0' in r:
        ips.append(r)

# Creating a dataframe with the below column names

column_names = ['Hosts', 'Names', 'Vendor']
df = pd.DataFrame(columns=column_names)

# from the IPs in the ips list we create a sepeate list of each item then filter out each item to create a dictionary to then be appended
# to the dataframe. 

for ip in ips:
    os_detection_results = nm.nmap_os_detection(ip)
    print(ip)
    #print(os_detection_results)
    for key in os_detection_results:
        #print(key['name'])
        names = key['name']
        vendors = key['osclass']['vendor']
        my_dict = {'Hosts': ip, 'Names': names, 'Vendor': vendors}
        print(my_dict)
        df = df.append(my_dict, ignore_index=True)


# Creating a excel sheet from the dataframe. Will create the spreadsheet from current working directory. 
cwd = os.getcwd()
excel_location = (cwd +'\\os_scan.xlsx')

df.to_excel(excel_location)

