'''get ip information from ipleak.com'''
import random
import string
import requests


def get_ip_leak_data():
    '''pull data from ipleak.com'''

    ip_leak_json = {
        "ip_info":
        {
            "ip": " ",
            "region": " ",
            "country": " "
        },
        "dns_info":
        [],
        "system_discrepancies": []
    }

    def random_string_generator(chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(40))
    '''return host ip'''
    response = requests.get("https://ipleak.net/json/")
    json_response = response.json()
    ip_leak_json['ip_info']['ip'] = json_response['ip']
    ip_leak_json['ip_info']['region'] = json_response['region_name']
    ip_leak_json['ip_info']['country'] = json_response['country_name']
    '''return list of dns servers. Api call only returns one dns address, so function hits api 15 times'''
    for _ in range(15):
        response = requests.get(
            f"https://{random_string_generator()}.ipleak.net/json/")
        json_response = response.json()
        dns_data = {'ip': json_response['ip'], 'region': json_response['region_name'],
                    'country': json_response['country_name']}
        '''if there are only 12 dns addresses, the api will return the last one 3 times (because loops until 15) so this only adds dns data if it's not already in the object'''
        if dns_data not in ip_leak_json['dns_info']:
            ip_leak_json['dns_info'].append(dns_data)
    for i in ip_leak_json['dns_info']:
        if i['country'] != ip_leak_json['ip_info']['country']:
            discrepancies = f"IP addresses resolved to different locations. {i['country']} resolved to {ip_leak_json['ip_info']['country']}"
            ip_leak_json['system_discrepancies'] = discrepancies
        else:
            ip_leak_json['system_discrepancies'] = "No discrepancies noted."

    return ip_leak_json


print(get_ip_leak_data())
