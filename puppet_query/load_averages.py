import requests
import json

url = "http://192.168.0.27:8080/pdb/query/v4/fact-contents"
query = {"query":["and",["=","path",["load_averages", "5m"]], ["<","value", 5]]}

r = requests.get(url, json=query)
#print(r.url)


print(r.json())

