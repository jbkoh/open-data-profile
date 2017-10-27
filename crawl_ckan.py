import json
import requests
import pdb


#baseurls = ['https://data.boston.gov/api/3'
#           ]

baseurl = 'https://data.boston.gov/api/3'
data = requests.get(baseurl + '/action/current_package_list_with_resources',
                        params={'limit':10000}).json()['result']

with open('result/boston.json', 'w') as fp:
    json.dump(data, fp)
