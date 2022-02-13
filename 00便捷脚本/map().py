

# 正常函数 一个参数
def add(x):
    return x ** 2

op = map(add,[2,4,6,8])
print("map一个参数："+str(list(op)))

# 正常函数 两个参数
def app(x,y):
    return x*y ** 2  # 先幂运算 再乘除加减

oo = map(app,[1,3,5,7,9],[2,4,6,8,10])
print("map两个参数："+str(list(oo)))

# 匿名函数 map 最low用法
pp = lambda x:x**2
po = map(pp,[5,6,7,8,9])
print("匿名函数lambda，map一个参数："+str(list(po)))

# 匿名函数 map 最靓用法
ox = map(lambda x:x**3 ,[1,2,3,4,5,6,7,8,9,10])
print("匿名函数 map 最靓用法: "+str(list(ox)))

