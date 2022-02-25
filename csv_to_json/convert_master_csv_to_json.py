'''convert master csv data to master json file'''
import json
from csv2json import convert

# convert csv to json
with open('master_data.csv', encoding='utf-8-sig') as r, open('data.json', 'w', encoding='utf-8') as w:
    convert(r, w)

# Open newly-converted JSON file
file = open('data.json', encoding='utf-8-sig')
data = json.load(file)
file.close()

# define proper formatting for json
master_format = {
    "VPN": "",
    "Progress": "",
    "Background Date": "",
    "Evaluation Summary": "",
    "URL": "",
    "Pricing": "",
    "Payment Information": "",
    "Extra Options": "",
    "Trial Information": "",
    "Account Creation Information": "",
    "Supported OS": "",
    "OS Applications": "",
    "Browser Extensions": "",
    "Other Devices": "",
    "Number of Devices": {
        "Connections": "",
    },
    "Encryption": "",
    "2FA": "",
    "AdBlock": "",
    "Supported Protocols": "",
    "Multi-Hop": "",
    "P2P": "",
    "Static IP": "",
    "Killswitch": "",
    "Server Locations": "",
    "Data Collection Policy": "Zero Log Policy",
    "Data Retained": "",
    "Advertising Data": "",
    "Payment Data": "",
    "Data Retention Timeline": "",
    "Ownership": " ",
    "Corporate HQ": "",
    "Country of Governance": "",
    "Notes": "",
    "Recent News": "",
    "Reported Malware": {
        "Malicious Intent": ""
    },
    "Windows Operating System": "",
    "Windows Configuration": " ",
    "Windows IP Geolocation": " ",
    "Windows Browser Geolocation": " ",
    "Windows DNS Status": " ",
    "Windows VPN/Proxy Detection": " ",
    "Windows IP Ownership": " ",
    "Windows Notes": "",
    "Ubuntu Operating System": "",
    "Ubuntu Evaluation Date": "",
    "Ubuntu Configuration": " ",
    "Ubuntu IP Geolocation": " ",
    "Ubuntu Browser Geolocation": " ",
    "Ubuntu DNS Status": " ",
    "Ubuntu VPN/Proxy Detection": " ",
    "Ubuntu IP Ownership": " ",
    "Ubuntu Notes": "",
    "Android Operating System": "",
    "Android Configuration": " ",
    "Android IP Geolocation": " ",
    "Android Browser Geolocation": " ",
    "Android DNS Status": " ",
    "Android VPN/Proxy Detection": " ",
    "Android IP Ownership": " ",
    "Android Notes": "",
    "IoS Operating System": "",
    "IoS Configuration": " ",
    "IoS IP Geolocation": " ",
    "IoS Browser Geolocation": " ",
    "IoS DNS Status": " ",
    "IoS VPN/Proxy Detection": " ",
    "IoS IP Ownership": " ",
    "IoS Notes": ""
}

# rewrite json to proper format
master_format['VPN'] = data[0]['VPN']
master_format['Progress'] = "Completed"
master_format['Background Date'] = data[0]['Background Evaluation Date']
master_format['Evaluation Summary'] = data[0]['Evaluation Summary']
master_format['URL'] = data[0]['URL']
master_format['Pricing'] = data[0]['Pricing']
master_format['Payment Information'] = data[0]['Payment Information']
master_format['Extra Options'] = data[0]['Extra Options']
master_format['Trial Information'] = data[0]['Trial Information']
master_format['Account Creation Information'] = data[0]['Account Creation Information']
master_format['Supported OS'] = data[0]['Supported OS']
master_format['OS Applications'] = data[0]['OS Applications']
master_format['Browser Extensions'] = data[0]['Browser Extensions']
master_format['Other Devices'] = data[0]['Other Devices']
master_format['Number of Devices']['Connections'] = data[0]['Number of Devices/Connections']
master_format['Encryption'] = data[0]['Encryption']
master_format['2FA'] = data[0]['2FA']
master_format['AdBlock'] = data[0]['AdBlock']
master_format['Supported Protocols'] = data[0]['Supported Protocols']
master_format['Multi-Hop'] = data[0]['Multi-Hop']
master_format['P2P'] = data[0]['P2P']
master_format['Static IP'] = data[0]['Static IP']
master_format['Killswitch'] = data[0]['Killswitch']
master_format['Server Locations'] = data[0]['Server Locations']
master_format['Data Collection Policy'] = data[0]['Data Collection Policy']
master_format['Data Retained'] = data[0]['Data Retained']
master_format['Advertising Data'] = data[0]['Advertising Data']
master_format['Payment Data'] = data[0]['Payment Data']
master_format['Data Retention Timeline'] = data[0]['Data Retention Timeline']
master_format['Corporate HQ'] = data[0]['Corporate HQ']
master_format['Country of Governance'] = data[0]['Country of Governance']
master_format['Notes'] = data[0]['Notes']
master_format['Recent News'] = data[0]['Recent News']
master_format['Reported Malware']['Malicious Intent'] = data[0]['Reported Malware/Malicious Intent']
master_format['Windows Operating System'] = data[1]['Windows Operating System']
master_format['Windows Evaluation Date'] = data[1]['Windows Evaluation Date']
master_format['Windows Configuration'] = data[1]['Windows Configuration']
master_format['Windows IP Geolocation'] = data[1]['Windows IP Geolocation']
master_format['Windows Browser Geolocation'] = data[1]['Windows Browser Geolocation']
master_format['Windows DNS Status'] = data[1]['Windows DNS Status']
master_format['Windows VPN/Proxy Detection'] = data[1]['Windows VPN/Proxy Detection']
master_format['Windows IP Ownership'] = data[1]['Windows IP Ownership']
master_format['Windows Notes'] = data[1]['Windows Notes']
master_format['Ubuntu Operating System'] = data[1]['Ubuntu Operating System']
master_format['Ubuntu Evaluation Date'] = data[1]['Ubuntu Evaluation Date']
master_format['Ubuntu Configuration'] = data[1]['Ubuntu Configuration']
master_format['Ubuntu IP Geolocation'] = data[1]['Ubuntu IP Geolocation']
master_format['Ubuntu Browser Geolocation'] = data[1]['Ubuntu Browser Geolocation']
master_format['Ubuntu DNS Status'] = data[1]['Ubuntu DNS Status']
master_format['Ubuntu VPN/Proxy Detection'] = data[1]['Ubuntu VPN/Proxy Detection']
master_format['Ubuntu IP Ownership'] = data[1]['Ubuntu IP Ownership']
master_format['Ubuntu Notes'] = data[1]['Ubuntu Notes']
master_format['Android Operating System'] = data[1]['Android Operating System']
master_format['Android Evaluation Date'] = data[1]['Android Evaluation Date']
master_format['Android Configuration'] = data[1]['Android Configuration']
master_format['Android IP Geolocation'] = data[1]['Android IP Geolocation']
master_format['Android Browser Geolocation'] = data[1]['Android Browser Geolocation']
master_format['Android DNS Status'] = data[1]['Android DNS Status']
master_format['Android VPN/Proxy Detection'] = data[1]['Android VPN/Proxy Detection']
master_format['Android IP Ownership'] = data[1]['Android IP Ownership']
master_format['Android Notes'] = data[1]['Android Notes']
master_format['IoS Operating System'] = data[1]['IoS Operating System']
master_format['IoS Evaluation Date'] = data[1]['IoS Evaluation Date']
master_format['IoS Configuration'] = data[1]['IoS Configuration']
master_format['IoS IP Geolocation'] = data[1]['IoS IP Geolocation']
master_format['IoS Browser Geolocation'] = data[1]['IoS Browser Geolocation']
master_format['IoS DNS Status'] = data[1]['IoS DNS Status']
master_format['IoS VPN/Proxy Detection'] = data[1]['IoS VPN/Proxy Detection']
master_format['IoS IP Ownership'] = data[1]['IoS IP Ownership']
master_format['IoS Notes'] = data[1]['IoS Notes']

json_object = json.dumps(master_format, indent=2)

# write properly formatted json to data.json
with open("data.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_object)
