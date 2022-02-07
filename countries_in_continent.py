import json
import requests
import pprint
def get_countries_in_continents():
    
    url = 'https://restcountries.com/v2/all?fields=name,region'
    response = requests.get(url)  
    response = response.json()
    return (response)

