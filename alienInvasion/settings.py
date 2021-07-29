class Settings:
    """存储游戏中的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #静态设置

        #屏幕设置
        self.screen_width = 800
        self.screen_heignt = 600
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3#设置屏幕上子弹限制

        #外星人设置
        self.alien_speed_y = 10

        #加快游戏节奏的速度
        self.speedup_scale = 1.1

        #外星人分数提高的速度
        self.alien_points_scale = 1.5

        #进行游戏动态设置
        self.initialize_dynamic_settings()

    #将以下设置单独成为一个函数，是因为以下属性在实例的生命周期中需要重新初始化
    def initialize_dynamic_settings(self):
        """初始化游戏动态设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed_x = 1.0
        self.alien_points = 50
        
        #fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高游戏速度和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_x *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.alien_points_scale)