import requests
from bs4 import BeautifulSoup

def get_html():
    url = 'http://www.biquger.net/html/40/40414/19538015.html'
    req = requests.get(url)
    req.encoding = 'gbk'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    with open('./震惊！我修仙秘密被孙女直播曝光.txt', 'a', encoding='utf-8') as fp:
        for i in range(562):
            title = soup.find("h1")
            name = title.text
            print(name)
            content = soup.find('div', id="nr1").text
            print(content)
            fp.write('\n'+name+'\n')
            fp.write('\n')
            fp.write(content+'\n')
            print('已写入: ', name)
            urls = soup.find('a', id="pb_next").get('href')
            # print(urls)
            ping = 'http://www.biquger.net'
            urll = ping + urls
            print(urll)
            req = requests.get(urll)
            req.encoding = 'gbk'
            html = req.text
            soup = BeautifulSoup(html, "html.parser")

if __name__ == '__main__':
    get_html()
