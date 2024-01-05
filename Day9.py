import paramiko
import re


def device_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, port=port)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()



def ssh_get_gateway(ip, username, password, cmd='route -n'):
    result = device_ssh(ip, username, password, cmd=cmd)
    pattern = re.compile(r'(?:\d+\.){3}\d+\s+((?:\d+\.){3}\d+)\s+(?:\d+\.){3}\d+\s+(\w+)')
    for line in result.strip().split('\n')[2:]:
        result1 = re.match(pattern, line).groups()
        if result1:                                               #如果匹配上了，在进行下一步
            if result1[1] == 'UG':
                return result1[0]


if __name__ == '__main__':
    print(device_ssh('192.168.85.128', 'root', 'root'))
    print(device_ssh('192.168.85.128', 'root', 'root',cmd='pwd'))
    print('网关为：')
    print(ssh_get_gateway('192.168.85.128', 'root', 'root'))
