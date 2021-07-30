import pygame.font
import pygame
from time import sleep

class ScreenStart:
    """初始界面的类"""

    def __init__(self, ai_game):
        """初始化初始界面设置"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.screen_start_strs = list()
        self.screen_start_strs_hights = list()
        self.screen_start_images = list()

        self._create_strs()
        self._prep_strs_images()
        self._calculate_str_Rect()

    def screen_start_draw(self):
        """显示初始界面"""
        self.screen_start_rect.y = self.screen_start_y#因为 y 与 x 不同，会发生改变所以每次重绘时需重置
        self.screen.blit(self.screen_start_image, self.screen_start_rect)
        i=0
        for screen_start_image in self.screen_start_images[1:]:
            self.screen_start_rect.y += self.screen_start_strs_hights[i]
            i += 1
            self.screen.blit(screen_start_image, self.screen_start_rect)

    def _create_strs(self):
        """创建初始界面文本"""
        self.screen_start_strs.append('Welcome to game "Alien Invasion"!!!')
        self.screen_start_strs.append(' ')
        self.screen_start_strs.append('Press "<" or ">" to control the ship')
        self.screen_start_strs.append('Press key "Q" to quit')
        self.screen_start_strs.append('Press key "S" or button "Play" to start')
        self.screen_start_strs.append('Press key "P" to pause')
        self.screen_start_strs.append('Press key "C" or button "continue" to continue')
        self.screen_start_strs.append('')
        self.screen_start_strs.append('Press any key but "Q" to skip the Guiding Screen')

    def _prep_strs_images(self):
        """将文字渲染为图像，并为计算Rect做准备"""
        screen_start_strs_widths = list()

        for screen_start_str in self.screen_start_strs:
            screen_start_image = self.font.render(screen_start_str, True,
                                            self.text_color, self.settings.bg_color)
            screen_start_strs_widths.append(screen_start_image.get_width())
            self.screen_start_strs_hights.append(screen_start_image.get_height())
            self.screen_start_images.append(screen_start_image)

        self.screen_start_strs_width = max(screen_start_strs_widths)
        self.screen_start_strs_hight = sum(self.screen_start_strs_hights)

    def _calculate_str_Rect(self):
        """计算字符图像的 Rect"""
        self.screen_start_image = self.screen_start_images[0]
        self.screen_start_rect = self.screen_start_image.get_rect()

        screen_start_x = (self.settings.screen_width - self.screen_start_strs_width) // 2
        self.screen_start_y = (self.settings.screen_heignt - self.screen_start_strs_hight) // 2

        self.screen_start_rect.x = screen_start_x
        #self.screen_start_rect.y = self.screen_start_y