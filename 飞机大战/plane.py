
import pygame as g

#玩家 飞机类
class Plane:
    def __init__(self,screen,player_settings,):
        self.screen = screen
        self.image = g.image.load("./images/me1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.player_settings = player_settings
        #飞机初始化   飞机在屏幕下方的中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #定义移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        self.sign_launch = False

    def biltme(self):
        """
        绘制玩家飞机
        :return:
        """
        self.screen.blit(self.image,self.rect)

    def change_position(self):
        #根据飞机标识  改变飞机的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.player_settings.player_change_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.player_settings.player_change_speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.bottom  -= self.player_settings.player_change_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom  += self.player_settings.player_change_speed





