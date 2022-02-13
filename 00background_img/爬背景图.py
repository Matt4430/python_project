#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :爬背景图.py
# @Time      :2022/1/17 22:06
# @Author    :杨晓东

'''
    下载HTML——music 背景图
'''



import requests
# import sys
# print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['E:\\Desktop\\matt_spider', 'E:/Desktop/matt_spider'])



def get():
    url = 'https://cdn.jsdelivr.net/gh/volantis-x/cdn-wallpaper-minimalist/2020/00'
    url1 = 'https://cdn.jsdelivr.net/gh/volantis-x/cdn-wallpaper-minimalist/2020/0'
    nums = 1
    for num in range(1,57):
        if num < 10:
            a = url + str(num) + '.jpg'
            req = requests.get(a)
            st = req.status_code
            print(a)
            print(st)

            if st == 200:
                f = open("./img/%s.jpg" % nums, 'wb')  # 以二进制格式写入img文件夹中
                f.write(req.content)
                f.close()
                print("第%s张图片下载完毕" % nums)
                nums = nums + 1
            else:
                continue
        else:
            a = url1 + str(num) + '.jpg'
            req = requests.get(a)
            st = req.status_code
            print(a)
            print(st)

            if st == 200:
                f = open("./img/%s.jpg" % nums, 'wb')  # 以二进制格式写入img文件夹中
                f.write(req.content)
                f.close()
                print("第%s张图片下载完毕" % nums)
                nums = nums + 1
            else:
                continue



if __name__ == "__main__":
    get()
