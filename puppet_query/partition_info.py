import requests
import json

#hostname = input("What is the hostname?")

# URL 
url = "http://192.168.0.27:8080/pdb/query/v4/facts/partitions"

# Headers
headers = {'Content-type': 'application/json'}

#query
query = {"query":["~","certname",".*.esxi.com"]}

# doing a POST with json 

r = requests.post(url, json=query)

# converting post into string

r = r.json
print(r)

# Creates a list of dictonaries

json_obj = json.loads(r)

#def(get_environment)
# for environment in json_obj:
# 	hostname = environment['certname']
# 	catalag_env = environment['catalog_environment']
# 	print(hostname, catalag_env)
# create pretty json - will convert to string

njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)

print(njson_obj)