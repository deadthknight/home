
# =============================DAY One===================================================
# 随机ip地址
# import random
# for i in range (1, 6):
#     section1 = random.randint(0, 255)
#     section2 = random.randint(0, 255)
#     section3 = random.randint(0, 255)
#     section4 = random.randint(0, 255)
#     random_ip = str(section1)+'.'+str(section2)+'.'+str(section3)+'.'+str(section4)
#     print(random_ip)
# =============================DAY One===================================================

# str_section1 = 'hello the world'
# print(str_section1.split('l'))
# lis1 = [1, 3, 4, 5, 6, 7]
# for i in enumerate(lis1):
#     print(i)
# print(type(i))
# ls1 = [i for i in enumerate(lis1)]
# print(ls1)
# ls1.append('none')
# print(ls1)

# str1 = "QYTANG'day"
# str2 = "2014-9-28"
# print(str1+' '+str2)

# =============================DAY Two===================================================
# word = 'scallywag'
# sub_word = word [2:6]
# print(sub_word)

# str = input('请输入一个单词:')
# str_trans = str[1:] + '-' + str[0] + 'y'
# print(str_trans)

# str1 = 'Port-channel1.189     192.168.189.254  YES  CONFIG  up'
# import re
# str2 = re.match(r'((\S+\d\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#                 r'\s+\w+\s+\w+\s+(\w+))', str1).groups()
# print(f'{"接口":<10}:{str2[1]}\n'
#       f'{"IP地址":<10}:{str2[2]}\n'
#       f'{"状态":<10}:{str2[3]}')
# =============================DAY3=========================================

# str_mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
# import re
# str_mac_re = re.match(r'(\d+)\s+(\S+)\s+(\S+)\s+(\S+)', str_mac).groups()
# print(f'{"VLAN ID":10s}:{str_mac_re[0]}\n'
#       f'{"MAC":10s}:{str_mac_re[1]}\n'
#       f'{"Type":10s}:{str_mac_re[2]}\n'
#       f'{"Interface":10s}:{str_mac_re[3]}')


# print('{:15s}:{}\n'.format("VLAN ID", str_mac_re[0]),
#       '{:15s}:{}\n'.format("MAC", str_mac_re[1]),
#       '{:15s}:{}\n'.format("Type", str_mac_re[2]),
#       '{:15s}:{}\n'.format("Interface", str_mac_re[3]), sep='')
# print("%-10s:%s\n" % ("VLAN ID", str_mac_re[0]),
#       "%-10s:%s\n" % ("MAC", str_mac_re[1]),
#       "%-10s:%s\n" % ("Type", str_mac_re[2]),
#       "%-10s:%s"% ("Interface", str_mac_re[3]), sep='')

# =============================DAY Three===================================================
# show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# import re
# show_conn_re = re.match(r'(\S+)\s+server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+localserver\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)'
#                         r',\s+idle\s+(\d+):(\d+):(\d+),\s+bytes\s+(\d+),\s+flags\s+(\w+)', show_conn).groups()
# print(show_conn_re)
# print(f'{"protocol":15s}:{show_conn_re[0]}\n'
#       f'{"server":15s}:{show_conn_re[1]}\n'
#       f'{"localserver":15s}:{show_conn_re[2]}\n'
#       f'{"idle":15s}:{show_conn_re[3]} 小时 {show_conn_re[4]}分钟 {show_conn_re[5]}秒\n'
#       f'{"bytes":15s}:{show_conn_re[6]}\n'
#       f'{"flags":15s}:{show_conn_re[7]}')
#===========================================================================

# import os
# import re
# ifconfig_result = os.popen('ifconfig ' + 'ens160').read()
# print(ifconfig_result)
# ipv4_add = re.findall(r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# netmask = re.findall(r'netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# broadcast = re.findall(r'broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# mac_addr = re.findall(r'ether\s+((?:[0-9a-f]{2}:){5}[0-9a-f]{2})', ifconfig_result)[0]
# format_string = '{:10s}:{}'
# print(format_string.format('ipv4_add', ipv4_add))
# print(format_string.format('netmask', netmask))
# print(format_string.format('broadcast', broadcast))
# print(format_string.format('mac_addr', mac_addr))
# pattern = re.match(r'(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)', ipv4_add).groups()
# ipv4_gw = pattern[0]+pattern[1]+pattern[2]+'254'
# print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为' + ipv4_gw + '\n')
# ping_result = os.popen('ping ' + str(ipv4_gw) + ' -c 1').read()
# re_ping_result = re.findall(r'[0]\sreceived', ping_result)
# if re_ping_result:
#     print('网关不可达')
# else:
#     print('网关可达')
#=============================================================================================