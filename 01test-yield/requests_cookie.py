import requests

s = requests.Session()

r1 = s.get('https://ajax.api.lianjia.com/config/cityConfig/getConfig?callback=jQuery111109944917597929641_1635790131165&type=province&category=1&_=1635790131166')
t = r1.encoding
print(r1.text)