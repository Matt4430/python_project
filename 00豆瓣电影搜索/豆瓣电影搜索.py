import requests
from lxml import etree
import fake_useragent
from selenium import webdriver
import re
import time
import csv
import json



# 传入搜索页面中保存的src   url
def jiexi_url(url):

    handers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    req = requests.get(url, headers=handers)
    req.encoding = 'utf-8'
    content = etree.HTML(req.text)

    # 开始解析
    text = req.text

    # 判断是否有评分
    aa = '暂无评分'
    pingfen = content.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/text()')[0]
    leix = re.sub('[^\u4e00-\u9fa5]+', '', str(pingfen))


    if aa != leix:
        # print(text)
        # 正则表达式  需要匹配的格式
        geshi_re = '"@context": "http://schema.org",(.*?)</script>'
        geshi = re.compile(geshi_re,re.S)
        js = re.findall(geshi,text)
        join_list = ['{ \n  "@context":"http://schema.org",']

        # 列表拼接
        jk = join_list + js
        re_sip = str(jk)
        re_1 = re_sip.replace(r'\n','').replace("'', '\n  '",'').replace("',",'').replace("'",'').replace("   ",'').replace("  ",'')

        # 转换为json list
        json_file = json.loads(re_1)
        # print(json_file)
        # 剧名
        juming = json_file[0]['name']
        print('剧名：',juming)

        # 地区
        diqu_re = '<span class="pl">制片国家/地区:</span>(.*?)<span class="pl">语言:</span>'
        diqu_geshi = re.compile(diqu_re, re.S)
        json_str = re.findall(diqu_geshi, text)[0]
        diqu = json_str.replace('<br/>\n','').replace(' ','').replace(r'\n','')
        print('地区：',diqu)

        # 类型
        leixing_re = '<span class="pl">类型:</span>(.*?)<span class="pl">官方网站:</span>'
        leixing_geshi = re.compile(leixing_re, re.S)
        leixs = re.findall(leixing_geshi, text)
        # 如果类型报错  排除
        if '' not in leixs:
            # 类型
            leixing_re = '<span class="pl">类型:</span>(.*?)<span class="pl">制片国家/地区:</span>'
            leixing_geshi = re.compile(leixing_re, re.S)
            leixs = re.findall(leixing_geshi, text)[0]
            leix = re.sub('[^\u4e00-\u9fa5]+', '/', leixs)
            print("类型：", leix)

        # 评分
        pingfen = content.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        print('评分：', pingfen)

        # 多少人评价
        pingjia = content.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0]
        print("多少人评价：", pingjia)

        # 导演
        daoyan = json_file[0]['director'][0]['name']
        print('导演：',daoyan)

        bianju_lists = []
        # 编剧
        bianju_list = json_file[0]['author']
        for i in bianju_list:
            for j,k in i.items():
                if j == 'name':
                    # print(k)
                    bianju_lists.append(k)
        del bianju_lists[-1]
        print('编剧：',bianju_lists)

        # 主演
        zhuyan_lists = []
        zhuyan_list = json_file[0]['actor']
        for i in zhuyan_list:
            for j,k in i.items():
                if j == 'name':
                    # print(k)
                    zhuyan_lists.append(k)
        del zhuyan_lists[-1]
        print('主演：',zhuyan_lists)
    else:
        print("该剧  暂无评分!!")

        # 正则表达式  需要匹配的格式
        geshi_re = '"@context": "http://schema.org",(.*?)</script>'
        geshi = re.compile(geshi_re, re.S)
        js = re.findall(geshi, text)
        join_list = ['{ \n  "@context":"http://schema.org",']

        # 列表拼接
        jk = join_list + js
        re_sip = str(jk)
        re_1 = re_sip.replace(r'\n', '').replace("'', '\n  '", '').replace("',", '').replace("'", '').replace("   ",
                                                                                                              '').replace(
            "  ", '')

        # 转换为json list
        json_file = json.loads(re_1)
        # print(json_file)
        # 剧名
        juming = json_file[0]['name']
        print('剧名：', juming)

        # 地区
        diqu_re = '<span class="pl">制片国家/地区:</span>(.*?)<span class="pl">语言:</span>'
        diqu_geshi = re.compile(diqu_re, re.S)
        json_str = re.findall(diqu_geshi, text)[0]
        diqu = json_str.replace('<br/>\n', '').replace(' ', '').replace(r'\n', '')
        print('地区：', diqu)

        # 类型
        leixing_re = '<span class="pl">类型:</span>(.*?)<span class="pl">官方网站:</span>'
        leixing_geshi = re.compile(leixing_re, re.S)
        leixs = re.findall(leixing_geshi, text)
        # 如果类型报错  排除
        if '' not in leixs:
            # 类型
            leixing_re = '<span class="pl">类型:</span>(.*?)<span class="pl">制片国家/地区:</span>'
            leixing_geshi = re.compile(leixing_re, re.S)
            leixs = re.findall(leixing_geshi, text)[0]
            leix = re.sub('[^\u4e00-\u9fa5]+', '/', leixs)
            print("类型：", leix)

        # 导演
        daoyan = json_file[0]['director'][0]['name']
        print('导演：', daoyan)

        bianju_lists = []
        # 编剧
        bianju_list = json_file[0]['author']
        for i in bianju_list:
            for j, k in i.items():
                if j == 'name':
                    # print(k)
                    bianju_lists.append(k)
        del bianju_lists[-1]
        print('编剧：', bianju_lists)

        # 主演
        zhuyan_lists = []
        zhuyan_list = json_file[0]['actor']
        for i in zhuyan_list:
            for j, k in i.items():
                if j == 'name':
                    # print(k)
                    zhuyan_lists.append(k)
        del zhuyan_lists[-1]
        print('主演：', zhuyan_lists)


def get_url(base_url, url_list):
    while True:
        # 把输入的关键字定义为全局变量
        global keyword
        keyword = input(
            'Please enter the keyword of the movie. If you want to enter multiple keyword,please seperate them with comma:')
        keyword_list = keyword.split(',')  # bug  注意区分中文逗号，& 英文逗号,
        if '' in keyword_list:
            print('This is the wrong input, please try again:')
        else:
            break

    for key in keyword_list:
        url_list.append(base_url.format(key))

def NodeExists(xpath):
   try:
      driver.find_element_by_link_text(xpath)
      return True
   except:
      return False

def req_url(url_list, driver,if_xpath):
    # 调用输入的关键字作为文件名
    keyword
    filename = './' + keyword + '电影搜索结果.csv'

    driver.maximize_window()

    with open(filename, 'a', encoding='utf-8', newline='') as f:
        print(filename, "   文件已创建...")
        fieldnames = ["电影名", "链接"]
        f_csv = csv.DictWriter(f, fieldnames=fieldnames)
        f_csv.writeheader()
        b = 0
        for i in url_list:
            b += 1
            print('第 {} 条url: '.format(b),i)
            driver.get(i)
            driver.implicitly_wait(20)
            time.sleep(2)

            # 注入js代码 滑动浏览器滚动条到底
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            text = driver.page_source
            html = etree.HTML(text)
            # 标识 获取a条数据
            a = 0
            # 异常抛出 若有分页数据则执行 try中代码  若只有一页数据则执行异常代码

            if NodeExists(if_xpath):
                while True:
                    driver.implicitly_wait(10)
                    text = driver.page_source
                    html = etree.HTML(text)
                    content = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]')[0]
                    for j in range(1, 18):
                        try:
                            title = content.xpath('.//div[' + str(j) + ']/div/div/div[1]/a/text()')[0]
                            print('title====', title)
                            src = content.xpath('.//div[' + str(j) + ']/div/div/div[1]/a/@href')[0]
                            print('src  ====', src)
                            a += 1
                            f_csv.writerow(
                                {
                                    '电影名': title,
                                    '链接': src
                                }
                            )
                            jiexi_url(src)
                        except:
                            continue
                    # 点击下一页
                    driver.find_element_by_link_text('后页>').click()
                    driver.implicitly_wait(20)
            else:
                content = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]')[0]
                for j in range(1, 18):
                    try:
                        title = content.xpath('.//div[' + str(j) + ']/div/div/div[1]/a/text()')[0]
                        # title = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a/text()')[0]
                        print('title====', title)
                        src = content.xpath('.//div[' + str(j) + ']/div/div/div[1]/a/@href')[0]
                        # src = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a/@href')[0]
                        print('src  ====', src)
                        a += 1
                        f_csv.writerow(
                            {
                                '电影名': title,
                                '链接': src
                            }
                        )
                        jiexi_url(src)
                    except:
                        continue

    # js = 'document.querySelector("#root > div > div._luoaf7sou > div._zrkqwekox > div:nth-child(1) > div.paginator.sc-htoDjs.eszZtj > a.num.activate.thispage").click()'
    # driver.execute_script(js)


    print('已获取 {} 条数据'.format(a))
    driver.close()
    print("程序结束！！！！！！！！！！！！")

if __name__ == '__main__':
    if_xpath = '后页>'

    # 实例化 user-agent 对象    得到随机user-agent
    ua = fake_useragent.UserAgent()

    # 使用随机ua
    headers = {"user-agent": ua.random}

    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    # 浏览器扩展程序
    # cookie获取程序
    # extension_path1 = './2.1.0.0_0.crx'

    # xpath程序
    extension_path2 = './2.0.2_0.crx'

    # 添加扩展程序到浏览器
    # options.add_extension(extension_path1)
    options.add_extension(extension_path2)

    # 添加随机ua到浏览器
    options.add_argument('user-agent=' + ua.random)
    driver = webdriver.Chrome(options=options)  # driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?

    # 浏览器窗口最大化
    # driver.maximize_window()

    base_url = 'https://search.douban.com/movie/subject_search?search_text={}&cat=1002'
    url_list = []

    # 开始执行函数
    get_url(base_url, url_list)
    req_url(url_list, driver,if_xpath)
