import json
import requests


#baseurls = ['https://data.boston.gov/api/3'
#           ]

baseurl = 'https://data.boston.gov/api/3'
packages = requests.get(baseurl + '/action/package_list_with_resources', 
                        params={'limit':200}).json()['result']
dataset = packages[0]
print(dataset)
