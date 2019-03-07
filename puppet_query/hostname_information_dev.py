import requests
import json

hostname = "canary.esxi.com"

def get_fact(fact, hostname):
	url = "http://192.168.0.27:8080/pdb/query/v4/facts/" + fact
	query = {"query":["~","certname", hostname]}
	r = requests.post(url, json=query)
	r = r.text
	json_obj = json.loads(r)
	#njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)
	return json_obj

memory = get_fact("memory", hostname)
partitions = get_fact("partitions", hostname)
ip_address = get_fact("ipaddress", hostname)
cpu_count = get_fact("processors", hostname)
os = get_fact("os", hostname)
virtual = get_fact("virtual", hostname)
macaddress_info = get_fact("macaddress", hostname)
domain_info = get_fact("domain", hostname)
netmask = get_fact("netmask", hostname)
hostname_info = get_fact("hostname", hostname)

def mem_info(key):
  for key in memory:
  	#hostname = key['certname']
  	#catalag_env = key['environment']
  	#swap_memory_total = key['value']['swap']['total']
  	system_memory_total = key['value']['system']['total']
  	print("Total System Memory: " + system_memory_total)

def get_hostname(key):
	for key in hostname_info:
		h = key['value']
		print("Hostname: " + h)

def ip(key):
	for key in ip_address:
		ip = key['value']
		print("IP Address: " + ip)

def os_info(key):
	for key in os:
		n = key['value']['name']
		full = key['value']['release']['full']
		t = ("OS: " + n, "\nVersion: " + full)
		t = ''.join(t)
		print(t)

def processor_count(key):
	for key in cpu_count:
		c = key['value']['count']
		c = str(c)
		print("CPU Count: " + c)

def isvirtual(key):
	for key in virtual:
		v = key['value']
		print("Platform: " + v)

def macaddress(key):
	for key in macaddress_info:
		ma = key['value']
		print("MAC Address: " + ma)

def domain(key):
	for key in domain_info:
		d = key['value']
		print("Domain: " + d)

def subnetmask(key):
	for key in netmask:
		d = key['value']
		print("Subnet Mask: " + d)

get_hostname(hostname)
domain(hostname)
os_info(hostname)
ip(hostname)
subnetmask(hostname)
macaddress(hostname)
processor_count(hostname)
mem_info(hostname)

