import requests
from lxml import etree
import random
import re


# 00ip代理
def ip_proxy():
    # 代理商提供的api
    url = "http://proxy.httpdaili.com/apinew.asp?ddbh=1454554059906534893"
    r = requests.get(url)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    print("当前代理ip地有：", ips)
    # proxy = {'http': ips[0]}
    # print("当前代理ip地址为：",proxy)

    return ips


def ip_data():
    for i in range(999):
        url = 'https://tool.lu/ip/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }
        # 代理ip
        ip = ip_proxy()
        ipp = {
            'https': 'http://' + ip[random.randint(0, 1)]
        }
        print(ipp)

        req = requests.get(url, headers=headers, proxies=ipp, timeout=10)

        # 输出状态码
        print(req)

        html_ip = etree.HTML(req.text)

        # 测试代理ip是否能用
        data = html_ip.xpath('//*[@id="main_form"]/p[1]/text()')
        print(data)


if __name__ == '__main__':
    ip_data()
