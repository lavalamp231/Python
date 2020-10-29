import os
import sys
import json
import pandas as pd
from pandas import json_normalize

column_names = ['Hostnames', 'Server Model', 'OS', 'OS Version', 'Domain', 'CPU Count', 'Total RAM', 'Used RAM', 'SDA', 'SDB']

cwd = os.getcwd()
excel_sheet_path = (cwd + '\\excel_sheet_ansible.xlsx')
server_fact_path = (cwd + '\\server_facts\\')

df = pd.DataFrame(columns=column_names)

list_server_fact_path = os.listdir(server_fact_path)

for json_file in list_server_fact_path:
    open_file = open(server_fact_path + json_file)
    load_file = json.load(open_file)
    if 'ansible_facts' in load_file: # this will help deal with if there is an issue with ansible connecting to the server resulting in a empty json file
        ansible_facts = load_file['ansible_facts']
        hostname = load_file['ansible_facts']['ansible_fqdn']
        print(hostname)
        server_model = load_file['ansible_facts']['facter_virtual']
        operating_system = load_file['ansible_facts']['facter_os']['name']
        os_version = load_file['ansible_facts']['facter_os']['release']['full']
        domain = load_file['ansible_facts']['facter_networking']['domain']
        cpu = load_file['ansible_facts']['facter_processors']['count']
        total_ram = load_file['ansible_facts']['facter_memory']['system']['total']
        used_ram = load_file['ansible_facts']['facter_memory']['system']['used']
        mac_address = load_file['ansible_facts']['facter_networking']['mac']
        ip_address = load_file['ansible_facts']['facter_networking']['ip']
        subnet_mask = load_file['ansible_facts']['facter_networking']['netmask']
        sda = load_file['ansible_facts']['facter_disks']['sda']['size']
        sdb = ansible_facts.get('facter_disks',{}).get('sdb',{}).get('size', 'null')
        my_dict = {'Hostnames': hostname, 'Server Model': server_model, 'OS': operating_system, 'OS Version': os_version, 'Domain': domain, 'CPU Count': cpu, 'Total RAM': total_ram, 'Used RAM': used_ram, 'SDA': sda, 'SDB': sdb}
        df = df.append(my_dict, ignore_index=True)

df.to_excel(excel_sheet_path + 'server_facts_ansible.xlsx')