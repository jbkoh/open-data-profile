import json

with open('result/socrata.json', 'r') as fp:
    data = json.load(fp)


la_cnt = 0
la_data = []
for datum in data:
    if 'lacity' in datum['link']:
        la_data.append(datum)

with open('result/la.json', 'w') as fp:
    json.dump(la_data, fp, indent=2)
