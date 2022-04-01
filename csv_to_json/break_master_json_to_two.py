import json

with open('./vpn_data_jsons/Hotspot Shield_data.json', 'r', encoding='utf-8') as f:
    data = f.read()
data = json.loads(data)

windows_evaluation_data = {
    "VPN": "",
    "Operating System": "",
    "Status": "Not Started",
    "Evaluation Date": "",
    "Configuration": "",
    "IP Geolocation": "",
    "Browser Geolocation": "",
    "DNS Status": "",
    "VPN_Proxy Detection": "",
    "IP Ownership": "",
    "Notes": ""
}
iOS_evaluation_data = {
    "VPN": "",
    "Operating System": "",
    "Status": "Not Started",
    "Evaluation Date": "",
    "Configuration": "",
    "IP Geolocation": "",
    "Browser Geolocation": "",
    "DNS Status": "",
    "VPN_Proxy Detection": "",
    "IP Ownership": "",
    "Notes": ""
}
ubuntu_evaluation_data = {
    "VPN": "",
    "Operating System": "",
    "Status": "Not Started",
    "Evaluation Date": "",
    "Configuration": "",
    "IP Geolocation": "",
    "Browser Geolocation": "",
    "DNS Status": "",
    "VPN_Proxy Detection": "",

    "IP Ownership": "",
    "Notes": ""
}
android_evaluation_data = {
    "VPN": "",
    "Operating System": "",
    "Status": "Not Started",
    "Evaluation Date": "",
    "Configuration": "",
    "IP Geolocation": "",
    "Browser Geolocation": "",
    "DNS Status": "",
    "VPN_Proxy Detection": "",

    "IP Ownership": "",
    "Notes": ""
}

background_data = {
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
}

background_data['VPN'] = data['VPN']
background_data['Progress'] = "Completed"
background_data['Background Date'] = data['Background Date']
background_data['Evaluation Summary'] = data['Evaluation Summary']
background_data['URL'] = data['URL']
background_data['Pricing'] = data['Pricing']
background_data['Payment Information'] = data['Payment Information']
background_data['Extra Options'] = data['Extra Options']
background_data['Trial Information'] = data['Trial Information']
background_data['Account Creation Information'] = data['Account Creation Information']
background_data['Supported OS'] = data['Supported OS']
background_data['OS Applications'] = data['OS Applications']
background_data['Browser Extensions'] = data['Browser Extensions']
background_data['Other Devices'] = data['Other Devices']
background_data['Number of Devices']['Connections'] = data['Number of Devices']['Connections']
background_data['Encryption'] = data['Encryption']
background_data['2FA'] = data['2FA']
background_data['AdBlock'] = data['AdBlock']
background_data['Supported Protocols'] = data['Supported Protocols']
background_data['Multi-Hop'] = data['Multi-Hop']
background_data['P2P'] = data['P2P']
background_data['Static IP'] = data['Static IP']
background_data['Killswitch'] = data['Killswitch']
background_data['Server Locations'] = data['Server Locations']
background_data['Data Collection Policy'] = data['Data Collection Policy']
background_data['Data Retained'] = data['Data Retained']
background_data['Advertising Data'] = data['Advertising Data']
background_data['Payment Data'] = data['Payment Data']
background_data['Data Retention Timeline'] = data['Data Retention Timeline']
background_data['Ownership'] = data['Ownership']
background_data['Corporate HQ'] = data['Corporate HQ']
background_data['Country of Governance'] = data['Country of Governance']
background_data['Notes'] = data['Notes']
background_data['Recent News'] = data['Recent News']
background_data['Reported Malware']['Malicious Intent'] = data['Reported Malware']['Malicious Intent']
windows_evaluation_data["VPN"] = data['VPN']
windows_evaluation_data["Status"] = 'Complete'
windows_evaluation_data["Operating System"] = data['Windows Operating System']
windows_evaluation_data["Evaluation Date"] = data['Windows Evaluation Date']
windows_evaluation_data["Configuration"] = data['Windows Configuration']
windows_evaluation_data["IP Geolocation"] = data['Windows IP Geolocation']
windows_evaluation_data["Browser Geolocation"] = data['Windows Browser Geolocation']
windows_evaluation_data["DNS Status"] = data['Windows DNS Status']
windows_evaluation_data["VPN_Proxy Detection"] = data['Windows VPN_Proxy Detection']
windows_evaluation_data["IP Ownership"] = data['Windows IP Ownership']
windows_evaluation_data["Notes"] = data['Windows Notes']
iOS_evaluation_data["VPN"] = data['VPN']
iOS_evaluation_data["Status"] = 'Complete'
iOS_evaluation_data["Operating System"] = data['iOS Operating System']
iOS_evaluation_data["Evaluation Date"] = data['iOS Evaluation Date']
iOS_evaluation_data["Configuration"] = data['iOS Configuration']
iOS_evaluation_data["IP Geolocation"] = data['iOS IP Geolocation']
iOS_evaluation_data["Browser Geolocation"] = data['iOS Browser Geolocation']
iOS_evaluation_data["DNS Status"] = data['iOS DNS Status']
iOS_evaluation_data["VPN_Proxy Detection"] = data['iOS VPN_Proxy Detection']
iOS_evaluation_data["IP Ownership"] = data['iOS IP Ownership']
iOS_evaluation_data["Notes"] = data['iOS Notes']
android_evaluation_data["VPN"] = data['VPN']
android_evaluation_data["Status"] = 'Complete'
android_evaluation_data["Operating System"] = data['Android Operating System']
android_evaluation_data["Evaluation Date"] = data['Android Evaluation Date']
android_evaluation_data["Configuration"] = data['Android Configuration']
android_evaluation_data["IP Geolocation"] = data['Android IP Geolocation']
android_evaluation_data["Browser Geolocation"] = data['Android Browser Geolocation']
android_evaluation_data["DNS Status"] = data['Android DNS Status']
android_evaluation_data["VPN_Proxy Detection"] = data['Android VPN_Proxy Detection']
android_evaluation_data["IP Ownership"] = data['Android IP Ownership']
android_evaluation_data["Notes"] = data['Android Notes']
ubuntu_evaluation_data["VPN"] = data['VPN']
ubuntu_evaluation_data["Status"] = 'Complete'
ubuntu_evaluation_data["Operating System"] = data['Ubuntu Operating System']
ubuntu_evaluation_data["Evaluation Date"] = data['Ubuntu Evaluation Date']
ubuntu_evaluation_data["Configuration"] = data['Ubuntu Configuration']
ubuntu_evaluation_data["IP Geolocation"] = data['Ubuntu IP Geolocation']
ubuntu_evaluation_data["Browser Geolocation"] = data['Ubuntu Browser Geolocation']
ubuntu_evaluation_data["DNS Status"] = data['Ubuntu DNS Status']
ubuntu_evaluation_data["VPN_Proxy Detection"] = data['Ubuntu VPN_Proxy Detection']
ubuntu_evaluation_data["IP Ownership"] = data['Ubuntu IP Ownership']
ubuntu_evaluation_data["Notes"] = data['Ubuntu Notes']

broken_down_data_compiled = [
    background_data,
    windows_evaluation_data,
    ubuntu_evaluation_data,
    iOS_evaluation_data,
    android_evaluation_data
]

filename = './separated_vpn_jsons/' + \
    data['VPN']+"_broken_and_compiled_data.json"

broken_down_data_compiled_json = json.dumps(broken_down_data_compiled)
with open(filename, "w", encoding='utf-8-sig') as outfile:
    json.dump(broken_down_data_compiled, outfile, indent=2)
