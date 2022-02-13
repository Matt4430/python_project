from selenium import webdriver
import time
import json
import requests


# cookie登陆
def login(url):
    driver.get(url)  # URL
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
def get_video(ye,url):
    ur = driver.current_url
    print("网址======" + ur)
    print("网址类型===" + str(type(ur)))
    ye += 1
    name = url[-2:]
    print(name)

    with open("url.txt","a",encoding="utf-8") as f:
        for i in range(1, 28):
            driver.implicitly_wait(20)

            driver.find_element_by_xpath(
                "/html/body/div/div[4]/div[4]/div[1]/div[" + str(i) + "]/div[1]/div/a/img[1]").click()  # 点击图片进入
            driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址
            # p = input("123")
            # 获取浏览器中所有标签页的句柄值
            handles = driver.window_handles
            if len(handles) == 1 or len(handles) < 2:
                print('-' * 10 + "当前第 " + str(ye) + "页   " + "开始点击下载第 " + str(i) + " 部 ！" + '-' * 10)
                driver.find_element_by_xpath('//*[@id="v-actions"]/div[2]/button[2]').click()  # 点击下载
                driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址

                uu = driver.find_element_by_xpath('//*[@id="tabDownload"]/div/p/a[2]').get_attribute("href")  # 获取高清视频url
                print("视频地址===="+uu)
                f.write(uu+"\n")
                driver.back()  # 返回上一界面
                print("第 " + str(ye) + "页 " + "第 " + str(i) + " 部视频已下载.......")
            else:
                print("遇到广告.....")
                # 切换窗口
                driver.switch_to.window(handles[0])
                time.sleep(5)
                print("广告：：：：：窗口：" + handles[0])
                print("ur====" + ur)
                # # 刷新当前页面
                # driver.refresh()
                # driver.implicitly_wait(20)
                b = i + 1
                if b <= 27:
                    driver.find_element_by_xpath(
                        "/html/body/div/div[4]/div[4]/div[1]/div[" + str(b) + "]/div[1]/div/a/img[1]").click()  # 点击图片进入
                    driver.implicitly_wait(20)  # 隐示等待，为了等待充分加载好网址
                else:
                    f.close()
                    break

    print("第 " + str(ye) + " 页开始....")
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[20]/a').click()  # 点击下一页
    get_video(ye,url)
    print("下载已完成！" + str(ye) + " 页 停止！")




if __name__ == '__main__':
    url = 'https://www.xvideos.com/?k=日本'
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
    prefs = {"download.default_directory": r"D:\007\0"}
    # 将自定义设置添加到chrome配置对象实例中
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 拿到浏览器操作手柄
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # 调用程序
    login(url)
    get_video(ye,url)
