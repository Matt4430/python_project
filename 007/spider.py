from selenium import webdriver
import time
from lxml import etree
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlretrieve
import requests
import os


# 登陆QQ访问对方QQ空间
def login(login_qq, password):
    '''
    登陆
    :param login_qq: 登陆用的QQ
    :param password: 登陆的QQ密码
    :param business_qq: 业务QQ
    :return: driver
    '''

    driver.get('https://www.xvideos.com/tags/s:views/m:3month/q:hd/hentai')  # URL
    # driver.get('https://www.xvideos.com/tags/s:views/m:3month/q:hd/hentai/1')  # URL
    driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址

    a = input('验证之后输入1：')
    if a == '1':
        pass
    driver.find_element_by_xpath('//*[@id="header-mobile-right"]/a[3]').click()
    driver.find_element_by_id('signin-form_login').click()
    driver.find_element_by_id('signin-form_login').send_keys(login_qq)  # 输入账号

    driver.find_element_by_id('signin-form_password').send_keys(password)  # 输入密码

    driver.find_element_by_xpath('//*[@id="signin-form"]/div[3]/div/div/label').click()  # 记住我
    driver.find_element_by_xpath('//*[@id="signin-form"]/div[4]/div/button').click()  # 点击‘登录’
    a = input('验证之后输入2：')
    if a == '2':
        pass


# 抓取说说 driver.back()  返回上一界面
def get_video(driver):

    for i in range(1,29):
        try:
            driver.find_element_by_xpath('/html/body/div/div[4]/div[4]/div[1]/div[' + str(i) + ']/div[1]/div/a/img[1]').click() # 点击图片进入
            driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
            print('-'*10 + "开始点击下载第 "+ str(i) +" 部 ！" + '-'*10)
            try:
                driver.find_element_by_xpath('//*[@id="video-actions"]/ul/li[2]/a').click()  # 点击下载
                driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
                driver.find_element_by_xpath('//*[@id="tabDownload"]/p/a[1]').click()  # 点击中等
                driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址
                driver.back()  # 返回上一界面
                print("第二行是下载！！！")
                print("第 " + str(i) + " 部视频已下载.......")

            except:
                print('第一行是下载.....')
                driver.find_element_by_xpath('//*[@id="video-actions"]/ul/li[1]/a').click()  # 先点击评论
                driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
                driver.find_element_by_xpath('//*[@id="tabDownload"]/p/a[1]').click()# 点击中等
                driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址
                driver.back()  # 返回上一界面
                print("第 " + str(i) + " 部视频已下载.......")

        except:
            # 获取打开的多个窗口句柄
            windows = driver.window_handles
            # 切换到当前最新打开的窗口
            driver.switch_to.window(windows[0])
            print("遇到广告.........")
            url1 = driver.current_url
            print(url1)
            driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址
            driver.get(url1)
            time.sleep(5)
            driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址

        # driver.find_element_by_xpath('//*[@id="video-actions"]/ul/li[1]/a').click()  # 先点击评论
        # try:
        #     driver.find_element_by_xpath('//*[@id="tabDownload"]/p/a[1]').click()# 点击中等
        #     print("第一行是下载！！！")
        # except:
        #     print('第一行是评论.....')
        #     driver.find_element_by_xpath('//*[@id="video-actions"]/ul/li[2]/a').click()  # 点击下载
        #     driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
        #     driver.find_element_by_xpath('//*[@id="tabDownload"]/p/a[1]').click()  # 点击中等



    driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[20]/a').click() # 点击下一页
    # con+=1
    # print('已进入第 ' + str(con) + '  页.........')
    get_video(driver)

if __name__ == '__main__':
    qq_num = '2945711528@qq.com'
    qq_pwd = 'matt00789'

    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    con = 1

    login(qq_num, qq_pwd)
    get_video(driver)
