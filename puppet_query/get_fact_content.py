import requests
import json

# def get_fact(fact):
#  	url = "http://192.168.0.27:8080/pdb/query/v4/facts/" + fact
#  	query = {"query":["~","certname",".*.esxi.com"]}
#  	r = requests.post(url, json=query)
#  	r = r.text
#  	json_obj = json.loads(r)
#  	return json_obj

def get_fact_content():
	url = "http://192.168.0.27:8080/pdb/query/v4/fact-contents"
	query = 'query=["and",["=","path",["load_averages", "5m"]], [">","value", 5]]'
	r = requests.get(url, json=query)
	data = r.json()


	#json_obj = json.loads(r)

	#return json_obj
	return(data)
	# njson_obj = json.dumps(json_obj, indent=4, sort_keys=True)

	#print(njson_obj)

#ip_address = get_fact("ipaddress")
#print(ip_address)


# def test():
# 	url = "http://192.168.0.27:8080/pdb/query/v4/fact-contents"
# 	r = requests.get(url)
# 	r.json()

# test()
p = get_fact_content()
print(p)