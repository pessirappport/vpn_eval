import json
from operator import indexOf
continent = "asia"

continent_json = {
    "ip": "123.23.24",
    "country": "China"
}
with open('data.json') as json_file:
    data = json.load(json_file)
    if continent in data:
        pass
    else:
        data[continent] = continent_json
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent = 2)

