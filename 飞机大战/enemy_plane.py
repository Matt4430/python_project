import pygame as g
import random

#敌机类
class EnemyPlane:
    def __init__(self,screen,player_settings):
        self.screen = screen
        self.player_settings = player_settings

        #定义标识
        self.booo = False

        #敌机属性   图像 rect属性
        im1 = "./images2/enemy1.png"
        im2 = "./images2/enemy2.png"
        im3 = "./images2/enemy3_n1.png"
        images = [im1,im2,im3]
        num = random.randint(0,2)
        if num == 0:
            self.images = g.image.load(images[0])
        if num == 1:
            self.images = g.image.load(images[1])
        if num == 2:
            self.images = g.image.load(images[1])
        # self.image2 = g.image.load("./images2/enemy2.png")
        self.rect = self.images.get_rect()
        # self.rect2 = self.image2.get_rect()

        #敌机的坐标
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # self.rect2.x = self.rect2.width
        # self.rect2.y = self.rect2.height

        #定义敌机飞机水平位置
        self.x = float(self.rect.x)
        # self.x2 = float(self.rect2.x)


    #画敌机
    def blitme(self):
        self.screen.blit(self.images,self.rect)
        # self.screen.blit(self.image2,self.rect2)

        # self.move_enemy()

    #移动方法   移动速度
    def move_enemy(self):
        self.rect.y += 2
        # self.rect2.y += 2

