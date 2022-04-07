from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import re
import time
import random
import os
import csv
import requests
from datetime import datetime


# Buster: Captcha Solver for Humans

def valid_date(timestr):
    nowTime_str = datetime.now().strftime('%Y-%m-%d')
    # mktime参数为struc_time,将日期转化为秒，
    e_time = time.mktime(time.strptime(nowTime_str, "%Y-%m-%d"))
    # print(e_time)
    try:
        s_time = time.mktime(time.strptime(timestr, '%Y-%m-%d'))
        # print(s_time)
        # 日期转化为int比较
        diff = int(s_time) - int(e_time)
        # print(diff)
        if diff >= 0:
            is_true = True
            # print('True')
            return is_true
        else:
            is_true = False
            # self.show_data.emit('测试版本已不能试用！！！')
            # print('测试版本已不能试用！！！')
            print('False')
            return is_true
    except Exception as e:
        print(e)
        return 0


# 请求方法
def get(driver):
    url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/p/a')
    url.click()
    # 新窗口句柄
    h = driver.window_handles
    print(h)
    # driver切换至最新生产的页面
    # driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.window(h[-1])
    time.sleep(1)
    # driver.implicitly_wait(10)
    url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/p/a')
    url.click()
    # 新窗口句柄
    h = driver.window_handles
    # driver切换至最新生产的页面
    driver.switch_to.window(h[-1])
    time.sleep(1)

    # driver.implicitly_wait(10)
    url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/p/a')
    url.click()
    # 新窗口句柄
    h = driver.window_handles
    # driver切换至最新生产的页面
    driver.switch_to.window(h[-1])
    time.sleep(1)

    # driver.implicitly_wait(10)
    url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/p/a')
    url.click()
    # 新窗口句柄
    h = driver.window_handles
    # driver切换至最新生产的页面
    driver.switch_to.window(h[-1])
    content(driver)




def content(driver):
    data = './A小说.txt'
    with open(data, "a", encoding='utf-8') as f:
        print("A小说.txt" + "   文件已创建...")
        title = driver.find_elements_by_css_selector('body > div.container-fluid > div.row > div:nth-child(2) > h1')
        print('title',title)







def verify(response):
    url = "https://www.ispfsb.com/Reg/signup.aspx"
    data = {"g-recaptcha-response": response}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.text


def create_task():
    url = 'http://api.recaptcha.press/task/create?siteKey=6LdAHv8UAAAAAC-KuK02qHMG7nLPZ3WpxZs7eG6K&siteReferer=https://www.ispfsb.com/&authorization=0a389ac1-ab1a-4d60-a089-1f182bd12461'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print('response data:', data)
            return data.get('data', {}).get('taskId')
    except requests.RequestException as e:
        print('create task failed', e)


def polling_task(task_id):
    url2 = 'https://api.recaptcha.press/task/status?taskId=%s' % task_id
    count = 0
    while count < 60:
        try:
            response = requests.get(url2)
            if response.status_code == 200:
                data = response.json()
                print('polling result', data)
                status = data.get('data', {}).get('status')
                print('status of task', status)
                if status == 'Success':
                    return data.get('data', {}).get('response')
        except requests.RequestException as e:
            print('polling task failed', e)
        finally:
            count += 1
            time.sleep(3)


def csv_read():
    data = './sss.csv'
    csv_data = csv.reader(open(data, 'r'))
    for i in csv_data:
        print(i[1])
    print(csv_data)
    print(type(csv_data))


# 程序入口
if __name__ == '__main__':
    # 标识 当前目录
    path = os.getcwd()
    url = "https://yazhouse8.com/article.php?cate=3"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 浏览器扩展程序
    # 语音识别程序
    # extension_path1 = './1.2.2_0.crx'
    # xpath程序
    extension_path2 = './2.0.2_0.crx'
    # options.add_extension(extension_path1)
    options.add_extension(extension_path2)
    driver = webdriver.Chrome(options=options)  # driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?
    driver.maximize_window()
    driver.get(url)

    get(driver)
