import requests
import json

url = "http://192.168.0.27:8080/pdb/query/v4/facts"

#query = {"query":["extract", [["function", "count"]], ["~", "certname", "canary*"]] }
query = {"query":["extract", [["function", "count"], "value"], ["=", "name", "operatingsystem"], ["group_by", "value"]] }
r = requests.post(url, json=query)
r = r.text
#json_obj = json.loads(r)


print(r)