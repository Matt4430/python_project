import re
import requests

# 00ip代理
def ip_proxy():
    # 代理商提供的api
    url = "http://proxy.httpdaili.com/apinew.asp?ddbh=1487181651686534893"
    r = requests.get(url)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    print(ips)
    proxy = {'http': ips[0]}
    print("当前代理ip地址为：",proxy)

    return proxy

if __name__ == '__main__':
    ip_proxy()