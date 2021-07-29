import pygame.font
import pygame

class ScreenStart:
    """初始界面的类"""

    def __init__(self, ai_game):
        """初始化初始界面设置"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        text_color = (0, 0, 255)
        font = pygame.font.SysFont(None, 48)

        screen_start_strs = list()
        screen_start_strs_widths = list()
        self.screen_start_strs_hights = list()
        self.screen_start_strs_hight = 0
        self.screen_start_images = list()

        screen_start_strs.append('Welcome to game "Alien Invasion"')
        screen_start_strs.append('Press "<" or ">" to control the ship')
        screen_start_strs.append('Press key "Q" to quit')
        screen_start_strs.append('Press key "S" or button "Play" to start')
        screen_start_strs.append('Press key "p" to pause')
        screen_start_strs.append('Press key "c" or button "continue" to continue')

        for screen_start_str in screen_start_strs:
            screen_start_image = font.render(screen_start_str, True,
                                            text_color, self.settings.bg_color)
            screen_start_rect = screen_start_image.get_rect()
            screen_start_strs_widths.append(screen_start_rect.width)
            self.screen_start_strs_hights.append(screen_start_rect.height)
            self.screen_start_images.append(screen_start_image)

        self.screen_start_strs_width = max(screen_start_strs_widths)
        self.screen_start_strs_hight = sum(self.screen_start_strs_hights)


    def screen_start_draw(self):
        """显示初始界面"""
        screen_start_image = self.screen_start_images[0]

        screen_start_rect = screen_start_image.get_rect()

        screen_start_x = (self.settings.screen_width - self.screen_start_strs_width) // 2
        screen_start_y = (self.settings.screen_heignt - self.screen_start_strs_hight) // 2

        screen_start_rect.x = screen_start_x
        screen_start_rect.y = screen_start_y

        self.screen.blit(screen_start_image, screen_start_rect)

        i=0

        for screen_start_image in self.screen_start_images[1:]:
            screen_start_rect.y += self.screen_start_strs_hights[i]
            i += 1
            self.screen.blit(screen_start_image, screen_start_rect)