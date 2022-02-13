
import itertools

def passwd(count):
    # 这个字符串比较长   用这个做测试吧
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*?_-."
    for i in range(6, 17):  # 密码长度  从5位数开始  16位数密码结束
         for c in itertools.product(chars, repeat=i):
            count += 1
            password = ''.join(c)
            print('*************** 第 ' + str(count) + ' 组密码 ***************')
            print(password)


if __name__ == '__main__':
    count = 1
    passwd(count)
    