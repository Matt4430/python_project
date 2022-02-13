from selenium import webdriver
import time
import random
import fake_useragent
import json
from lxml import etree
import csv

#登录

def login():
    #登录访问url
    driver.get('https://www.lagou.com/')
    # 首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()

    with open('cookies.txt', 'r') as cookief:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookieslist = json.load(cookief)
        # print(cookieslist)
        for cookie in cookieslist:
            # print(cookie)
            if 'sameSite' in cookie:
                del cookie['sameSite']
            driver.add_cookie(cookie)
    driver.refresh()

def search_product(keyword):
    # 设置窗口最大化
    driver.maximize_window()
    driver.implicitly_wait(20)
    # time.sleep(random.randint(3, 5))

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")


    driver.find_element_by_xpath('//*[@id="password_remind"]/div[4]').click()
    driver.find_element_by_xpath('//*[@id="lg_tbar"]/div[1]/div[2]/ul/li[2]/div/i').click()
    driver.find_element_by_xpath('//*[@id="search_input"]').send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="search_button"]').click()
    driver.implicitly_wait(20)


    weiye = driver.find_element_by_xpath('//*[@id="jobList"]/div[3]/ul/li[8]/a').text
    print('该职位  一共： ',weiye," 页！！")
    with open('./{}职位详情.csv'.format(keyword),'a',encoding='utf-8')as fp:
        fieldnames = ["职位名称", "发布时间", "薪资待遇", "学历要求", "公司名称", "公司现状"]
        f_csv = csv.DictWriter(fp, fieldnames=fieldnames)
        f_csv.writeheader()
        #模拟点击下一页
        a = 0
        for i in range(int(weiye)):
            a += 1
            # 点击下一页
            driver.find_element_by_link_text('下一页').click()
            driver.implicitly_wait(20)
            # 等待
            time.sleep(2)
            # 拉动滚动条
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 下拉滚动条
            # 获取数据
            get_data(a,f_csv)
            # 随机等待
            # time.sleep(random.randint(3, 5))
            driver.implicitly_wait(20)

def get_data(b,f_csv):
    time.sleep(2)

    # xpath 提取数据
    text = driver.page_source
    content = etree.HTML(text)
    # print(content)
    # 职位

    for i in range(1,16):
        # 职位名称：
        zhiwei = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[1]/div[1]/a/text()')[0]
        # 发布时间：
        fabushijian = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[1]/div[1]/span/text()')[0]
        # 薪资待遇：
        xinzidaiyu = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[1]/div[2]/span/text()')[0]
        # 学历要求：
        xueliyaoqiu = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[1]/div[2]/text()')[0]
        # 公司名称：
        gongsi = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[2]/div[1]/a/text()')[0]
        # 公司现状:
        gognsixianzhuang = content.xpath('//*[@id="jobList"]/div[1]/div['+str(i)+']/div[1]/div[2]/div[2]/text()')[0]
        print('*'*10,'第 {} 页，第 {} 个职位详情！！！'.format(b,i),'*'*10)
        print('职位名称：',zhiwei)
        print('发布时间：', fabushijian)
        print('薪资待遇：', xinzidaiyu)
        print('学历要求：', xueliyaoqiu)
        print('公司名称：', gongsi)
        print('公司现状:', gognsixianzhuang)
        f_csv.writerow(
            {
                '职位名称': zhiwei,
                '发布时间': fabushijian,
                '薪资待遇': xinzidaiyu,
                '学历要求': xueliyaoqiu,
                '公司名称': gongsi,
                '公司现状': gognsixianzhuang
            }
        )

if __name__ == '__main__':
    keyword = input('请输入你要爬取的岗位名称:')

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

    login()
    search_product(keyword)