import requests
from bs4 import BeautifulSoup

url = 'https://sycm.taobao.com/cc/macroscopic_monitor?spm=a21ag.8718589.TopMenu.d227.33db50a5pyaJSG#item-rank'
req = requests.get(url)
html = BeautifulSoup(req.content, 'lxml', from_encoding='utf-8')
print(html)