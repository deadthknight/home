from kamene.all import *
import logging
from kamene.layers.inet import IP, ICMP
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)

def device_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False


if __name__ == '__main__':
    result = device_ping(input('ip:'))
    print(result)




