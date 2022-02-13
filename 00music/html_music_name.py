#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :html_music_name.py
# @Time      :2022/1/18 22:59
# @Author    :杨晓东
import os
import random



def music():
    a1 = '{'  # 开头括号
    a2 = '''title: "<img src='./images/{}.jpg' alt='' /><div class='item-song'>{}</div><div class='item-artist'>{}</div>",'''  # 随机背景图片数字 and 歌名不要MP3 and 歌手名
    a3 = 'itunes: "{}/{}",'  # 文件夹名 and 歌曲名.mp3
    a4 = 'mp3: "{}/{}",'  # 文件夹名 and 歌曲名.mp3
    a5 = '},'  # 结尾括号
    rd = random.randint(1,45)
    # 文件夹名
    file_dir = "./music"
    with open("./正常歌曲名.txt",'w',encoding='utf-8') as fp:
        for root, dirs, files in os.walk(file_dir, topdown=False):  # 循环的到文件目录  以及 文件名
            print(root)  # 当前目录路径
            print(dirs)  # 当前目录下所有子目录
            print(files)  # 当前路径下所有非目录子文件
            for i in files:
                rd = random.randint(1, 45)
                name_list = i.split("-")
                music_name_mp3 = name_list[1].replace(" ","")
                ren_name = name_list[0].replace(" ","")
                music_name = music_name_mp3.replace(".mp3","")

                print(i)
                print(music_name_mp3)
                print(music_name)
                print(ren_name)

                fp.write(a1+'\n')
                fp.write('\t'+ a2.format(str(rd),music_name,ren_name)+'\n')
                fp.write('\t'+ a3.format(file_dir,i)+'\n')
                fp.write('\t'+ a4.format(file_dir,i)+'\n')
                fp.write(a5+'\n')
                print(i,"   已写入......................")

    print("over...............")






if __name__ == "__main__":
    music()







