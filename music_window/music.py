# -*- coding: utf-8 -*-

"""
Created on 2019/8/20

@author: eln

@requirements: PyCharm 2017.2; Python 3.5.6 |Anaconda 4.1.1 (64-bit)

@decription: 用 Python 制作一个电子相册
"""
# pip install pillow pygame mutagen
import os
import sys
import threading
import tkinter as tk
import time
from PIL import ImageTk, Image
import pygame
from mutagen.mp3 import MP3


def playmusic():
    """播放音乐。"""
    Path = r'music\\'
    try:
        list1 = os.listdir(Path)  # 获取指定路径下所有的 mp3 文件
        for x in list1:
            if not (x.endswith('.mp3')):
                list1.remove(x)

        list2 = []
        for i in list1:
            s = os.path.join(Path, i)  # 对路径与文件进行拼接
            list2.append(s)

        while True:
            for n in list2:
                # 获取每一首歌的时长
                path = n
                audio = MP3(n)
                pygame.mixer.init()  # 初始化所有引入的模块
                pygame.mixer.music.load(path)  # 载入音乐，音乐可以是 ogg、mp3 等格式
                pygame.mixer.music.play()  # 播放载入的音乐
                time.sleep(int(audio.info.length))  # 获取每一首歌曲的时长，使程序存活的时长等于歌曲时长

    except Exception as e:
        print("Exception: %s" % e)


resolution = (1366, 768)  # 分辨率
Path = r'photo\\'  # 相册路径
Interval = 5  # 播放间隔.单位:s
Index = 0  # 当前照片计数
title = "电子相册"  # 窗口标题


def getfiles():
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files


files = getfiles()
print(files)
scaler = Image.ANTIALIAS  # 设定 ANTIALIAS ，即抗锯齿
root = tk.Tk()  # 创建窗口
root.title(title)  # 设置窗口标题

img_in = Image.open(Path + files[0])  # 加载第一张图片
# img_in = Image.open("load.jpg")  # 加载第一张图片
w, h = img_in.size  # 获取图片大小
size_new = (int(w * resolution[1] / h), resolution[1])
img_out = img_in.resize(size_new, scaler)  # 重新设置大小
img = ImageTk.PhotoImage(img_out)  # 用 PhotoImage 打开图片
panel = tk.Label(root, image=img)  # Label 自适应图片大小
panel.pack(side="bottom", fill="both", expand="yes")


def callback(e):
    """手动切换图片。"""
    try:
        global Index

        for i, x in enumerate(files):
            # 判断文件是否存在
            if not os.path.isfile(Path + '%s' % x):
                break

            if i != Index:  # 跳过已播放的图片
                continue

            print('手动处理图片', x, Index)  # python 3.5
            # print(unicode('手动处理图片 %s %d' % (x, Index), "utf8", errors="ignore"))  # python 2.7.15
            img_in = Image.open(Path + '%s' % x)
            print(img_in)
            w, h = img_in.size
            size_new = (int(w * resolution[1] / h), resolution[1])
            img_out = img_in.resize(size_new, scaler)
            img2 = ImageTk.PhotoImage(img_out)
            panel.configure(image=img2)
            panel.image = img2
            Index += 1
            if Index >= len(files):
                Index = 0
            break

    except Exception as e:
        print("Exception: %s " % e)
        sys.exit(1)


# root.bind("<Return>", callback)
root.bind("<Button-1>", callback)  # 点击窗口切换下一张图片


def image_change():
    """自动切换图片。"""
    try:
        global Index

        time.sleep(3)
        while True:
            for i, x in enumerate(files):
                # 判断文件是否存在
                if not os.path.isfile(Path + '%s' % x):
                    break

                if i != Index:  # 跳过已播放的图片
                    continue

                print('自动处理图片', x, Index)  # python 3.5
                # print(unicode('自动处理图片 %s %d' % (x, Index), "utf8", errors="ignore"))  # python 2.7.15
                img_in = Image.open(Path + '%s' % x)
                w, h = img_in.size
                size_new = (int(w * resolution[1] / h), resolution[1])
                img_out = img_in.resize(size_new, scaler)
                img2 = ImageTk.PhotoImage(img_out)
                panel.configure(image=img2)
                panel.image = img2
                Index += 1
                if Index >= len(files):
                    Index = 0
                time.sleep(Interval)

    except Exception as e:
        print("Exception: %s " % e)
        sys.exit(1)


m = threading.Thread(target=playmusic)  # 创建音乐播放线程
t = threading.Thread(target=image_change)  # 创建图片切换线程
# python 可以通过 threading module 来创建新的线程，然而在创建线程的线程（父线程）关闭之后，相应的子线程可能却没有关闭
# 需要把 setDaemon 函数放在 start 函数前面解决此问题
m.setDaemon(True)
m.start()  # 启动线程
t.start()  # 启动线程
root.mainloop()  # 窗口循环
