dns_leak_data = [
    {'ip': '146.70.8.130', 'hostname': 'BEzeq', 'isp': 'M247 Ltd'}, 
    {'ip': '146.146.8.130', 'hostname': 'HEllo', 'isp': 'Cloudlfare Ltd'}, 
    {'ip': '146.70.146.130', 'hostname': 'Me', 'isp': 'Total server oslutions Ltd'}
]

for i in (dns_leak_data):
    print(i['ip'])