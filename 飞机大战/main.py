import pygame as g
import sys
from settings import Settings
from plane import Plane
import game_functions as ga
from bullet import Bullet
from multiprocessing import Process


#游戏开始方法
def strat_game():
    #初始化这个游戏窗口
    g.init()
    #实例化  Setting 类
    player_setings = Settings()
    # 创建一个屏幕对象
    screen = g.display.set_mode((player_setings.screen_weight,player_setings.screen_hight))
    # 实例化Plane类
    player_plane = Plane(screen, player_setings)
    #实例化  子弹类
    # bullet = Bullet(player_setings,screen,player_plane)

    #窗口标题
    g.display.set_caption("老杨战机  v1.0")
    #容器存放多颗子弹
    bullets = []

    #敌机容器
    enemys = []

    #敌机子弹容器
    enemybullets = []

    bg_music = g.mixer.Sound("./sound/game_music.ogg")
    bg_music.set_volume(0.3)
    bg_music.play(-1)


    #状态
    while True:

        #调用事件操作方法
        ga.check_keyboard(player_plane,bullets,player_setings,screen)
        #调用更新窗口图像方法
        ga.update_screen(player_setings,player_plane,screen,bullets,enemys,enemybullets)

        #调用射击方法
        ga.launch_bullet(player_plane,bullets,player_setings,screen)

        # 调用创建敌机方法
        ga.create_enemys(player_setings,screen,enemys)

        #调用子弹删除
        ga.delete_bullet(bullets)

        #调用敌机 和 敌机子弹  删除方法
        # ga.delete_enemyandbullet(enemys,player_setings,enemybullets)

        #调用碰撞方法
        ga.is_bullet_enemy(bullets,enemys)

        #调用子弹抵消
        ga.bo_bo(bullets,enemybullets)

        #调用敌军飞机碰撞我方飞机   分数－100分
        ga.enemy_bo_plane(enemys,player_plane)

        #全屏炸弹
        ga.boo(enemys)





#程序入口
if __name__ == '__main__':
    strat_game()