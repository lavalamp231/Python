import requests
import os
import json
import nmap, socket

# Summary: Receiving the request from dns1.esxi.com then gathering all IPs 
# Date: 6/30/21

###################### LISTS ###########################

new_list = []

########################################################

# using requests to do a GET request to dns1.esxi.com. From there I am converting it into a string then converting it
# into a list. 

def get_request_dns():
	url = "https://dns1.esxi.com/"
	r = requests.get(url, verify=False)
	r = r.text
	list_of_dns_info = r.split("\n")
	return list_of_dns_info

# from the list generated I am gathering all of the DNS servers then creating another list DNS entries

def create_list_of_dns_servers():
	for element in get_request_dns():
		element = element.split()
		new_list.append(element)
		n = new_list[:-1]
	return n
		
# Getting list 'n' then grabbing the ip addresses in the list then converting the strings into integers then appending it to
# fourth_octet_list. 

def get_last_octet():
	fourth_octet_list = []
	for item in create_list_of_dns_servers():
		item = item[3].split(".")
		fourth_octet_list.append(int(item[3]))
	fourth_octet_list = sorted(fourth_octet_list)
	return fourth_octet_list


def verify_ip_is_not_in_use():
	ip_addr_without_last_octet = "192.168.0."
	scanner = nmap.PortScanner()
	for ip in get_last_octet():
		new_ip = ip_addr_without_last_octet + str(ip)
		host = socket.gethostbyname(new_ip)
		scanner.scan(host, '1', '-v')
		print(new_ip, scanner[host].state())

verify_ip_is_not_in_use()


