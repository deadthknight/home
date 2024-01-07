# ！usr/bin/env Python3.11
# -*-coding:utf-8 -*-
from Day9 import device_ssh
import re
import hashlib
import time


def get_device_config(ip, username='admin', password='cisco', cmd='show running-config'):
    try:
        result = device_ssh(ip, username, password, cmd=cmd)
        return re.search(r'hostname[\s\S]*?\nend', result).group()
    except Exception as error:
        return error


def configure_changed(ip, username, password):
    original_md5 = ''
    while True:
        try:
            md5 = hashlib.md5()
            original_config = get_device_config(ip, username, password)
            md5.update(original_config.encode())
            current_md5 = md5.hexdigest()
            print(current_md5)
            if original_md5 == '':
                original_md5 = current_md5
            elif original_md5 != current_md5:
                print(current_md5)
                print("MD5 value changed")
                break
            time.sleep(5)
        except Exception as error:
            return error



if __name__ == "__main__":
    # print(get_device_config('10.10.1.1', username='admin', password='cisco'))
    print(configure_changed('10.10.1.1', username='admin', password='cisco'))
