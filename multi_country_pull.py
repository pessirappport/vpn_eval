import pprint
import json

from single_country_data import get_single_country_data
from countries_in_continent import get_countries_in_continents
from ip_api import get_ip_api_data
print("get_single_country_data")
master_json = {
        "north_america": {},
        "south_america":{},
        "africa": {},
        "europe": {},
        "asia":{},
        "australia":{}
    }
ip_json = get_single_country_data()
countries_list = get_countries_in_continents()

country = ip_json["ip_api"]["ipInfo"]["country"]
country = country.replace(" ","_")
continent = " "
for item in countries_list:
    if item["country"] == country:
        continent = item['continent'].lower()
master_json[continent] = ip_json

with open('data.json', 'w') as outfile:
    json.dump(master_json, outfile, indent=4)



