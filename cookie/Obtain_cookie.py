
# 获取cookie

from selenium import webdriver
import time
import json

qq_num = '2426325927'

#填写webdriver的保存目录
driver = webdriver.Chrome()

#记得写完整的url 包括http和https
# driver.get('https://user.qzone.qq.com/{}/311'.format(qq_num))
driver.get('https://passport.lagou.com/login/login.html')


#程序打开网页后20秒内手动登陆账户
time.sleep(30)
cook = driver.get_cookies()
print(cook)

with open('cookies.txt', 'w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.close()
print('0000000000000000000000000000000000000000000000000000')
