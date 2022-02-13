
# 使用cookie登陆

from selenium import webdriver
import time
import json

#填写webdriver的保存目录
driver = webdriver.Chrome()
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#         "source": """
#         Object.defineProperty(navigator, 'webdriver', {
#           get: () => undefined
#         })
#       """
#     })

#记得写完整的url 包括http和https
driver.get('https://sycm.taobao.com/custom/enterprise_info')
#首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookie.txt','r') as cookief:
    #使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    # print(cookieslist)
    for cookie in cookieslist:
        print(cookie)
        if 'sameSite' in cookie:
            del cookie['sameSite']
        driver.add_cookie(cookie)

