import pygame as g
from enemy_plane import EnemyPlane

#子弹类
class Bullet:
    def __init__(self,player_setings,screen,player_plane):
        self.screen = screen
        #创建一个矩形    子弹
        self.rect = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect1 = g.Rect(0,0, player_setings.bullet_width,player_setings.bullet_height)
        self.rect2 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect3 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect4 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect5 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect6 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect7 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect8 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect9 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect10 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect11 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)
        self.rect12 = g.Rect(0,0,player_setings.bullet_width,player_setings.bullet_height)


        #子弹的位置
        self.rect.centerx = player_plane.rect.centerx
        self.rect1.centerx = player_plane.rect.centerx + 10
        self.rect2.centerx = player_plane.rect.centerx - 10
        self.rect3.centerx = player_plane.rect.centerx + 20
        self.rect4.centerx = player_plane.rect.centerx - 20
        self.rect5.centerx = player_plane.rect.centerx + 30
        self.rect6.centerx = player_plane.rect.centerx - 30
        # self.rect7.centerx = player_plane.rect.centerx + 40
        # self.rect8.centerx = player_plane.rect.centerx - 40
        # self.rect9.centerx = player_plane.rect.centerx - 50
        # self.rect10.centerx = player_plane.rect.centerx + 50
        # self.rect11.centerx = player_plane.rect.centerx + 60
        # self.rect12.centerx = player_plane.rect.centerx - 60

        self.rect.top = player_plane.rect.top
        self.rect1.top = player_plane.rect.top
        self.rect2.top = player_plane.rect.top
        self.rect3.top = player_plane.rect.top
        self.rect4.top = player_plane.rect.top
        self.rect5.top = player_plane.rect.top
        self.rect6.top = player_plane.rect.top
        # self.rect7.top = player_plane.rect.top + 40
        # self.rect8.top = player_plane.rect.top + 40
        # self.rect9.top = player_plane.rect.top + 50
        # self.rect10.top = player_plane.rect.top + 50
        # self.rect11.top = player_plane.rect.top + 60
        # self.rect12.top = player_plane.rect.top + 60


        #子弹图像的矩形位置
        self.y = float(self.rect.y)
        self.y1 = float(self.rect1.y)
        self.y2 = float(self.rect2.y)
        self.y3 = float(self.rect3.y)
        self.y4 = float(self.rect4.y)
        self.y5 = float(self.rect5.y)
        self.y6 = float(self.rect6.y)
        # self.y7 = float(self.rect7.y)
        # self.y8 = float(self.rect8.y)
        # self.y9 = float(self.rect9.y)
        # self.y10 = float(self.rect10.y)
        # self.y11 = float(self.rect11.y)
        # self.y12 = float(self.rect12.y)


        self.x = float(self.rect.x)
        #速度
        self.bullet_speed = player_setings.bullet_speed
        #颜色
        self.bullet_color = player_setings.bullet_color

    def draw_bullet(self):
        """
        绘制子弹
        :return:
        """
        g.draw.rect(self.screen,self.bullet_color,self.rect)
        g.draw.rect(self.screen,self.bullet_color,self.rect1)
        g.draw.rect(self.screen,self.bullet_color,self.rect2)
        g.draw.rect(self.screen,self.bullet_color,self.rect3)
        g.draw.rect(self.screen,self.bullet_color,self.rect4)
        g.draw.rect(self.screen,self.bullet_color,self.rect5)
        g.draw.rect(self.screen,self.bullet_color,self.rect6)
        # g.draw.rect(self.screen,self.bullet_color,self.rect7)
        # g.draw.rect(self.screen,self.bullet_color,self.rect8)
        # g.draw.rect(self.screen,self.bullet_color,self.rect9)
        # g.draw.rect(self.screen,self.bullet_color,self.rect10)
        # g.draw.rect(self.screen,self.bullet_color,self.rect11)
        # g.draw.rect(self.screen,self.bullet_color,self.rect12)


    #子弹移动更新
    def move_update(self):
        self.y -= self.bullet_speed
        self.y1 -= self.bullet_speed
        self.y2 -= self.bullet_speed
        self.y3 -= self.bullet_speed
        self.y4 -= self.bullet_speed
        self.y5 -= self.bullet_speed
        self.y6 -= self.bullet_speed
        # self.y7 -= self.bullet_speed
        # self.y8 -= self.bullet_speed
        # self.y9 -= self.bullet_speed
        # self.y10 -= self.bullet_speed
        # self.y11 -= self.bullet_speed
        # self.y12 -= self.bullet_speed


        #更新位置
        self.rect.y = self.y
        self.rect1.y = self.y1
        self.rect2.y = self.y2
        self.rect3.y = self.y3
        self.rect4.y = self.y4
        self.rect5.y = self.y5
        self.rect6.y = self.y6
        # self.rect7.y = self.y7
        # self.rect8.y = se
        # self.rect9.y = self.y9
        # self.rect10.y = self.y10
        # self.rect11.y = self.y11
        # self.rect12.y = self.y12

