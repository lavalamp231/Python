import requests
import json

#hostname = input("What is the hostname?")

# URL 
url = "http://192.168.0.1/1.1.16/index.html"

r = requests.get(url, auth=('admin','admin'))

print r.text



