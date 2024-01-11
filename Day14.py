# ！usr/bin/env Python3.11
# -*-coding:utf-8 -*-
import paramiko


def device_ssh(ip, username, password, port=22, cmd='ls'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, port=port)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.read().decode()
    except Exception as error:
        return f'Error:{error}'


if __name__ == "__main__":
    from argparse import ArgumentParser

    usage = "usage: python Simple_SSH_Client -i ipaddr -u username -p password -c command"
    parser = ArgumentParser(usage=usage)

    parser.add_argument('-i', '--ipaddr', dest='IPADDR', help='SSH Server', type=str)
    parser.add_argument('-u', '--username', dest='USERNAME', help='SSH Username', type=str, default='root')
    parser.add_argument('-p', '--password', dest='PASSWORD', help='SSH Password', type=str, default='root')
    parser.add_argument('-c', '--command', dest='COMMAND', help='Shell Command', type=str, default='ls')

    args = parser.parse_args()

    device_ssh(args.IPADDR, args.USERNAME, args.PASSWORD, port=22, cmd=args.COMMAND)

    # ip = args.IPADDR
    # username = args.USERNAME
    # password = args.PASSWORD
    # command = args.COMMAND

    result = device_ssh(args.IPADDR, args.USERNAME, args.PASSWORD, port=22, cmd=args.COMMAND)
    print(result)
