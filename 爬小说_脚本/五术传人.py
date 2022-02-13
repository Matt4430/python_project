import requests
from bs4 import BeautifulSoup


def get_html(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    # print(req.text)
    html = req.text
    soup = BeautifulSoup(html,"html.parser")
    with open('./五术传人.txt','a',encoding='utf-8') as fp:
        table = soup.find("li",class_="active")
        name = table.text
        print(name)
        content = soup.find('div',class_="readcontent").text
        print(content)
        fp.write(name)
        fp.write(content)
        print('已写入: ',name)
        url = soup.find('a',id="linkNext").get('href')
        get_html(url)




if __name__ == '__main__':
    url = 'https://www.yeshuyuan.com/read/53887/17033995.html'

    get_html(url)