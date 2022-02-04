import json
from ip_api import get_ip_api_data
from dns_leak_test import get_dns_test_leak_data
from ip_leak import get_ip_leak_data
from icann_lookup import get_icann_lookup_data
from whoer import get_whoer_data

def get_single_country_data():
    print("Starting tests now")
    ip_json = {
        "ip_api": {},
        "dns_leak_test":{},
        "ip_leak": {},
        "whoer": {},
        "icann_lookup":{}
    }

    ip_api_data = get_ip_api_data()
    dns_leak_test_data = get_dns_test_leak_data()
    ip_leak_data = get_ip_leak_data()
    whoer_json = get_whoer_data()

    #add datasets to master json
    ip_json["ip_api"] = ip_api_data
    ip_json["dns_leak_test"] = dns_leak_test_data
    ip_json["ip_leak"] = ip_leak_data
    ip_json["whoer"] = whoer_json

    #find ip address owners
    icann_lookup_data = get_icann_lookup_data(ip_json)

    ip_json["icann_lookup"] = icann_lookup_data


    with open('mock_data.json', 'w') as outfile:
        json.dump(ip_json, outfile, indent=4)
    
    return (ip_json)