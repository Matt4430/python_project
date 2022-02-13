import requests
from lxml import etree

def fanye_get(biaoqing,shuru1):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    b = 1
    for i in range(1,shuru1):
        url = 'https://www.doutula.com/search?type=photo&more=1&keyword='+biaoqing+'&page='+str(i)
        print('拼接好的URL地址：',url)

        # 开始请求url
        req = requests.get(url, headers=headers)

        # 解析网页
        html_data = etree.HTML(req.text)

        # 解析图片名和图片地址
        imgs = html_data.xpath('//*[@id="search-result-page"]/div/div/div[2]/div/div[1]/div/div/a/img/@data-backup')
        name = html_data.xpath('//*[@id="search-result-page"]/div/div/div[2]/div/div[1]/div/div/a/p/text()')

        # print('name  list ==================', name)
        # print('imgs  list ==================', imgs)
        a = 0

        # 遍历获取到的图片地址
        for i in imgs:
            if a < len(imgs):
                a = 0
            print('图片URL：', i)

            # 开始单独请求图片地址
            ree = requests.get(i, headers=headers)

            # print('字节形式查看图片内容：',ree.content)

            # 拼接文件名
            fi = './img/'
            filename =  str(b) + name[a] + i[-4:]
            filename = filename.replace('?','').replace('？','').replace('/','').replace("\\",'').replace(':','').replace('<','').replace('>','').replace('|','')
            filename = fi + filename
            print("filename=================",filename)


            # 以二进制形式写入文件
            with open(filename, 'wb') as fp:

                fp.write(ree.content)
                print(filename,"   下载完成！！！！！！！！！！！！！！")

                a += 1
                b += 1

    print("本次一共下载 {} 张图片！！！".format(b))

if __name__ == '__main__':
    表情名 = input("请输入你想爬取的表情包（按回车确定）：")
    shuru1 = input("请输入你想爬取多少页（一页72张）：")
    shuru1 = int(shuru1) + 1

    fanye_get(表情名,shuru1)