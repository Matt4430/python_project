import requests
from bs4 import BeautifulSoup
import fake_useragent


def get_url(num):
    with open('./url.txt','r',encoding='utf-8')as f:
        a = f.readlines()
        print(str(len(a)),' 条记录 ..')
        for i in a:
            print(i)

            # 实例化 user-agent 对象
            ua = fake_useragent.UserAgent()
            headers = {
                'User-Agent': ua.random
            }

            req = requests.get(i,headers=headers)
            soup = BeautifulSoup(req.content, 'lxml', from_encoding='utf-8')

            print(soup)
            break
            # # url_list_a = soup.find_all('div')
            # url_list_a = soup.findAll(name="div", attrs={"class" :"mozaique cust-nb-cols"})
            # lis = []
            # with open("jk.txt","a",encoding="utf-8") as f:
            #     for i in url_list_a:
            #         uu = i.findAll(name="div", attrs={"class" :"thumb"})
            #         for j in uu:
            #             ua = j.findAll('a')
            #             for g in ua:
            #                 ug = g.get('href')
            #                 lis.append(ug)
            #                 # print(ug)
            #                 # print(type(ug))
            #                 jj = join_url+ug
            #                 print(jj)
            #                 f.write(jj+"\n")
    num += 1
    print('第  {}  页'.format(num))
    get_url(num)

if __name__ == '__main__':
    num = 1
    get_url(num)