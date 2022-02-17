'''get name, registrant, and registrant location from icann.lookup.org'''
import requests

def get_ip_list(ip_json):
    '''get list of ip addresses and dns servers from master json list'''
    ip_list = []
    if ip_json["ip_api"]:
        ip_list.append(ip_json["ip_api"]["ipInfo"]["query"])
    if ip_json["ip_api"]["dnsInfo"]["ip"]:
        ip_list.append(ip_json["ip_api"]["dnsInfo"]["ip"])
    for i in ip_json["dns_leak_test"]:
        ip_list.append(i["ip"])
    ip_list.append(ip_json['ip_leak']["ip_info"]["ip"])
    for i in ip_json["ip_leak"]["dns_info"]:
        ip_list.append(i["ip"])
    ip_list.append(ip_json["whoer"]["ip"])

    ip_list = [i for n, i in enumerate(ip_list) if i not in ip_list[:n]]
    return ip_list


def get_icann_lookup_data(ip_json):
    '''feed each ip address and dns through icann.lookup.org and sort through response'''
    list_ip = get_ip_list(ip_json)
    list_name =[]
    list_registrant = []
    list_registrant_loc = []

    icann_lookup_json = []
    for ip_address in list_ip:
        response = requests.get('https://rdap.arin.net/registry/ip/'+ip_address)
        response_json = response.json()

        '''name'''
        try:
            name = (response_json['name'])
            list_name.append(name)
        except Exception as error:
            response_name = 'unknown'
            list_name.append(response_name)

        '''registrant'''
        try:
            registrant = response_json['entities'][0]['vcardArray'][1][1][3]
            list_registrant.append(registrant)
        except Exception as error:
            registrant = 'unknown'
            list_registrant.append(registrant)

        '''registrant location'''
        try:
            registrant_loc_dict = response_json['entities'][0]['vcardArray'][1][2][1]
            registrant_loc_with_line_breaks = (registrant_loc_dict.get('label'))
            registrant_loc = registrant_loc_with_line_breaks.replace("\n"," ")
            registrant_loc = registrant_loc.replace("\r", " ")
            list_registrant_loc.append(registrant_loc)
        except Exception as error:
            registrant_loc = 'unknown'
            list_registrant_loc.append(registrant_loc)

    for i in range (len(list_ip)):
        ip_dict = {
            "ip_address": " ",
            "name": " ",
            "registrant_name": " ",
            "registrant_location": " "
        }
        ip_dict['ip_address'] = list_ip[i]
        ip_dict['name'] = list_name[i]
        ip_dict['registrant_name'] = list_registrant[i]
        ip_dict['registrant_location'] = list_registrant_loc[i]
        icann_lookup_json.append(ip_dict)

    return icann_lookup_json
