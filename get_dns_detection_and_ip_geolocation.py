'''get status of proxy/hosting/mobile results and if ip geolocated to correct location. Results are printed to results.json'''
import json
import pprint


'''get ip_json data'''
with open("data.json", encoding='utf-8') as outFile:
    json_object = json.load(outFile)
    outFile.close()

continents = ['americas', 'europe', 'asia', 'africa', 'oceania']
def dns_detection():
    '''displays mobile/hosting/proxy detection failures'''
    number_of_fails = 0
    results = []
    elements = ['mobile', 'hosting', 'proxy']
    '''print continent, element, detection value'''
    for element in elements:
        for continent in continents:
            results.append([element, continent, json_object[continent]['ip_api']['ipInfo'][element]])

    #get number of fails
    element_fails = []
    for result in results:
        if not result[2] :
            number_of_fails+=1
            element_fails.append(result[0])
    total_failures = "Number of failures: ", number_of_fails
    totalelement_fails = "Failures detected: ", element_fails
    results.append(total_failures)
    results.append(totalelement_fails)

    return results

def ip_geolocation():
    '''prints name of country if the lat-long coordinates do not match up with country given'''
    results = []
    for continent in continents:
        country = (json_object[continent]['ip_api']['ipInfo']['country'])
        lat_lon_resolve = (json_object[continent]['ip_api']['ipInfo']['lat-lon-resolve'])
        if country not in lat_lon_resolve:
            results.append(country)
    if len(results) == 0:
        return "IP addresses geolocate to right country"
    else:
        return results

data = {}
data["ip_geolocation"] = ip_geolocation()
data["dns_detection"] = dns_detection()
print (type(data))
pprint.pprint(data, indent = 2)

with open('results.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent = 2)
    