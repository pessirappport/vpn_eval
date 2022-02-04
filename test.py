import pprint
import json

from single_country_data import get_single_country_data
print("get_single_country_data")
ip_json = get_single_country_data()

country = ip_json["ip_api"]["ipInfo"]["country"]
country = country.replace(" ","_").lower()
print(country)
master_json = {
    country: ip_json
}
print(master_json)
with open('data.json', 'a') as outfile:
    json.dump(master_json, outfile, indent=4)


