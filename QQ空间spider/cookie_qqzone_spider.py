import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests

# 登陆QQ访问对方QQ空间
def login(login_qq, password, business_qq):
    '''
    登陆
    :param login_qq: 登陆用的QQ
    :param password: 登陆的QQ密码
    :param business_qq: 业务QQ
    :return: driver
    '''


    print("开始登陆中...")
    driver.get('https://user.qzone.qq.com/{}/311'.format(business_qq))  # URL
    driver.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
    driver.find_element_by_id('login_div')
    driver.switch_to.frame('login_frame')  # 切到输入账号密码的frame
    driver.find_element_by_id('switcher_plogin').click()  ##点击‘账号密码登录’
    driver.find_element_by_id('u').clear()  ##清空账号栏
    driver.find_element_by_id('u').send_keys(login_qq)  # 输入账号
    driver.find_element_by_id('p').clear()  # 清空密码栏
    driver.find_element_by_id('p').send_keys(password)  # 输入密码
    driver.find_element_by_id('login_button').click()  # 点击‘登录’
    driver.switch_to.default_content()

    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        print("登陆完成....")
        return driver
    except:
        print('不能访问' + business_qq)
        return None


# 抓取说说
def get_shuoshuo(driver):
    page = 1
    while True:
        # 下拉滚动条
        for j in range(1, 5):
            driver.execute_script("window.scrollBy(0,5000)")
            time.sleep(2)

            # 切换 frame
        driver.switch_to.frame('app_canvas_frame')
        # 构建 BeautifulSoup 对象
        bs = BeautifulSoup(driver.page_source.encode('GBK', 'ignore').decode('gbk'))
        # 找到页面上的所有说说
        pres = bs.find_all('pre', class_='content')

        for pre in pres:
            shuoshuo = pre.text
            tx = pre.parent.parent.find('a', class_="c_tx c_tx3 goDetail")['title']
            print(tx + ":" + shuoshuo)
            with open('她的空间动态.txt', 'a+') as f:
                f.write('\n' + tx + ":" + shuoshuo + '\n')
                f.close()

            # 页数判断
        page = page + 1
        maxPage = bs.find('a', title='末页').text

        if int(maxPage) < page:
            break

        driver.find_element_by_link_text(u'下一页').click()
        # 回到主文档
        driver.switch_to.default_content()
        # 等待页面加载
        time.sleep(3)

# 计数函数
def num(name_a):
    name_a+=1
    return name_a


# 下载图片  单个相册中点击图片
def get_photo(driver):
    # 照片下载路径

    photo_path = r"E:\DC\2548957387\{}.jpg"
    mkdir_path = r'E:\DC\2548957387'

    if os.path.exists(mkdir_path):
        pass
    else:
        mkdir_path = os.mkdir(r'E:\DC\2548957387')


    # 相册索引
    photoIndex = 1

    while True:
        # 回到主文档
        driver.switch_to.default_content()
        # driver.switch_to.parent_frame()
        # 点击头部的相册按钮
        driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[3]/a').click()
        # 等待加载
        driver.implicitly_wait(10)
        time.sleep(3)
        # 切换 frame
        driver.switch_to.frame('app_canvas_frame')
        # 各个相册的超链接
        a = driver.find_elements_by_class_name('album-cover')
        # 单个相册
        a[photoIndex].click()
        # 隐式等待，5秒钟内只要找到了元素就开始执行，10秒钟后未找到，就超时；
        driver.implicitly_wait(10)
        # 等待10秒
        time.sleep(3)
        # 相册的第一张图
        p = driver.find_elements_by_class_name('item-cover')[0]
        p.click()
        time.sleep(3)

        # 相册大图在父frame，切换到父frame
        driver.switch_to.parent_frame()
        # 循环相册中的照片
        name_a = 0
        while True:
            # 照片url地址和名称
            # img = driver.find_element_by_id('js-img-disp')
            img = driver.find_element_by_xpath('//*[@id="js-img-border"]/img')
            print(img)
            src = img.get_attribute('src').replace('&t=5', '')
            name = driver.find_element_by_id("js-photo-name").text

            # 下载
            print(src)
            print(photo_path.format(name))

            req = requests.get(src)
            name_a+=1


            with open(photo_path.format(name + "-" + str(name_a)),'wb') as f:
                f.write(req.content)
                f.close()
                print("第 {} 张，已下载！！！！".format(name_a))
            # urlretrieve(src,photo_path.format(miss_qq,name))

            # 取下面的 当前照片张数/总照片数量
            counts = driver.find_element_by_xpath('//*[@id="js-ctn-infoBar"]/div/div[1]/span').text
            print(counts + "张！")

            counts = counts.split('/')
            # 最后一张的时候退出照片浏览
            if counts[0] == counts[1]:
                # 右上角的 X 按钮
                driver.find_element_by_xpath('//*[@id="js-viewer-main"]/div[1]/a').click()
                print("右上角x")
                break
            # 点击 下一张，网页加载慢，所以10次加载
            for i in (1, 10):
                if driver.find_element_by_id('js-btn-nextPhoto'):
                    n = driver.find_element_by_id('js-btn-nextPhoto')
                    ActionChains(driver).click(n).perform()
                    print("等待1秒，点击下一张.....")
                    time.sleep(1)
                    break
                else:
                    time.sleep(5)
                    print("否则time5秒")

                    # 相册数量比较，是否下载了全部的相册
        photoIndex = photoIndex + 1
        if len(a) <= photoIndex:
            break




if __name__ == '__main__':
    # 输入QQ信息
    qq_num = input("请输入自己的QQ：")
    qq_pwd = input("请输入自己的QQ密码：")
    miss_qq = input("请输入要查看的QQ：")

    # 标识 当前目录
    path = os.getcwd()
    url = "https://www.ispfsb.com/Public/FOID.aspx"
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
    extension_path2 = r'E:\Desktop\matt_spider\QQ空间spider\XPath Helper 2.0.2\2.0.2_0.crx'
    # options.add_extension(extension_path1)
    options.add_extension(extension_path2)
    driver = webdriver.Chrome(options=options)  # driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')?
    driver.maximize_window()
    # 登陆
    login(qq_num, qq_pwd, miss_qq)
    # 爬取说说
    get_shuoshuo(driver)
