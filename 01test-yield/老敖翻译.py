# import requests
# def fanyi():
#     kw = input('请输入你要翻译的文字：')
#     data = {'kw':kw }
#     url = 'https://fanyi.baidu.com/sug'
#     req = requests.post(url=url,data=data)
#     a = ''
#     for i in req.json()['data']:
#         a+=i["v"]+'\n'
#         print(kw+'翻译的结果为：')
#         print(a)
# if __name__ == '__main__':
#     fanyi()

# 有道翻译
import json
import requests


def translation():
    shuru = input("请输入要翻译的文本：")

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {}
    data["i"] = shuru
    data["from"] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '5639426771167'
    data['sign'] = '568c59da5ee3b59bce534d4e586dbaf3'
    data['ts'] = '1563942677116'
    data['bv'] = 'f355c521b6e13c15aa35c72a097b7786'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    req = requests.post(url, data=data)
    req.encoding = 'utf-8'
    print(req.text)
    relult = json.loads(req.text)
    re_list = []
    for i in range(len(relult["translateResult"][0])):
        # print(len(relult["translateResult"][0]))

        # print("翻译结果:%s" % (relult["translateResult"][0][i]['tgt']))
        re_list.append(relult["translateResult"][0][i]['tgt'])

    print("翻译结果:%s" % (str(re_list)))

if __name__ == '__main__':
    while True:
        translation()
