import requests
import json
import os

#hostname = input("What is the hostname?")

# URL 
url = "https://pe-server.esxi.com:8081/pdb/query/v4/nodes"

# Headers
headers = {'Content-type': 'application/json'}

#query
query = {"query":["~","certname",".*.esxi.com"], "order_by":[{"field":"certname"}],"limit":100}

# doing a POST with json 

username = os.getenv('username')
f = ("C:/Users/" + username + "/ca.pem")

r = requests.post(url, json=query, verify=f)

# converting post into string

r = r.text

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