import requests
import pdb
import json

discovery_url = 'https://api.us.socrata.com/api/catalog/v1'
resp = requests.get(discovery_url)

baseurl = 'https://data.lacity.org/resource'

max_num = 135604

limit = 10000
res_list = []
scroll_id = None
for offset in range(0, 135000, limit):
    params = {'limit': limit}
    if scroll_id:
        params['scroll_id'] = scroll_id
    res = requests.get(discovery_url, params=params).json()
    try:
        res_list += res['results']
    except:
        pdb.set_trace()
    scroll_id = res_list[-1]['resource']['id']


with open('result/socrata.json', 'w') as fp:
    json.dump(res_list, fp, indent=2)


