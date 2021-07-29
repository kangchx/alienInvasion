import pygame
from pygame.sprite import Sprite

#玩家控制的Ship 与Alien，Bullet不同，玩家控制的Ship在整个游戏中只会实例化一次
class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #移动标志
        self.moving_right = False
        self.moving_left = False

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #生成飞船
        self.ship_reborn()

    def update(self):
        """根据移动标志调整飞船位置"""
        #更新飞船而不是rect对象的x值（因为rect.x只能储存整数）
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += 1
        #这里用的是if而非elif，因为可能同时按下左右键，以及使左右键优先级相同
        if self.moving_left == True and self.rect.left > 0:
            self.x -= 1

        #根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def ship_reborn(self):
        """(重新)生成在低端居中的飞船(非创建新实例)"""
        #对于每艘新飞船，都将其放在屏幕底端中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性中储存小数
        self.x = float(self.rect.x)
