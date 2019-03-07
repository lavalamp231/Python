import requests
import json

hostname = "canary.esxi.com"

def get_fact(hostname):
	url = "http://192.168.0.27:8080/pdb/query/v4/?query=facts[] {(facts{(name = 'clientcert' and value ~ '$server')})}"
	#query = {"query":["~","certname",".*.esxi.com"]}
	r = requests.post(url)
	r = r.text
	# json_obj = json.loads(r)
	# #njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)
	# return json_obj

t = get_fact(hostname)

print(t)