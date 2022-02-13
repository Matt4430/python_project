"""
快代理  网站 免费代理ip
https://www.kuaidaili.com/free/inha/1/
"""

import requests
import fake_useragent
from lxml import etree
import random
import time

def test():
    fp = open('./ip存储池.txt','r',encoding='utf-8')
    list_txt = fp.readlines()
    url = 'https://tool.lu/ip/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    }
    with open('./清洗后ip.txt','a',encoding='utf-8')as f:
        for i in list_txt:
            try:
                print(i,'000000000000')
                req = requests.get(url=url, headers=headers, proxies={"https": "http://" + str(i)}, timeout=5)
                print('状态码：',req.status_code)
                # 解析测试网页内容
                # print(req.text)
                content = etree.HTML(req.text)
                # 测试代理ip是否能用
                data = content.xpath('//*[@id="main_form"]/p[1]/text()')
                print(data)
                yield i
            except:
                pass





# ip获取
def ip_get():
    # 目标站
    url = 'https://www.kuaidaili.com/free/inha/'

    # 实例化 user-agent 对象    得到随机user-agent
    ua = fake_useragent.UserAgent()

    # 空列表存储爬取到的代理ip
    list1 = []

    with open('./ip存储池.txt', 'a', encoding='utf-8') as fp:
        for i in range(1, 4398):  # ,4398
            headers = {"User-Agent": ua.random}
            # 拼接完整url
            urls = url + str(i) + "/"
            print(urls)
            time.sleep(1)
            res = requests.get(urls, headers=headers, proxies={"https": "http://" + str(test())})  # , verify=False   ,proxies={"https": "http://" + str(list_txt[random.randint(0,t)])}
            print(res.status_code, '代理ip获取页  请求状态码！！')
            text = res.text
            html = etree.HTML(text)
            for j in range(1, 16):
                ip = html.xpath('//*[@id="list"]/table/tbody/tr[' + str(j) + ']/td[1]/text()')[0]
                prot = html.xpath('//*[@id="list"]/table/tbody/tr[' + str(j) + ']/td[2]/text()')[0]
                protocol = html.xpath('//*[@id="list"]/table/tbody/tr[' + str(j) + ']/td[4]/text()')[0]

                print('免费ip:', ip, '代理端口：', prot, '使用协议：', protocol)
                ip_p = ip + ':' + prot
                list1.append(ip_p)
                fp.write(ip_p + '\n')

    return list1


# 测试是否代理成功
def ip_data():
    # 将爬取的可用ip存储到txt文件
    with open('./ip存储池.txt', 'a+', encoding='utf-8') as fp:

        # 计数器
        a = 0

        # 代理ip
        ip = ip_get()
        for j in ip:
            try:
                url = 'http://icanhazip.com/'
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
                }
                proxies = {
                    "http": "http://" + str(j)
                }

                # 开始使用收集到的ip发起请求  优选5秒内能连接的
                res = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)
                # 响应的状态码
                code = res.status_code
                print(code, '代理后请求   响应码')

                # 判断可用ip
                if code == 200:
                    a += 1
                    print(j, '  此ip可用！！！！')
                    fp.write(j + '\n')
                    print('已写入ip存储池.txt')
                else:
                    print(j, '  此ip不可用........')
                    pass
                    # 解析测试网页内容
                    content = etree.HTML(res.text)
                    con = content.xpath('/html/body/pre/text()')[0]
                    print(con, '解析后  测试网页内容 ！')
            except:
                print(j, '当前代理ip不适用！！')
    print('over.....  收集可用ip {} 个'.format(a))

if __name__ == '__main__':
    # ip_get()
    ip_data()
