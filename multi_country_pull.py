import pprint
import json

from single_country_data import get_single_country_data
from countries_in_continent import get_countries_in_continents

print("get_single_country_data")
master_json = {
        "americas":{},
        "africa": {},
        "europe": {},
        "asia":{},
        "oceania":{}
    }

#get data from one country
ip_json = get_single_country_data()
countries_list = get_countries_in_continents()
country = ip_json["ip_api"]["ipInfo"]["country"]
if (country == "United Kingdom"):
    country = "United Kingdom of Great Britain and Northern Ireland"
elif (country == "United States"):
    country == "United States of America"
print(country)

#find which continent it is in
continent = " "
for item in countries_list:
    if item["name"] == country:
        continent = item['region'].lower()
print(continent)

#get json data
with open('data.json') as json_file:
    data = json.load(json_file)
    #add it to correct place in file
    # if continent in data:
    #     pass
    # else:
    data[continent] = ip_json
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, 
                        indent=2,  
                        separators=(',',': '))

    




