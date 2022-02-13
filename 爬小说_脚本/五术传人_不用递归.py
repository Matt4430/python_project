import requests
from bs4 import BeautifulSoup


def get_html():
    url = 'https://www.yeshuyuan.com/read/53887/17033995.html'
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    with open('./五术传人0.txt', 'a', encoding='utf-8') as fp:
        for i in range(712):
            table = soup.find("li", class_="active")
            name = table.text
            print(name)
            content = soup.find('div', class_="readcontent").text
            print(content)
            fp.write('\n'+name+'\n')
            fp.write('\n')
            fp.write(content+'\n')
            print('已写入: ', name)
            urls = soup.find('a', id="linkNext").get('href')
            req = requests.get(urls)
            req.encoding = 'utf-8'
            html = req.text
            soup = BeautifulSoup(html, "html.parser")


if __name__ == '__main__':
    get_html()
