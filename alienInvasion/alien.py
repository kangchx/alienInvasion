import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game, x = 0, y = 0):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen  = ai_game.screen
        self.settings = ai_game.settings

        #加载外星人图像并设置其初始位置
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #存储外星人的精确位置
        self.x = float(x)#float()确保其为 float 型
        self.y = float(y)
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed_x * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """检查外星人是否位于屏幕水平方向边缘，是则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def check_bottom(self):
        """检查外星人是否到达了低端，是则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def alien_drop(self):
        """向下移"""
        self.y += self.settings.alien_speed_y
        self.rect.y = self.y