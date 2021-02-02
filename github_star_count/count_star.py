#!/usr/bin/python3

from lxml import etree
import sys
import requests
import json

url = sys.argv[1]
token = sys.argv[2]

headers={"Authorization":"token "+token}
response = requests.get(url, headers=headers)

json_data = json.loads(response.text)
print (json_data['stargazers_count'])