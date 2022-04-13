import pygame as g
from enemy_plane import EnemyPlane

#敌军子弹类
class EnemyBullet:
    def __init__(self,player_setings,screen,enemy_plane):
        self.screen = screen
        #创建一个矩形    子弹
        self.rect = g.Rect(0,0,player_setings.enemy_bullet_width,player_setings.enemy_bullet_height)

        #子弹的位置
        self.rect.centerx = enemy_plane.rect.centerx
        self.rect.bottom = enemy_plane.rect.bottom

        #子弹图像的矩形位置
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        #速度
        self.bullet_speed = player_setings.enemy_bullet_speed
        #颜色
        self.bullet_color = player_setings.enemy_bullet_color

    def draw_bullet(self):
        """
        绘制子弹
        :return:
        """
        g.draw.rect(self.screen,self.bullet_color,self.rect)

    #子弹移动更新
    def move_update(self):
        self.y += self.bullet_speed

        #更新位置
        self.rect.y = self.y
