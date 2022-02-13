import requests
from lxml import etree
import random
import re
from bs4 import BeautifulSoup


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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    # 代理ip
    ip = ip_proxy()
    ipp = {
        'https': 'http://' + ip[random.randint(0, 1)]
    }
    print(ipp)
    """
    针对 《震惊！我修仙秘密被孙女直播曝光》小说脚本
    :return:
    """

    # 小说网页地址
    url = 'http://www.ywggzy.com/bxwx/28463/4083918.html'
    # 开始请求
    req = requests.get(url, proxies=ipp, headers=headers)
    req.encoding = 'utf-8'
    # 拿到网页内容
    html = req.text

    # 用BeautifulSoup解析网页
    soup = BeautifulSoup(html, "html.parser")

    # 写入txt文本
    with open('./老敖小说000.txt', 'a', encoding='utf-8') as fp:
        # 连载562章
        try:
            for i in range(10000):
                # 查找小说主体内容
                content = soup.find('div', id="content")

                # 章节查看
                name = soup.find('h1', class_="title").text

                # 拿到主体内容 转型成字符串  清洗内容
                ct = str(content).replace('\n', '').replace('<br/>　　<br/>　　', '\n').replace(
                    '<div class="posterror"><a class="red" href="javascript:postError();">章节错误,点此举报(免注册)</a>,'
                    '举报后维护人员会在两分钟内校正章节内容,请耐心等待,并刷新页面。</div>', '').replace('<br/>', '').replace('<div class="content" '
                                                                                               'id="content">',
                                                                                               '').replace(
                    '</div>', '').replace('                        ', '').replace('　　　　', '').replace('(本章完)', '\n')

                # 输出清洗好的内容到控制台
                print('ct=========', ct)
                print('\n章节：', name)

                # 写入输出的内容
                fp.write(ct)

                # 用xpath解析网页  获取下一页url
                con = etree.HTML(html)
                urls = con.xpath('//*[@id="container"]/div/div/div[2]/div[4]/a[3]/@href')[0]
                ping = 'http://www.ywggzy.com/bxwx/28463/'

                # 下一页url拼接
                urll = ping + urls

                # 输出url测试
                print('222222222222', urll)
                print('ip_list：',ip)
                print('ip_dict：',ipp)

                # 继续请求下一页
                req = requests.get(urll, proxies=ipp, headers=headers)
                req.encoding = 'utf-8'
                html = req.text
                soup = BeautifulSoup(html, "html.parser")
        except:

            # 因为上面翻页无具体规则   所以循环次数填得略多  爬取完成后会继续循环 导致出错  在此抛出异常
            print('已爬取完毕！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')

if __name__ == '__main__':
    ip_data()