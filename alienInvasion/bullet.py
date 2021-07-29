import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射子弹的类"""

    def __init__(self, ai_game):
        """在飞船当前位置创造子弹对象"""
        super().__init__()#利用sprite使子弹实例可以被编组，进而统一管理
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #创建子弹
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y -=self.settings.bullet_speed
        self.rect.y = self.y

    #注意与Alien类的不同，虽然都是精灵，但是Alien是image，所以可用缺省的draw
    #而Bullet不同，需要自己绘制，因此不能对组统一调用绘制的方法
    def draw_bullet(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)