import requests
import json



#hostname = input("What is the hostname?")

# URL 
url = "http://192.168.0.27:8080/pdb/query/v4/nodes"

# Headers
headers = {'Content-type': 'application/json'}

#query
query = {"query":["~","certname",".*.esxi.com"], "order_by":[{"field":"certname"}],"limit":3}

# doing a POST with json 

r = requests.post(url, json=query)

# converting post into string

r = r.text

# Creates a list of dictonaries

json_obj = json.loads(r)

#def(get_environment)
for environment in json_obj:
	environment = environment['catalog_environment']
	print(environment)
# create pretty json - will convert to string

njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)

#print(njson_obj['certname'])
print(njson_obj)