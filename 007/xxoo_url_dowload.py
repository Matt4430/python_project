from selenium import webdriver
import time
import json


# cookie登陆
def login():
    driver.get('https://www.xvideos.com/?k=jk&top')  # URL
    # 首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()

    with open('xx.txt', 'r') as cookief:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookieslist = json.load(cookief)
        # print(cookieslist)
        for cookie in cookieslist:
            if 'sameSite' in cookie:
                del cookie['sameSite']

            driver.add_cookie(cookie)
        print("已使用cookie登陆......")

    # 刷新当前页面
    driver.refresh()
    driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址


# 视频抓取
def get_video():
    with open('./url.txt','r',encoding='utf-8')as f:
        a = f.readlines()
        print(str(len(a)))
        for i in a:
            print(i)
            try:
                driver.get(i)
                driver.implicitly_wait(300)
                botton = driver.find_element_by_xpath('//*[@id="v-actions"]/div[2]/button[2]')
                botton.click()
                driver.implicitly_wait(300)
                down = driver.find_element_by_xpath('//*[@id="tabDownload"]/div/p/a[1]/strong/span')
                down.click()
                driver.implicitly_wait(300)
            except:
                driver.refresh()
                driver.get(i)
                driver.implicitly_wait(300)
                botton = driver.find_element_by_xpath('//*[@id="v-actions"]/div[2]/button[2]')
                botton.click()
                driver.implicitly_wait(300)
                down = driver.find_element_by_xpath('//*[@id="tabDownload"]/div/p/a[1]/strong/span')
                down.click()
                driver.implicitly_wait(300)

if __name__ == '__main__':
    ye = 0
    # 定义账号密码
    qq_num = '2945711528@qq.com'
    qq_pwd = 'matt00789'
    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    # 浏览器扩展程序
    # 语音识别程序
    extension_path1 = '../1.2.2_0.crx'
    # xpath程序
    extension_path2 = '../2.0.2_0.crx'
    # 将自定义设置添加到chrome配置对象实例中
    options.add_extension(extension_path1)
    options.add_extension(extension_path2)
    # 如果该目录不存在则直接创建
    prefs = {"download.default_directory": r"D:\007\1"}
    # 将自定义设置添加到chrome配置对象实例中
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 拿到浏览器操作手柄
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # 调用程序
    login()
    get_video()
