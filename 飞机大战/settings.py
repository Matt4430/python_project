


#配置文件  类
class Settings:
    """
    游戏设置类
    """
    def __init__(self):

        #游戏的窗口宽度
        self.screen_weight = 680
        #游戏的窗口高度
        self.screen_hight = 910
        #背景图片的地址
        self.background_image = './images/03.png'
        #玩家飞机速度
        self.player_change_speed = 20

        #子弹的参数

        #敌机飞机的速度
        self.enemy_plane_speed = 5
        #玩家子弹的速度
        self.bullet_speed = 25
        #子弹的宽度
        self.bullet_width  = 3
        #子弹的高度
        self.bullet_height = 10
        #子弹的颜色
        self.bullet_color = 255,255,0
        #敌军子弹颜色
        self.enemy_bullet_color = 255,0,0
        #敌机子弹  宽度
        self.enemy_bullet_width = 20
        #敌机子弹  高度
        self.enemy_bullet_height = 8

        #敌机子弹的速度
        self.enemy_bullet_speed = 6

        #状态
        self.da = True
        self.xiao = False

