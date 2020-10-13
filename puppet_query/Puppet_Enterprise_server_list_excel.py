import os
import requests
import pandas as pd
import json

cwd = os.getcwd()
ca_location = (cwd +'\\ca.pem')
hostname = "^.*"

def get_oAuth_token():
    token_location = (cwd + '\\token')
    open_token_file = open(token_location, 'r')
    read_token_file = open_token_file.read()
    open_token_file.close()
    return read_token_file


key = get_oAuth_token()

def get_fact(fact):
    url = "https://pe-server.esxi.com:8081/pdb/query/v4/facts/" + fact
    query = {"query":["~","certname", hostname]}
    return_value = requests.post(url, json=query, verify=ca_location, headers={'X-Authentication': key})
    return return_value.json()

memory = get_fact("memory")
disks = get_fact("disks")
ip_address = get_fact("ipaddress")
macaddress_info = get_fact("macaddress")
cpu_info = get_fact("processors")
os = get_fact("os")
virtual = get_fact("virtual")
domain_info = get_fact("domain")
netmask = get_fact("netmask")
hostname = get_fact("fqdn")

column_names = ['Hostname', 'Total RAM', 'Used RAM', 'SDA Size', 'SDB Size', 'IP Address', 'MAC Address', 'CPU Count', 'OS Version', 'Virtual', 'Domain', 'Netmask']
df = pd.DataFrame(columns=column_names)



for keys in memory:
    memory_df = df.append({'Total RAM': keys['value']['system']['total']}, ignore_index=True)

for keys in hostname:
    hostnames = keys['value']
    print(hostnames)
    # df2 = df.insert('Hostname', hostnames)

# def combine_series():
#     empty_dict = {}
#     for keys in hostname:
print(memory_df)

# a = pd.Series(mem_info())
# b = pd.Series(hostname_info())
# b = b.reindex(index =[ 'value'])
# b = b.rename(index={'value': 'FQDN'})

# combined_series = a.append(b)
# series_to_dict = combined_series.to_dict()

# print(series_to_dict)

