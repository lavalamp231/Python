import requests
import json



hostname = input("What is the hostname?")

# URL 
url = "http://192.168.0.27:8080/pdb/query/v4/nodes"

# Headers
headers = {'Content-type': 'application/json'}

#query
query = {"query":["=","certname","$hostname"]}

r = requests.post(url, json=query)

r = r.text

json_obj = json.loads(r)

# create pretty json

njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)

#print json

print(njson_obj)