import requests
from lxml import etree
url = 'http://www.ywggzy.com/bxwx/28463/4152307.html'

def txt_html(url):
    req = requests.get(url,timeout=20)
    print(req)
    html = etree.HTML(req.text)
    print(html)
    with open(r'D:\下载暂存\小说.txt', 'a', encoding='utf-8') as fp:
        txt = html.xpath('//*[@id="content"]/text()')
        print(txt)
        for j in txt:
            j=j.strip('\n')
            j=j.strip('\r\n                        \u3000\u3000')
            # j = j.strip('\u3000\u3000')
            # print(j)
            fp.write(j+'\n')
        for i in range(999999):
            href = html.xpath('//*[@id="container"]/div/div/div[2]/div[1]/a[3]/@href')
            print(href)
            href = href[0]
            href.lstrip('bxwx/28463/')
            urls = 'http://www.ywggzy.com/bxwx/28463/' + str(href)
            print(urls)
            req = requests.get(urls,timeout=20)
            print(req)
            html = etree.HTML(req.text)
            txt = html.xpath('//*[@id="content"]/text()')
            print(txt)
            for a in txt:
                a=a.strip('\n')
                a=a.strip('\r\n                        \u3000\u3000')
                # a=a.strip('\u3000\u3000')
                # print(a)
                fp.write(a+'\n')



if __name__ == '__main__':
    txt_html(url)
