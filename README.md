# vpn_eval

pulls IP data from different IP data gathering websites

1. multi_country_pull gathers data from a single country at a time (user's VPN country) and adds it to data.json.
2. multi_country_pull should be run 5 times (asia, europe, africa, oceania, americas).
3. get_dns_detection_and_ip_geolocation returns ip_geolocation status and any fails, and a list of country, (hosting/proxy/mobile), and detection status.

# csv_to_json

1. If user has csv: Add csv to folder and rename it "master_data.csv." Data can include background evaluation and technical evaluations for one vpn at a time. When evaluating multiple VPNs, use one csv per evaluation.
   If user has json: Add json to folder and rename 'data.json'.
2. convert_master_csv_to_json.py will change it to a json and dump it into data.json.
3. validate_json compares it to the json schema will return whether data format is valid or invalid. It will also confirm whether entries are aligned with web page options (i.e. "No issues; concerns; failures") and that all fields are the proper data type (date, url, etc.).
4. break_master_json_to_two.py is a module that takes the master_json and breaks into a background investigation and four separate technical evaluations, based on OS, to seamlessly get integrated in web page data flow.

        ( master_format.csv - csv schema
        master_format.json - json schema)