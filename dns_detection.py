import json

with open("data.json") as outFile:
    json_object = json.load(outFile)
    outFile.close()

continents = ['americas', 'europe', 'asia', 'africa', 'oceania']
def dns_detection():
    numberOfFails = 0
    results = []
    for continent in continents:
        print((json_object[continent]['ip_api']['ipInfo']['proxy']), ": proxy")
        print((json_object[continent]['ip_api']['ipInfo']['hosting']), ": hosting")
        print((json_object[continent]['ip_api']['ipInfo']['mobile']), ": mobile")
        results.append(json_object[continent]['ip_api']['ipInfo']['proxy'])
        results.append(json_object[continent]['ip_api']['ipInfo']['hosting'])
        results.append(json_object[continent]['ip_api']['ipInfo']['mobile'])
    for result in results:
        if not result :
            numberOfFails+=1
    print("Number of failures:", numberOfFails)

def ip_geolocation():
    #prints name of country if the lat-long coordinates do not match up with country given
    results = []
    for continent in continents:
        country = (json_object[continent]['ip_api']['ipInfo']['country'])
        lat_lon_resolve = (json_object[continent]['ip_api']['ipInfo']['lat-lon-resolve'])
        if country not in lat_lon_resolve:
            results.append(country)
    if len(results) == 0:
        print("IP addresses geolocate to right country")
    else: print (results)

ip_geolocation()
print("---------------------------------------")
dns_detection()

