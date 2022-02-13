from selenium import webdriver
import time

# 登陆
def login(login_qq, password):
    driver.get('https://www.xvideos.com/tags/s:views/m:3month/q:hd/hentai')  # URL
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

# 抓取
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

    driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[20]/a').click() # 点击下一页
    get_video(driver)

if __name__ == '__main__':
    # 定义账号密码
    qq_num = '2945711528@qq.com'
    qq_pwd = 'matt00789'
    # 去除浏览器被控  字样
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 拿到浏览器操作手柄
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # 调用程序
    login(qq_num, qq_pwd)
    get_video(driver)