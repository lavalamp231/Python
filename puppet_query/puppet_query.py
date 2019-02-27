from urllib.request import urlopen
import json

# URL 
url = "http://192.168.0.27:8080/pdb/query/v4/nodes"

# open URL

obj = urlopen(url)

# Convert to string

string = obj.read().decode('utf-8')

# convert to json

json_obj = json.loads(string)

# create pretty json

njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)

#print json

print(njson_obj)

print(url)
