

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
    for i in range(5,16): # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)



@time_out
def Lower_case_letters(a=5,count=0):
    """
    纯小写字母
    :return:
    """
    chars = "abcdefghijklmnopqrstuvwxyz"

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)


@time_out
def uppercase_letter(a=5,count=0):
    """
    纯大写字母
    :return:
    """
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_Lower_case_letters(a=5,count=0):
    """
    数字 + 小写字母
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_uppercase_letter(a=5,count=0):
    """
    数字 + 大写字母
    :return:
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_z_Z(a=5,count=0):
    """
    数字 + 小写字母 + 大写字母
    :return:
    """

    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_symbol(a=5,count=0):
    """
    数字 + 符号
    :return:
    """
    chars = "0123456789~!@#$%^&*?_-."

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_z_symbol(a=5,count=0):
    """
    数字 + 小写字母 + 符号
    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*?_-."

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_Z_symbol(a=5,count=0):
    """
    数字 + 大写字母 + 符号
    :return:
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)

@time_out
def num_z_Z_symbol(a=5,count=0):
    """
    数字 + 小写字母 + 大写字母 + 符号

    :return:
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."

    for i in range(5, 16):  # 密码长度  从5位数开始
        for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            # print('*************** 第 ' + str(count) + ' 组密码 ***************')
            # print(password)


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
