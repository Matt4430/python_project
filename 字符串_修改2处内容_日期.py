import datetime

pp = 'https://sycm.taobao.com/cc/cockpit/marcro/item/excel/top.json?spm=a21ag.12100459.item-rank.3.657550a5XzkT3L&dateRange=2021-08-16%7C2021-08-22&dateType=week&pageSize=10&page=1&order=desc&orderBy=payAmt&dtUpdateTime=false&keyword=&follow=false&cateId=&cateLevel=&guideCateId=&device=0&indexCode=itmUv%2CitemCartCnt%2CpayItmCnt%2CpayAmt'

# 前面日期
b = []
time22 = datetime.datetime.now() + datetime.timedelta(days=-2)
for i in range(1, 13):
    time = time22 + datetime.timedelta(days=-(i * 7 - 1))
    time1 = time.strftime('%Y-%m-%d')
    b.append(time1)

# 后面日期
c = []
time22 = datetime.datetime.now() + datetime.timedelta(days=-2)
for j in range(0,12):
    time = time22+ datetime.timedelta(days=(j*-7))
    time1 = time.strftime('%Y-%m-%d')
    c.append(time1)
# 前面日期修改后
gg = []
for f in b:
    a = list(pp)
    a[118:128] = str(f)
    a = ''.join(a)
    gg.append(a)
# 后面日期修改
tt = []

cc = 0
for fo in gg:
    cc += 1
    a = list(fo)
    a[131:141] = str(c[cc-1])
    a = ''.join(a)
    tt.append(a)


for po in tt:
    print(po)


