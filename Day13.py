# ！usr/bin/env Python3.11
# -*-coding:utf-8 -*-
import paramiko
from kamene.all import *
class QYTPING:
    def __init__(self,ip):
        self.ip = ip
        self.length = 100
        self.dstip = self.ip
        self.srcip = None
        self.pkt = IP(src=self.srcip, dst=self.ip) / ICMP()

    def one(self):
        ping_result = sr1(self.pkt, timeout=2, verbose=False)
        if ping_result:
            print (f'{self.ip} 可达！')
    def ping(self):
        ping_result = sr1(self.pkt, timeout=2, verbose=False)
        if ping_result:
            print(f'!!!!!')
        elif ping_result is None:
            print(f'+++++.')
    def __str__(self):
        if self.srcip is not None:
            return f'<{self.__class__.__name__} => srcip:{self.srcip},dstip:{self.ip},size:{self.length}>'
        return f'<{self.__class__.__name__} => dstip:{self.ip},size:{self.length}>'






if __name__ == "__main__":
    ping = QYTPING('10.10.1.1')
    total_len= 70
    def print_new(word , s='-'):
        print('{}{}{}'.format((s * int((70-len(word))/2)), word,s* int((70-len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '10.10.10.10'
    print(ping.srcip)
    ping.ping()
    # print_new('new class NewPing', '=')
    # newping = NewPing('10.10.1.200')
    # newping.length = 300
    # print(newping)
    # newping.ping()