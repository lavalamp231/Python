import requests
import json

def get_fact(fact):
	url = "http://192.168.0.27:8080/pdb/query/v4/facts/" + fact
	query = {"query":["~","certname",".*.esxi.com"]}
	r = requests.post(url, json=query)
	r = r.text
	json_obj = json.loads(r)
	return json_obj

def get_fact_content():
	url = "http://192.168.0.27:8080/pdb/query/v4/fact-contents/"
	query = {"query":["=","path",[ "mountpoints", "/", "options", 0 ]]}
	r = requests.post(url, json=query)
	print(r)
	r = r.text
	json_obj = json.loads(r)
	print(json_obj)

memory = get_fact("memory")
ip_address = get_fact("ipaddress")
print(ip_address)
#print(memory)
get_fact_content()

def mem_info(key):
  for key in memory:
  	hostname = key['certname']
  	catalag_env = key['environment']
  	swap_memory_total = key['value']['swap']['total']
  	system_memory_total = key['value']['system']['total']
  	print(hostname, catalag_env, swap_memory_total, system_memory_total)

def ip_address_info(key):
	for key in ip_address:
		ipaddress = key['value']
		print(ipaddress)

#mem_info(memory)
m = mem_info(memory)
i = ip_address_info(ip_address)

