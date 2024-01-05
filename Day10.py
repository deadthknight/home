from Day8 import device_ping
from Day9 import device_ssh

import re
from pprint import pprint
def get_route_interface_infor(*ips, username='admin', password='cisco'):
    device_int_infor_result = {}
    for ip in ips:
        device_int_infor = {}
        if device_ping(ip):
            interface_infor = device_ssh(ip, username=username, password=password,cmd='show ip interface brief')
            for line in interface_infor.strip().split('\n')[1:]:
                if_con = re.match(r'(\S+)\s+((?:(?:\d+\.){3}\d+)|\S+)',line).groups()
                device_int_infor[if_con[0]] = if_con[1]
        device_int_infor_result[ip] = device_int_infor
    return device_int_infor_result


if __name__ == "__main__":
    pprint(get_route_interface_infor("10.10.1.1","10.10.1.2","10.10.1.9",
                                     username='admin',password='cisco'))
