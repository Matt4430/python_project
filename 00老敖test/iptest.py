

import urllib
import requests

def myip_wan():
    url = 'https://www.ip138.com' # 'https://whatismyipaddress.com/' # http://bot.whatismyipaddress.com
    ip  = None
    with urllib.request.urlopen(url) as fp:
        ip = fp.read()
        print('00000000',ip)
        if isinstance(ip, bytes):
            ip = ip.decode('utf-8')
            print('1111111111',ip)
    return ip

if __name__ == '__main__':
    myip_wan()