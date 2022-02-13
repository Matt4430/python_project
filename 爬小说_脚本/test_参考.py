from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lxml.etree import HTML

driver = webdriver.Chrome()  # 打开浏览器

driver.get('https://www.xbiquge.la/')  # 打开页面

driver.find_element_by_xpath('//*[@id="hotcontent"]/div[1]/div[1]/dl/dt/a').click()  # 用xpath寻找到对应的小说名称

a_list = driver.find_elements_by_xpath(
    '//div[@id="list"]/dl/dd/a')  # 用xpath寻找到小说所有的章节，如果用find_element_by_xpath时只能找到一个，不能找到所有
for a in range(len(a_list)):  # 循环所有小说章节
    if (a >= 12) and ((a - 12) % 3 == 0):  # 默认浏览器窗口只能显示12章，当超过时需要移动鼠标，将没在浏览器可视区域内的元素移动到可视区域
        ActionChains(driver).move_to_element(a_list[a]).perform()  # 移动非可视区域内的元素移动到可视区域
        driver.implicitly_wait(20)  # 只能等待，等待元素加载完成，如时间到后都没加载完成会不等待执行下面代码
    driver.execute_script("arguments[0].click();", a_list[a])  # 对找到的章节进行点检，也可用a_list[a].click()，但该方法有时会出现找到的元素无法点击
    inner_text = driver.page_source  # 获取网页源码
    inner_html = HTML(inner_text)  # 对网页源码构建xpath解析树
    txt = inner_html.xpath('//div[@id="content"]/text()')  # 获取内容
    print(txt)
    driver.back()  # 内容获取完成后返回到上一页面
    driver.implicitly_wait(20)
    a_list = driver.find_elements_by_xpath(
        '//div[@id="list"]/dl/dd/a')  # 词句虽上方已经出现，但这里不能省略，因为点击返回到上一页面时页面的元素已经发生改变，如果继续使用上一页面获取的元素，在此页面将会找不到，故需从新获取页面元素
driver.close()  # 关闭浏览器
