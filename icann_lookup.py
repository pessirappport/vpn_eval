import requests

def get_ip_list(ip_json):
    ip_list = []
    if (ip_json["ip_api"]["ipInfo"]): ip_list.append(ip_json["ip_api"]["ipInfo"]["query"])
    if (ip_json["ip_api"]["dnsInfo"]): ip_list.append(ip_json["ip_api"]["dnsInfo"]["ip"])
    for i in ip_json["dns_leak_test"]:
        ip_list.append(i["ip"])
    ip_list.append(ip_json['ip_leak']["ip_info"]["ip"])
    for i in ip_json["ip_leak"]["dns_info"]:
        ip_list.append(i["ip"])  
    ip_list.append(ip_json["whoer"]["ip"])
    ip_list = [i for n, i in enumerate(ip_list) if i not in ip_list[:n]] 
    return ip_list


def get_icann_lookup_data(ip_json):
    list_ip = get_ip_list(ip_json)
    list_name =[]
    list_registrant = []
    list_registrant_loc = [] 

    icann_lookup_json = []
    for ip in list_ip:
        print(ip)
        response = requests.get('https://rdap.arin.net/registry/ip/'+ip)
        response_json = response.json()

        #name
        try:
            name = (response_json['name'])
            list_name.append(name)
        except Exception as e:
            response_name = 'unknown'
            list_name.append(response_name) 

        #registrant
        try:
            registrant = response_json['entities'][0]['vcardArray'][1][1][3]
            list_registrant.append(registrant)
        except Exception as e:
            registrant = 'unknown'
            list_registrant.append(registrant)

        #registrant location
        try:
            registrant_loc_dict = response_json['entities'][0]['vcardArray'][1][2][1]
            registrant_loc_with_line_breaks = (registrant_loc_dict.get('label'))
            registrant_loc = registrant_loc_with_line_breaks.replace("\n"," ")
            registrant_loc = registrant_loc.replace("\r", " ")
            list_registrant_loc.append(registrant_loc)
        except Exception as e:
            registrant_loc = 'unknown'
            list_registrant_loc.append(registrant_loc)  

    for i in range (len(list_ip)):
        dict = {
            "ip_address": " ",
            "name": " ",
            "registrant_name": " ",
            "registrant_location": " "
        }
        dict['ip_address'] = list_ip[i]
        dict['name'] = list_name[i]
        dict['registrant_name'] = list_registrant[i]
        dict['registrant_location'] = list_registrant_loc[i]
        icann_lookup_json.append(dict)

    return icann_lookup_json
