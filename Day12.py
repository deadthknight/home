# ！usr/bin/env Python3.11
# -*-coding:utf-8 -*-
import paramiko
import time


def device_multicmd(ip, username, password, cmd, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()  # 创建SSH client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥

    try:
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接
        chan = ssh.invoke_shell()
        time.sleep(1)
        output =chan.recv(2048).decode()
        print(output)
        if '>' in output:
            chan.send('enable'.encode()+b'\n')
            chan.send('test'.encode()+b'\n')

        for cmd in cmd_list:
            chan.send(cmd.encode()+b'\n')
            time.sleep(wait_time)
            x = chan.recv(2048).decode()
            print(x)

    except Exception as error:
        return error


if __name__ == "__main__":
    cmd_list = ['terminal length 0','show version', 'config terminal', 'router os 1', 'network 10.10.1.0 255.255.255.0 a 0']
    device_multicmd('10.10.1.1', username='test', password='test', cmd=cmd_list)
