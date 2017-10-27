import json
from urllib.parse import urlparse

with open('result/socrata.json', 'r') as fp:
    data = json.load(fp)


la_cnt = 0
la_data = []
for datum in data:
    if 'lacity' in datum['link']:
        la_data.append(datum)

urls = set()
for datum in data:
    url = datum['link']
    urls.add(urlparse(url).hostname)

with open('result/la.json', 'w') as fp:
    json.dump(la_data, fp, indent=2)

print('# of Hosts: ', len(urls))
