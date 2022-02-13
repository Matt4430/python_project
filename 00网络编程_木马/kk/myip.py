import urllib.request
import requests
from lxml import etree

def myip_wan():
    url = 'https://tool.lu/ip/' # http://bot.whatismyipaddress.com

    ip  = None
    # with urllib.request.urlopen(url) as fp:
    #     ip  = fp.read()
    #     if isinstance(ip, bytes):
    #         ip = ip.decode('utf-8')
    url = 'https://tool.lu/ip/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }


    req = requests.get(url, headers=headers)

    # 输出状态码
    print(req)

    html_ip = etree.HTML(req.text)

    # 测试代理ip是否能用
    data = html_ip.xpath('//*[@id="main_form"]/p[1]/text()')[0]
    print(data[-13:])

    return data[-13:]

def myip_lan():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 53))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':
    ip = myip_wan()
    print(ip)
    ip = myip_lan()
    print(ip)
