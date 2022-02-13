import time
import re
import requests
import fake_useragent
from selenium import webdriver
from lxml.etree import HTML


# 00ip代理
def ip_out():
    url = "http://proxy.httpdaili.com/apinew.asp?sl=3&noinfo=true&text=1&ddbh=1420927609453534893"
    r = requests.get(url)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    # print(ips)
    proxy = {'http': ips[0]}
    print("当前代理ip地址为：", proxy)

    return proxy


# 装饰器 计算时间
def time_out(a_func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = a_func(*args, **kwargs)
        end = time.time()
        print("程序：" + a_func.__name__, "    运行时间：" + str(end - start))
        return result

    return clocked


# 章节详情页 url拼接数字迭代
def add_num(num=17907917):
    for i in range(num, num + 1179):
        yield str(i)


# 开始请求 url地址
@time_out
def page_number(num=add_num(), aa=0):
    for i in num:
        # page_url = url + nu + ".html"
        page_url = driver.current_url
        print(page_url, '   00000000000000000000000000000000000000000000000000')
        driver.implicitly_wait(20)
        content = driver.page_source
        # 章节名字
        title = driver.find_elements_by_xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1')[0].text
        print(title)
        html = HTML(content)
        txt = html.xpath("//div[@id='content']/text()")

        with open("./异界之魔武流氓.txt", "a+", encoding="utf-8") as f:
            f.write('\n')
            f.write('\t' + title + '\n')
            f.write('\n')
            for i in txt:
                ok = str(i)
                print(ok)
                f.write(ok + '\n')

            f.close()
        driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[6]/a[3]').click()
        driver.implicitly_wait(60)

        if title == '第1178章至尊界主（大结局）':
            print("############################  全书已下载完成  ############################ \n" * 5)
        else:
            pass

if __name__ == '__main__':
    # 实例化 user-agent 对象
    ua = fake_useragent.UserAgent()
    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 更换头部
    options.add_argument('user-agent={}'.format(ua.random))
    # 浏览器扩展程序
    # xpath程序
    extension_path2 = '../2.0.2_0.crx'
    options.add_extension(extension_path2)
    driver = webdriver.Chrome(options=options)  # driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?
    # 浏览器窗口最大化
    driver.maximize_window()

    url = 'https://www.biqugee.com/book/35456/17907917.html '
    driver.get(url)

    page_number()
