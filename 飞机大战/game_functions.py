
#存放 方法（函数）
import pygame as g
import sys
from bullet import Bullet
from enemy_plane import EnemyPlane
import random
from enemy_bullet import EnemyBullet
from multiprocessing import Process
from time import sleep

bullet_count = 0
enemy_count = 0
enemy_bullet_count = 0
score = 0
booo = False   #全屏炸弹标识    按b键全部消失



#监听键盘和鼠标事件
def check_keyboard(player_plane,bullets,player_setings,screen):
    global booo
    # 监听鼠标事件
    for event in g.event.get():
        if event.type == g.QUIT:
            sys.exit()

        elif event.type == g.KEYDOWN:
            #检测  右键是否按下
            if event.key == g.K_RIGHT or event.key == g.K_d:
                player_plane.moving_right = True
            if event.key == g.K_LEFT or event.key == g.K_a:
                player_plane.moving_left = True
            if event.key == g.K_UP or event.key == g.K_w:
                player_plane.moving_top = True
            if event.key == g.K_DOWN or event.key == g.K_s:
                player_plane.moving_bottom = True
            if event.key == g.K_SPACE or event.key == g.K_0:
                player_plane.sign_launch = True
            if event.key == g.K_b:
                booo = True   #全屏炸弹




        elif event.type == g.KEYUP:
            #检测   按键是否松开
            if event.key == g.K_RIGHT or event.key == g.K_d:
                player_plane.moving_right = False
            if event.key == g.K_LEFT or event.key == g.K_a:
                player_plane.moving_left = False
            if event.key == g.K_UP or event.key == g.K_w:
                player_plane.moving_top = False
            if event.key == g.K_DOWN or event.key == g.K_s:
                player_plane.moving_bottom = False
            if event.key == g.K_SPACE or event.key == g.K_0:
                player_plane.sign_launch = False
            if event.key == g.K_b:
                booo = False


#射击方法  我方子弹速度
def launch_bullet(player_plane,bullets,player_setings,screen):
    global bullet_count
    if player_plane.sign_launch:
        if bullet_count % 5 == 0:
            new_bullet = Bullet(player_setings,screen,player_plane)
            bullets.append(new_bullet)
            # 播放音效
            bullet_music = g.mixer.Sound("./sound/bullet.wav")
            bullet_music.set_volume(0.9)
            bullet_music.play(0)
        bullet_count += 1
    if bullet_count == 10000:
        bullet_count = 0

#删除超出屏幕的子弹
def delete_bullet(bullets):
    #遍历里所有的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#超出屏幕的敌机和敌机子弹
def delete_enemyandbullet(enemys,player_settings,enemybullets):
    #遍历所有敌机和敌机子弹
    for enemy_plane in enemys:
        if enemy_plane.rect.top > player_settings.screen_hight:
            enemys.remove(enemy_plane)
    for enemy_bullet in enemybullets:
        if enemy_bullet.rect.top > player_settings.screen_hight:
            enemybullets.remove(enemy_bullet)






#创建敌机方法
def create_enemys(player_settings,screen,enemys):
    global enemy_count
    if enemy_count % 20 == 0:
        #实例化敌机
        enemy = EnemyPlane(screen,player_settings)
        # enemy2 = EnemyPlane(screen,player_settings)
        enemy.rect.x = random.randint(0,player_settings.screen_weight-enemy.images.get_width())
        enemy.rect.y = 0
        # enemy2.rect2.x = random.randint(0, player_settings.screen_weight - enemy2.image2.get_width())
        # enemy2.rect2.y = 0
        enemys.append(enemy)
        # enemys.append(enemy2)


    if enemy_count == 10000:
        enemy_count = 0
    enemy_count += 1



#更新窗口图像
def update_screen(player_setings,player_plane,screen,bullets,enemys,enemybullets):
    global score
    global enemy_bullet_count
    # 创建一个屏幕对象
    # screen = g.display.set_mode((player_setings.screen_weight, player_setings.screen_hight))
    # 背景图片地址
    # background_image_path = player_setings.background_image
    background = g.image.load(player_setings.background_image)
    # 填充背景图片
    screen.blit(background, (0, 0))
    # 调用  绘制玩家飞机的方法
    player_plane.biltme()
    #调用玩家飞机移动的方法
    player_plane.change_position()
    #调用子弹绘制方法
    # bullet = Bullet(player_setings,screen,player_plane)
    # bullet.draw_bullet()
    # bullet.move_update()

    for bullet in bullets:
        bullet.draw_bullet()
        bullet.move_update()

    #调用绘制敌机的方法
    for enemy in enemys:
        enemy.blitme()
        enemy.move_enemy()
        # if enemy_count % 20 == 0 :
            #创建敌机子弹

            # enemybullet = EnemyBullet(player_setings,screen,enemy)
            # enemybullet.rect.bottom = enemy.rect.bottom
            # enemybullets.append(enemybullet)

            # p = Process(target=update_screen)
            # p.start()
            # sleep(0.1)
            # p.join()
            # p.close()


    for enemybullet in enemybullets:
        enemybullet.draw_bullet()
        enemybullet.move_update()

    #绘制分数
    myfont = g.font.SysFont("微软雅黑",25)
    textinfo = myfont.render("Score:"+str(score),True,(255,0,0))
    screen.blit(textinfo,(0,10))

    # 刷新窗口
    g.display.update()


#子弹碰撞敌机
def is_bullet_enemy(bullets,enemys):
    global score
    for bullet in bullets:
        for enemy in enemys:
            if bullet.rect.x - 60> enemy.rect.x+enemy.rect.width or enemy.rect.x > bullet.rect.x - 60 + bullet.rect.width *13*2  or bullet.rect.y > enemy.rect.y+enemy.rect.height or enemy.rect.y >bullet.rect.y+bullet.rect.height:
                pass
            else:
                #移除子弹和敌机
                bullets.remove(bullet)
                enemys.remove(enemy)
                enemy_music = g.mixer.Sound("./sound/use_bomb.wav")
                enemy_music.set_volume(0.4)
                enemy_music.play()
                score += 10

#敌机碰撞我方飞机
def enemy_bo_plane(enemys,plane):
    global score
    for enemy in enemys:
        if enemy.rect.x > plane.rect.x + plane.rect.width or plane.rect.x > enemy.rect.x + enemy.rect.width or enemy.rect.y > plane.rect.y + plane.rect.height or plane.rect.y > enemy.rect.y + enemy.rect.height:
            pass
        else:
            #移除子弹和敌机
            enemys.remove(enemy)
            enemy_music = g.mixer.Sound("./sound/me_down.wav")
            enemy_music.set_volume(0.4)
            enemy_music.play()
            score -= 100



#子弹碰撞子弹
def bo_bo(bullets,enemybullets):
    for bullet in bullets:
        for enemybullet in enemybullets:
            if bullet.rect.x - 60 > enemybullet.rect.x+enemybullet.rect.width or enemybullet.rect.x > bullet.rect.x - 60 + bullet.rect.width *13*2 or bullet.rect.y > enemybullet.rect.y+enemybullet.rect.height or enemybullet.rect.y >bullet.rect.y+bullet.rect.height:
                pass
            else:
                enemybullets.remove(enemybullet)
                bullets.remove(bullet)
                # p = Process(target=bo_bo)
                # p.start()
                # p.join()
                # p.close()

#全屏炸弹  方法
def boo(enemys):
    a = 0
    global score
    global booo
    for enemy in enemys:
        if booo == True:
            enemys.remove(enemy)
            enemy_music = g.mixer.Sound("./sound/me_down.wav")
            enemy_music.set_volume(0.4)
            enemy_music.play()
            a += 1
            score += a

        else:
            pass


