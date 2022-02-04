import requests

def get_ip_api_data():

    ip_api_json = {
            "ipInfo": {
                "status": " ",
                "country": " ",
                "regionName": " ",
                "city": " ",
                "lat-lon": " ",
                "lat-lon-resolve": " ",
                "isp": " ",
                "mobile": " ",
                "proxy": " ",
                "hosting": " ",
                "query": " "
            },
            "dnsInfo": {
                "geo": " ",
                "ip": " "
            }
        }
    key = "riWnWmVRqcqDI7NHPp3832mmT5wDNG3VhihAvBM85oTzh5r2iD"
    #get ip information
    response = requests.get("http://ip-api.com/json/?fields=status,message,country,regionName,city,lat,lon,isp,mobile,proxy,hosting,query")
    json_response = response.json()

    #get dns information
    response = requests.get("http://edns.ip-api.com/json")
    dns_json_response = response.json()
    if json_response['status'] == 'fail':
        print ("API limit exceeded for ip-api.com")
    else:

        #get lat_lon coordinates
        lat_lon = json_response['lat'], json_response['lon']

        #reverse geocode the coordinates to find city, country
        url = ("https://api.myptv.com/geocoding/v1/locations/by-position/{}/{}?language=en".format(json_response['lat'], json_response['lon']))
        headers = {
            'apiKey': "NzM0NjdlOTcwMDY3NDU2NTkxMjhjNjVmMTQ3NGU3ZmM6MDU2NWNiYTMtYjJjMy00NDVhLWJiMjMtZjAwYjQyMTI5NWZl"
        }
        response = requests.request("GET", url, headers=headers)
        location_resolve = response.json()
        city = location_resolve['locations'][0]['address']['city']
        state = location_resolve['locations'][0]['address']['state']
        country = location_resolve['locations'][0]['address']['countryName']
        lat_lon_resolve = (city, state, country)
        ip_api_json['ipInfo']['status'] = json_response['status']
        ip_api_json['ipInfo']['country'] = json_response['country']
        ip_api_json['ipInfo']['regionName'] = json_response['regionName']
        ip_api_json['ipInfo']['city'] = json_response['city']
        ip_api_json['ipInfo']['lat-lon'] = lat_lon
        ip_api_json['ipInfo']['lat-lon-resolve'] = lat_lon_resolve
        ip_api_json['ipInfo']['isp'] = json_response['isp']
        ip_api_json['ipInfo']['mobile'] = json_response['mobile']
        ip_api_json['ipInfo']['proxy'] = json_response['proxy']
        ip_api_json['ipInfo']['hosting'] = json_response['hosting']
        ip_api_json['ipInfo']['query'] = json_response['query']
        ip_api_json['dnsInfo']['geo'] = dns_json_response['dns']['geo']
        ip_api_json['dnsInfo']['ip'] = dns_json_response['dns']['ip']

        return ip_api_json
