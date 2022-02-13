import requests
from lxml import etree


def test():
    fp = open('./ip存储池.txt','r',encoding='utf-8')
    list_txt = fp.readlines()
    url = 'https://tool.lu/ip/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    }
    a = 0
    with open('./清洗后ip.txt','a',encoding='utf-8')as f:
        for i in list_txt:
            try:
                print(i,'000000000000')
                req = requests.get(url=url, headers=headers, proxies={"https": "http://" + str(i)}, timeout=5)
                print('状态码：',req.status_code)
                # 解析测试网页内容
                # print(req.text)
                content = etree.HTML(req.text)
                # con = content.xpath('/html/body/pre/text()')
                # print('代理ip：',i, '解析后  测试网页内容 :',con)
                # 测试代理ip是否能用
                data = content.xpath('//*[@id="main_form"]/p[1]/text()')

                print(data)
                f.write(i + '\n')
                print('已重新写入......')
                a += 1
            except:
                pass
    print(a,' 个ip可用')



if __name__ == '__main__':
    test()

