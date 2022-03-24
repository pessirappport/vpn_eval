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
for i in range (len(data)):
    master_format['VPN'] = data[i]['VPN']
    master_format['Progress'] = "Completed"
    master_format['Background Date'] = data[i]['Background Evaluation Date']
    master_format['Evaluation Summary'] = data[i]['Evaluation Summary']
    master_format['URL'] = data[i]['URL']
    master_format['Pricing'] = data[i]['Pricing']
    master_format['Payment Information'] = data[i]['Payment Information']
    master_format['Extra Options'] = data[i]['Extra Options']
    master_format['Trial Information'] = data[i]['Trial Information']
    master_format['Account Creation Information'] = data[i]['Account Creation Information']
    master_format['Supported OS'] = data[i]['Supported OS']
    master_format['OS Applications'] = data[i]['OS Applications']
    master_format['Browser Extensions'] = data[i]['Browser Extensions']
    master_format['Other Devices'] = data[i]['Other Devices']
    master_format['Number of Devices']['Connections'] = data[i]['Number of Devices/Connections']
    master_format['Encryption'] = data[i]['Encryption']
    master_format['2FA'] = data[i]['2FA']
    master_format['AdBlock'] = data[i]['AdBlock']
    master_format['Supported Protocols'] = data[i]['Supported Protocols']
    master_format['Multi-Hop'] = data[i]['Multi-Hop']
    master_format['P2P'] = data[i]['P2P']
    master_format['Static IP'] = data[i]['Static IP']
    master_format['Killswitch'] = data[i]['Killswitch']
    master_format['Server Locations'] = data[i]['Server Locations']
    master_format['Data Collection Policy'] = data[i]['Data Collection Policy']
    master_format['Data Retained'] = data[i]['Data Retained']
    master_format['Advertising Data'] = data[i]['Advertising Data']
    master_format['Payment Data'] = data[i]['Payment Data']
    master_format['Data Retention Timeline'] = data[i]['Data Retention Timeline']
    master_format['Corporate HQ'] = data[i]['Corporate HQ']
    master_format['Country of Governance'] = data[i]['Country of Governance']
    master_format['Notes'] = data[i]['Notes']
    master_format['Recent News'] = data[i]['Recent News']
    master_format['Reported Malware']['Malicious Intent'] = data[i]['Reported Malware/Malicious Intent']
    master_format['Windows Operating System'] = data[i]['Windows Operating System']
    master_format['Windows Evaluation Date'] = data[i]['Windows Evaluation Date']
    master_format['Windows Configuration'] = data[i]['Windows Configuration']
    master_format['Windows IP Geolocation'] = data[i]['Windows IP Geolocation']
    master_format['Windows Browser Geolocation'] = data[i]['Windows Browser Geolocation']
    master_format['Windows DNS Status'] = data[i]['Windows DNS Status']
    master_format['Windows VPN_Proxy Detection'] = data[i]['Windows VPN_Proxy Detection']
    master_format['Windows IP Ownership'] = data[i]['Windows IP Ownership']
    master_format['Windows Notes'] = data[i]['Windows Notes']
    master_format['Ubuntu Operating System'] = data[i]['Ubuntu Operating System']
    master_format['Ubuntu Evaluation Date'] = data[i]['Ubuntu Evaluation Date']
    master_format['Ubuntu Configuration'] = data[i]['Ubuntu Configuration']
    master_format['Ubuntu IP Geolocation'] = data[i]['Ubuntu IP Geolocation']
    master_format['Ubuntu Browser Geolocation'] = data[i]['Ubuntu Browser Geolocation']
    master_format['Ubuntu DNS Status'] = data[i]['Ubuntu DNS Status']
    master_format['Ubuntu VPN_Proxy Detection'] = data[i]['Ubuntu VPN_Proxy Detection']
    master_format['Ubuntu IP Ownership'] = data[i]['Ubuntu IP Ownership']
    master_format['Ubuntu Notes'] = data[i]['Ubuntu Notes']
    master_format['Android Operating System'] = data[i]['Android Operating System']
    master_format['Android Evaluation Date'] = data[i]['Android Evaluation Date']
    master_format['Android Configuration'] = data[i]['Android Configuration']
    master_format['Android IP Geolocation'] = data[i]['Android IP Geolocation']
    master_format['Android Browser Geolocation'] = data[i]['Android Browser Geolocation']
    master_format['Android DNS Status'] = data[i]['Android DNS Status']
    master_format['Android VPN_Proxy Detection'] = data[i]['Android VPN_Proxy Detection']
    master_format['Android IP Ownership'] = data[i]['Android IP Ownership']
    master_format['Android Notes'] = data[i]['Android Notes']
    master_format['iOS Operating System'] = data[i]['iOS Operating System']
    master_format['iOS Evaluation Date'] = data[i]['iOS Evaluation Date']
    master_format['iOS Configuration'] = data[i]['iOS Configuration']
    master_format['iOS IP Geolocation'] = data[i]['iOS IP Geolocation']
    master_format['iOS Browser Geolocation'] = data[i]['iOS Browser Geolocation']
    master_format['iOS DNS Status'] = data[i]['iOS DNS Status']
    master_format['iOS VPN_Proxy Detection'] = data[i]['iOS VPN_Proxy Detection']
    master_format['iOS IP Ownership'] = data[i]['iOS IP Ownership']
    master_format['iOS Notes'] = data[i]['iOS Notes']

    json_object = json.dumps(master_format, indent=2)
    filename = data[i]['VPN'] + "_data.json"
    # write properly formatted json to data.json
    with open(filename, "w", encoding='utf-8') as outfile:
        outfile.write(json_object)
