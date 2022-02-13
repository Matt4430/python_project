

import itertools
import time

# 装饰器 计算时间
def time_out(a_func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = a_func(*args, **kwargs)
        end = time.time()
        print("程序：" + a_func.__name__,"    运行时间：" + str(end - start))
        return result
    return clocked

@time_out
def num(a=5, count=0):
    """
    纯数字
    :return:
    """
    chars = "0123456789"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def Lower_case_letters(a=5,count=0):
    """
    纯小写字母
    :return:
    """
    chars = "abcdefghijklmnopqrstuvwxyz"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "小写字母" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def uppercase_letter(a=5,count=0):
    """
    纯大写字母
    :return:
    """
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "大写字母" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_Lower_case_letters(a=5,count=0):
    """
    数字 + 小写字母
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字+小写字母" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_uppercase_letter(a=5,count=0):
    """
    数字 + 大写字母
    :return:
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字+大写字母" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_z_Z(a=5,count=0):
    """
    数字 + 小写字母 + 大写字母
    :return:
    """

    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字+小写字母+大写字母" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_symbol(a=5,count=0):
    """
    数字 + 符号
    :return:
    """
    chars = "0123456789~!@#$%^&*?_-."

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字+符号" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_z_symbol(a=5,count=0):
    """
    数字 + 小写字母 + 符号
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*?_-."

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)

    return print("长度为" + str(a) + "位的   “" + "数字+小写字母+符号" + "”  组成密码，一共 " + str(count) + " 组！")


@time_out
def num_Z_symbol(a=5,count=0):
    """
    数字 + 大写字母 + 符号
    :return:
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)


    return print("长度为" + str(a) +"位的   “"+"数字+大写字母+符号"+ "”  组成密码，一共 " +str(count)+" 组！")


@time_out
def num_z_Z_symbol(a=5,count=0):
    """
    数字 + 小写字母 + 大写字母 + 符号

    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."

    for c in itertools.product(chars, repeat=a):
        count += 1
        password = ''.join(c)
        # print('*************** 第 ' + str(count) + ' 组密码 ***************')
        # print(password)


    return print("长度为" + str(a) +"位的   “"+"数字+小写字母+大写字母+符号"+ "”  组成密码，一共 " +str(count)+" 组！")



if __name__ == '__main__':
    num_a = 4
    count = 0


    # 纯数字
    # num(num_a, count)

    # 纯小写字母
    # Lower_case_letters(num_a, count)

    # 纯大写字母
    # uppercase_letter(num_a, count)

    # 数字 + 小写字母
    # num_Lower_case_letters(num_a, count)

    # 数字 + 大写字母
    # num_uppercase_letter(num_a, count)

    # 数字 + 小写字母 + 大写字母
    # num_z_Z()

    # 数字 + 符号
    # num_symbol(num_a, count)

    # 数字 + 小写字母 + 符号
    # num_z_symbol(num_a, count)

    # 数字 + 大写字母 + 符号
    # num_Z_symbol(num_a, count)

    # 数字 + 小写字母 + 大写字母 + 符号
    # num_z_Z_symbol(num_a, count)
