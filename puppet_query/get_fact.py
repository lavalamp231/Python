import requests
import json

def get_fact(fact):
	url = "http://192.168.0.27:8080/pdb/query/v4/facts/" + fact
	query = {"query":["~","certname",".*.esxi.com"]}
	r = requests.post(url, json=query)
	r = r.text
	json_obj = json.loads(r)
	njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)
	print(njson_obj)

get_fact("hostname")