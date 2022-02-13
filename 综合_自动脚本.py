from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from lxml import etree
from bs4 import BeautifulSoup
import re
import time
import random
import os
import pandas as pd
import csv
import numpy as np
import eventlet
# Buster: Captcha Solver for Humans

# 请求方法
def get(driver,url):
    data = './sss.csv'
    csv_data = csv.reader(open(data, 'r'))
    with open("./"+'结果.csv', "a", newline='', encoding='utf-8') as f:
        print("结果" + '.csv' + "   文件已创建...")
        fieldnames = ["名", "中间名", "姓", "地址", "生日", "ssn", "驾照","体重"]
        f_csv = csv.DictWriter(f, fieldnames=fieldnames)
        f_csv.writeheader()
        for i in csv_data:
            for j in range(100,170):
                driver.get(url)
                print("已打开首页")
                driver.implicitly_wait(10)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                # 点击apply  应用
                driver.find_element_by_xpath(
                    '//*[@id="main-content"]/section/section/div/div/div/div[2]/div[1]/section/div/a').click()
                driver.implicitly_wait(10)

                # 点击close
                driver.find_element_by_xpath('//*[@id="divSystemMessage"]/div/div/div[3]/button').click()
                try: # 关掉第二个close
                    driver.find_element_by_xpath('//*[@id="divnote"]/div/div/div[3]/button').click()
                    # ActionChains(driver).move_by_offset(1298, 297).click().perform()  # 鼠标左键点击一律不

                except:
                    pass
                # 点击注册
                driver.find_element_by_xpath('//*[@id="divRegister"]/section/div/div/div/a').click()
                driver.implicitly_wait(10)

                # 点击begin
                driver.find_element_by_xpath('//*[@id="divStep1"]/div[2]/div/span/a').click()
                driver.implicitly_wait(5)

                # 下拉滚动条到底
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)

                # a = input("00000000000000：")

                # 下拉滚动条到底
                driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
                time.sleep(1)

                # 输入第一个last name
                # html = driver.page_source
                # soup = BeautifulSoup(html,'lxml')
                # soup.select('')
                lastname1 = driver.find_element_by_xpath('//*[@id="txtLastname"]')
                lastname1.click()
                lastname1.send_keys(i[2])

                # 输入第一个生日
                date1 = driver.find_element_by_xpath('//*[@id="txtDOB"]')
                date1.click()
                date1.send_keys(i[8])
                driver.implicitly_wait(5)


                # 输入第二个last name
                lastname2 = driver.find_element_by_xpath('//*[@id="txtLastNameConfirm"]')
                lastname2.click()
                lastname2.send_keys(i[2])
                driver.implicitly_wait(5)


                # 输入第二个生日
                date2 = driver.find_element_by_xpath('//*[@id="txtDOBConfirm"]')
                date2.click()
                date2.send_keys(i[8])
                driver.implicitly_wait(5)


                # 输入随机ID
                ID = random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                                    'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                    'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
                                    'B', 'N', 'M'], 8)
                id = ''.join(ID)
                User_ID = driver.find_element_by_xpath('//*[@id="txtUserID"]')
                User_ID.click()
                User_ID.send_keys(id)
                driver.implicitly_wait(5)


                # 输入随机邮箱
                Email_Address = driver.find_element_by_xpath('//*[@id="txtEmailAddress"]')
                Email_Address.click()
                Email_Address.send_keys(id+"@163.com")
                driver.implicitly_wait(5)


                # 创建密码
                Password1 = driver.find_element_by_xpath('//*[@id="txtPassword"]')
                Password1.click()
                Password1.send_keys("ASDFasgh###555")
                driver.implicitly_wait(5)


                # 确认密码
                Password2 = driver.find_element_by_xpath('//*[@id="txtPasswordConfirm"]')
                Password2.click()
                Password2.send_keys('ASDFasgh###555')

                # 下拉滚动条到底
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)

                # 问题1
                Question1 = driver.find_element_by_xpath('//*[@id="drpSecQuestion1"]')
                Question1.click()
                Select(driver.find_element_by_id('drpSecQuestion1')).select_by_value('14')
                driver.implicitly_wait(10)

                # 输入随机ID
                ID = random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                                    'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                    'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
                                    'B', 'N', 'M'], 8)
                id = ''.join(ID)


                # 问题1答案
                Answer1 = driver.find_element_by_xpath('//*[@id="txtQuestion1"]')
                Answer1.click()
                Answer1.send_keys(id)
                driver.implicitly_wait(5)

                # 问题2
                Question2 = driver.find_element_by_xpath('//*[@id="drpSecQuestion2"]')
                Question2.click()
                Select(driver.find_element_by_id('drpSecQuestion2')).select_by_value('11')
                driver.implicitly_wait(5)

                # 输入随机ID
                ID = random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                                    'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                    'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
                                    'B', 'N', 'M'], 8)
                id = ''.join(ID)

                # 问题2答案
                Answer2 = driver.find_element_by_xpath('//*[@id="txtQuestion2"]')
                Answer2.click()
                Answer2.send_keys(id)
                driver.implicitly_wait(5)

                # 问题3
                Question3 = driver.find_element_by_xpath('//*[@id="drpSecQuestion3"]')
                Question3.click()
                Select(driver.find_element_by_id('drpSecQuestion3')).select_by_value('10')
                driver.implicitly_wait(5)

                # 输入随机ID
                ID = random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                                    'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                    'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
                                    'B', 'N', 'M'], 8)
                id = ''.join(ID)

                # 问题3答案
                Answer3 = driver.find_element_by_xpath('//*[@id="txtQuestion3"]')
                Answer3.click()
                Answer3.send_keys(id)
                driver.implicitly_wait(5)

                # 问题4
                Question4 = driver.find_element_by_xpath('//*[@id="drpSecQuestion4"]')
                Question4.click()
                Select(driver.find_element_by_id('drpSecQuestion4')).select_by_value('13')
                driver.implicitly_wait(5)

                # 输入随机ID
                ID = random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                                    'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'Q', 'W', 'E', 'R', 'T', 'Y',
                                    'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
                                    'B', 'N', 'M'], 8)
                id = ''.join(ID)

                # 问题4答案
                Answer4 = driver.find_element_by_xpath('//*[@id="txtQuestion4"]')
                Answer4.click()
                Answer4.send_keys(id)
                driver.implicitly_wait(5)
                time.sleep(2)

                html = driver.page_source
                print(html)



                driver.find_element_by_css_selector('#recaptcha-anchor > div.recaptcha-checkbox-border').click()




                # 点击人机验证   人工智能
                a = input('人工智能验证中：')
                # time.sleep(2)
                #
                # # 点击验证码
                # ActionChains(driver).move_by_offset(392, 820).click().perform()  # 鼠标左键点击
                # time.sleep(2)
                # # 点击人头
                # ActionChains(driver).move_by_offset(444, 1006).click().perform()  # 鼠标左键点击
                # # 等待5秒  通过验证
                # time.sleep(5)


                # 点击Next
                driver.find_element_by_xpath('//*[@id="btnNext"]').click()
                driver.implicitly_wait(10)


                # *****************************************************************************************************************************
                # 第二页

                # ActionChains(driver).move_by_offset(1765, 266).click().perform()  # 鼠标左键点击一律不


                # last name
                last1 = driver.find_element_by_xpath('//*[@id="txtLast"]')
                last1.click()
                last1.clear()
                last1.send_keys(i[2])

                # first name
                first = driver.find_element_by_xpath('//*[@id="txtFirst"]')
                first.click()
                first.send_keys(i[0])

                # Middle
                Middle = driver.find_element_by_xpath('//*[@id="txtMiddle"]')
                Middle.click()
                Middle.send_keys(i[1])

                # 出生日期
                bir = driver.find_element_by_xpath('//*[@id="txtDOB"]')
                bir.click()
                bir.send_keys(i[-1])

                # Eye Color
                Eye_Color = driver.find_element_by_xpath('//*[@id="drpEyeColor"]')
                Eye_Color.click()
                Select(driver.find_element_by_id('drpEyeColor')).select_by_value('BLU')

                # 随机10位数电话号码
                # nums = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
                num = "2562131565"

                # 下拉滚动条到底
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)

                # Primary Phone
                Primary_Phone = driver.find_element_by_xpath('//*[@id="txtPhone"]')
                Primary_Phone.click()
                Primary_Phone.send_keys(num)

                # ID State
                ID_State = driver.find_element_by_xpath('//*[@id="drpIDStateDisplay"]')
                ID_State.click()
                Select(driver.find_element_by_id('drpIDStateDisplay')).select_by_value('IL')

                # ID Type
                ID_Type = driver.find_element_by_xpath('//*[@id="drpIDType"]')
                ID_Type.click()
                Select(driver.find_element_by_id('drpIDType')).select_by_value('OL')

                # ID Number
                ID_Number = driver.find_element_by_xpath('//*[@id="txtIDNumber"]')
                ID_Number.click()
                ID_Number.send_keys(i[-3])

                # 隐式等待
                driver.implicitly_wait(5)

                # Weight as displayed on your Drivers License
                tizhong = driver.find_element_by_xpath('//*[@id="txtWeight"]')
                tizhong.click()
                tizhong.clear()
                tizhong.send_keys(j+10)
                print(j)

                # over
                driver.find_element_by_xpath('//*[@id="btnNext"]').click()

                html = driver.page_source
                soup = BeautifulSoup(html,'lxml')
                hahas = soup.select('#phTitle')
                haha_re = 'i> (.*?) <i'
                haha_geshi = re.compile(haha_re, re.S)
                haha = re.findall(haha_geshi, str(hahas))[0]
                print(haha)
                print(type(haha))
                if haha == "hahah": # "名", "中间名", "姓", "地址", "生日", "ssn", "驾照","体重"
                    f_csv.writerow(
                        {
                            '名': i[0],
                            '中间名': i[1],
                            '姓': i[2],
                            '地址': i[3],
                            '生日': i[4],
                            'ssn': i[5],
                            '驾照': i[6],
                            '体重':j
                        }
                    )
                    print('名:'+i[0]+'\n'+'中间名'+i[1]+'\n'+'姓:'+ i[2]+'\n'+'地址:'+i[3]+'\n'+'生日:'+i[4]+'\n'+'ssn:'+i[5]+'\n'+'驾照:'+i[6]+'\n'+'体重:'+j)
                    print("已写入...")
                    driver.find_element_by_xpath('//*[@id="btnHome"]').click()
                    driver.implicitly_wait(20)
                    time.sleep(2)

                    # Learn More
                    driver.find_element_by_xpath('//*[@id="home1"]/section/div/div[2]/div/a[2]').click()
                    break
                else:
                    driver.find_element_by_xpath('//*[@id="btnHome"]').click()
                    continue


        # 递归
        # get(driver)










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
    url = "https://www.ispfsb.com/Public/FOID.aspx"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    # 文件验证是否存在
    # if os.path.exists('./' + id + '.csv'):
    #     try:
    #         os.remove('./' + id + '.csv')
    #     except:
    #         print("请删除" + id + '.csv' + "原文件后重新运行！")
    #
    #     print(id + '.csv' + "已删除....")

    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 浏览器扩展程序
    # 语音识别程序
    extension_path1 = './1.2.2_0.crx'
    # xpath程序
    extension_path2 = './2.0.2_0.crx'

    options.add_extension(extension_path1)
    options.add_extension(extension_path2)
    driver = webdriver.Chrome(options=options) #driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?
    driver.maximize_window()
    # a = input("人工智障打码操作：")


    get(driver,url)
    # csv_read()
