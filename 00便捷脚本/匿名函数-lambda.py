import random


"""
    注意：
        调用匿名函数句柄时  要加括号（）
        无参数匿名函数调用时   要加括号（）
    复习：
        random函数   random.random()  会返回0-1之间的随机小数


"""

# 正常函数定义
def add(a,b=1):
    return a+b

print("正常函数："+str(add(5,5)))
print("正常函数："+str(add(5)))

# 匿名函数lambda 赋值运算
app = lambda x,y=20:x+y
print("匿名函数："+str(app(5,6)))
print("匿名函数："+str(app(8)))

# 匿名函数lambda判断运算
get_odd_even = lambda x,y:"even" if x % 2 ==0 and y % 2 == 0 else "odd"
print("匿名函数判断："+get_odd_even(16,28))
print("匿名函数判断："+get_odd_even(17,28))

# 无参数的匿名函数
num = lambda:random.random()
print(str(num()))
print(str(num()))
print(str(num()))
