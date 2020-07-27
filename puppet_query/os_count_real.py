import requests
import json


key = '0fjTyHS0X1ZaOeOu37_0Hlyd3Bnp4CCjAVUGFRKgje2k'

def get_count():
   url = "https://ausplpmom01.us.dell.com:8081/pdb/query/v4/facts"
   query = {"query":["extract", [["function", "count"], "value"], ["=", "name", "operatingsystem"], ["group_by", "value"]] }
   r = requests.post(url, json=query, verify="C:/Users/Andrew_Simons/prod_cert/ca.pem", headers={'X-Authentication': key})
   print(r.text)

get_count()

