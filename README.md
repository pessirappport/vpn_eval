# vpn_eval

pulls IP data from different IP data gathering websites

1. multi_country_pull gathers data from a single country at a time (user's VPN country) and adds it to data.json
2. multi_country_pull should be run 5 times (asia, europe, africa, oceania, americas)
3. get_dns_detection_and_ip_geolocation returns ip_geolocation status and any fails, and a list of country, (hosting/proxy/mobile), and detection status

# csv_to_json

converts csv to json and then validates it for seamless upload to webpage

1. Add csv to folder and rename it "vpn_eval.csv"
2. convert.py will change it to a json and dump it into data.json
3. validate_json compares it to the json schema for web page and will return whether data format is valid or invalid"
