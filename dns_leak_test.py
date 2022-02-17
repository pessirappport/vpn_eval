'''get ip information from dnsleaktest.com'''
import socket
import sys
from uuid import uuid4
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from json import loads, dumps

def dns_req(uuid, server, port):
    ''' Accepts a 36-character uuid, DNS server and port through which to lookup {uuid}.test.dnsleaktest.com'''
    req = b'\x42\x42\x01\x10\x00\x01\x00\x00\x00\x00\x00\x00\x24' + uuid.encode("utf-8") + b'\x04test\x0bdnsleaktest\x03com\x00\x00\x01\x00\x01'
    try:
        try:
            skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            skt.sendto(req, (server, port))
        except socket.gaierror:
            skt = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            skt.sendto(req, (server, port))
        skt.settimeout(5)
        skt.recv(512)
    except (socket.timeout, socket.error) as error:
        sys.exit("Error connecting to DNS server: " + str(error))

def get_dns_test_leak_data():
    '''get dnsleaktest.com data'''

    '''Taken from: https://gist.github.com/Tugzrida/6fe83682157ead89875a76d065874973
    Author: Tugzrida(https://gist.github.com/Tugzrida)
    dnsleaktest v0.7 python CLI'''
    version = "0.7"
    test_ids = []
    server = None
    extended = False
    port = 53
    json = False
    # Begin the tests
    for _ in range(36 if extended else 6):
        test_ids.append(str(uuid4()))
    try:
        urlopen(Request("https://www.dnsleaktest.com/api/v1/identifiers", headers={"User-Agent": "dnsleaktestcli/{} (https://gist.github.com/Tugzrida)".format(version), "Content-Type": "application/json;charset=UTF-8"}), dumps({"identifiers": test_ids}).encode("utf-8"), timeout=5)
    except HTTPError:
        pass # Endpoint always returns 400 Bad Request
    except URLError:
        sys.exit("Unable to reach dnsleaktest.com!")
    for test_count in range(36 if extended else 6):
        if server:
            dns_req(test_ids[test_count], server, port)
        else:
            socket.gethostbyname("{}.test.dnsleaktest.com".format(test_ids[test_count]))
        sys.stdout.flush()
    # Get the results
    res = loads(urlopen(Request("https://www.dnsleaktest.com/api/v1/servers-for-result", headers={"User-Agent": "dnsleaktestcli/{} (https://gist.github.com/Tugzrida)".format(version), "Content-Type": "application/json;charset=UTF-8"}), dumps({"queries": test_ids}).encode("utf-8"), timeout=5).read().decode("utf-8"))
    server_list = []
    if json:
        print(dumps(res))
    else:
        max_ip_len = max(len(x["ip_address"]) for x in res)
        if max_ip_len == 0:
            sys.exit('  No recursors found!')
        for server in res:
            server_info = {'ip': server['ip_address'], 'hostname':server['hostname'], 'isp':server['isp'], 'country': server['country']}
            if server_info not in server_list:
                server_list.append(server_info)
    return server_list
