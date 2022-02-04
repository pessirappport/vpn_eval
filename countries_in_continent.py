import json
import requests
def get_countries_in_continents():
    url = 'https://parseapi.back4app.com/classes/Country?order=continent&include=continent&keys=name,continent,continent.name'
    headers = {
        'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja', # This is the fake app's application id
        'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH' # This is the fake app's readonly master key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    countries = []
    for result in data['results']:
        country = {
            "country":result["name"],
            "continent": result["continent"]["name"]
        }
        countries.append(country)
    return (countries)