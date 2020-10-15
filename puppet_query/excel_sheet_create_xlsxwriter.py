import os
import requests
import xlsxwriter
import json

cwd = os.getcwd()
ca_location = (cwd +'\\ca.pem')
hostname = "^.*"

excel_sheet_path = (cwd + '\\excel_sheets\\')
workbook = xlsxwriter.Workbook(excel_sheet_path + 'server_specs.xlsx')
worksheet = workbook.add_worksheet()

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

host_dict = {}

def disk_detail():
    for i in range(0,len(disks)):
        disk_properties = disks[i]
        sda = disk_properties.get('value',{}).get('sda',{}).get('size','null')
        sdb = disk_properties.get('value',{}).get('sdb',{}).get('size','null')
        host = disk_properties.get('certname',{})
        host_dict[host]["sda"] = sda
        host_dict[host]["sdb"] = sdb

def mem_info():
    for key in memory:
        system_memory_total = key['value']['system']['total']
        system_memory_used = key['value']['system']['used']
        host = key["certname"]
        host_dict[host] = {"memory": system_memory_total}
        host_dict[host]["system_memory_used"] = system_memory_used

def ip():
    for key in ip_address:
        ip = key['value']
        host = key["certname"]
        host_dict[host]["ip"] = ip

def os_info():
    for key in os:
        n = key['value']['name']
        host = key["certname"]
        host_dict[host]["os"] = n

def os_version():
    for key in os:
        full = key['value']['release']['full']
        str(full)
        host = key["certname"]
        host_dict[host]["os_version"] = full

def processor_count():
    for key in cpu_info:
        c = key['value']['count']
        host = key["certname"]
        host_dict[host]["cpu"] = c

def servermodel():
    for key in virtual:
        v = key['value']
        host = key["certname"]
        host_dict[host]["model"] = v

def macaddress():
    for key in macaddress_info:
        ma = key['value']
        host = key['certname']
        host_dict[host]["mac"] = ma

def domain():
    for key in domain_info:
        d = key['value']
        host = key["certname"]
        host_dict[host]["domain"] = d

def subnetmask():
    for key in netmask:
        d = key['value']
        host = key["certname"]
        host_dict[host]["subnet"] = d

#####
mem_info()
servermodel()
os_info()
os_version()
domain()
processor_count()
macaddress()
ip()
subnetmask()
disk_detail()
###

row = 0
col = 0

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Hostnames', bold)
worksheet.write('B1', 'Server Model', bold)
worksheet.write('C1', 'OS', bold)
worksheet.write('D1', 'OS Version', bold)
worksheet.write('E1', 'Domain', bold)
worksheet.write('F1', 'CPU Count', bold)
worksheet.write('G1', 'Total RAM', bold)
worksheet.write('H1', 'Used RAM', bold)
worksheet.write('I1', 'MAC Address', bold)
worksheet.write('J1', 'IP Address', bold)
worksheet.write('K1', 'Subnet', bold)
worksheet.write('L1', 'SDA', bold)
worksheet.write('M1', 'SDB', bold)


for key in host_dict.keys():
    row += 1
    worksheet.write(row,col,key)
    worksheet.write(row, col+1, host_dict[key]["model"])
    worksheet.write(row, col+2, host_dict[key]["os"])
    worksheet.write(row, col+3, host_dict[key]["os_version"])
    worksheet.write(row, col+4, host_dict[key]["domain"])
    worksheet.write(row, col+5, host_dict[key]["cpu"])
    worksheet.write(row, col+6, host_dict[key]["memory"])
    worksheet.write(row, col+7, host_dict[key]["system_memory_used"])
    worksheet.write(row, col+8, host_dict[key]["mac"])
    worksheet.write(row, col+9, host_dict[key]["ip"])
    worksheet.write(row, col+10, host_dict[key]["subnet"])
    worksheet.write(row, col+11, host_dict[key]["sda"])
    worksheet.write(row, col+12, host_dict[key]["sdb"])

workbook.close()