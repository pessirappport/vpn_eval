'''convert master csv data to master json file'''
import json
from csv2json import convert

# convert csv to json
with open('PIA_data.csv', encoding='utf-8-sig') as r, open('data.json', 'w', encoding='utf-8') as w:
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
    "Windows VPN_Proxy Detection": " ",
    "Windows IP Ownership": " ",
    "Windows Notes": "",
    "Ubuntu Operating System": "",
    "Ubuntu Evaluation Date": "",
    "Ubuntu Configuration": " ",
    "Ubuntu IP Geolocation": " ",
    "Ubuntu Browser Geolocation": " ",
    "Ubuntu DNS Status": " ",
    "Ubuntu VPN_Proxy Detection": " ",
    "Ubuntu IP Ownership": " ",
    "Ubuntu Notes": "",
    "Android Operating System": "",
    "Android Configuration": " ",
    "Android IP Geolocation": " ",
    "Android Browser Geolocation": " ",
    "Android DNS Status": " ",
    "Android VPN_Proxy Detection": " ",
    "Android IP Ownership": " ",
    "Android Notes": "",
    "iOS Operating System": "",
    "iOS Configuration": " ",
    "iOS IP Geolocation": " ",
    "iOS Browser Geolocation": " ",
    "iOS DNS Status": " ",
    "iOS VPN_Proxy Detection": " ",
    "iOS IP Ownership": " ",
    "iOS Notes": ""
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
master_format['Windows Operating System'] = data[0]['Windows Operating System']
master_format['Windows Evaluation Date'] = data[0]['Windows Evaluation Date']
master_format['Windows Configuration'] = data[0]['Windows Configuration']
master_format['Windows IP Geolocation'] = data[0]['Windows IP Geolocation']
master_format['Windows Browser Geolocation'] = data[0]['Windows Browser Geolocation']
master_format['Windows DNS Status'] = data[0]['Windows DNS Status']
master_format['Windows VPN_Proxy Detection'] = data[0]['Windows VPN_Proxy Detection']
master_format['Windows IP Ownership'] = data[0]['Windows IP Ownership']
master_format['Windows Notes'] = data[0]['Windows Notes']
master_format['Ubuntu Operating System'] = data[0]['Ubuntu Operating System']
master_format['Ubuntu Evaluation Date'] = data[0]['Ubuntu Evaluation Date']
master_format['Ubuntu Configuration'] = data[0]['Ubuntu Configuration']
master_format['Ubuntu IP Geolocation'] = data[0]['Ubuntu IP Geolocation']
master_format['Ubuntu Browser Geolocation'] = data[0]['Ubuntu Browser Geolocation']
master_format['Ubuntu DNS Status'] = data[0]['Ubuntu DNS Status']
master_format['Ubuntu VPN_Proxy Detection'] = data[0]['Ubuntu VPN_Proxy Detection']
master_format['Ubuntu IP Ownership'] = data[0]['Ubuntu IP Ownership']
master_format['Ubuntu Notes'] = data[0]['Ubuntu Notes']
master_format['Android Operating System'] = data[0]['Android Operating System']
master_format['Android Evaluation Date'] = data[0]['Android Evaluation Date']
master_format['Android Configuration'] = data[0]['Android Configuration']
master_format['Android IP Geolocation'] = data[0]['Android IP Geolocation']
master_format['Android Browser Geolocation'] = data[0]['Android Browser Geolocation']
master_format['Android DNS Status'] = data[0]['Android DNS Status']
master_format['Android VPN_Proxy Detection'] = data[0]['Android VPN_Proxy Detection']
master_format['Android IP Ownership'] = data[0]['Android IP Ownership']
master_format['Android Notes'] = data[0]['Android Notes']
master_format['iOS Operating System'] = data[0]['iOS Operating System']
master_format['iOS Evaluation Date'] = data[0]['iOS Evaluation Date']
master_format['iOS Configuration'] = data[0]['iOS Configuration']
master_format['iOS IP Geolocation'] = data[0]['iOS IP Geolocation']
master_format['iOS Browser Geolocation'] = data[0]['iOS Browser Geolocation']
master_format['iOS DNS Status'] = data[0]['iOS DNS Status']
master_format['iOS VPN_Proxy Detection'] = data[0]['iOS VPN_Proxy Detection']
master_format['iOS IP Ownership'] = data[0]['iOS IP Ownership']
master_format['iOS Notes'] = data[0]['iOS Notes']

json_object = json.dumps(master_format, indent=2)

# write properly formatted json to data.json
with open("data.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_object)
