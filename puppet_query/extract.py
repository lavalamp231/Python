import requests
import json

url = "http://192.168.0.27:8080/pdb/query/v4/nodes"

query = {"query":["extract", [["function", "count"]], ["~", "operatingsystem", "Linux"]] }

r = requests.post(url, json=query)
r = r.text
#json_obj = json.loads(r)


print(r)