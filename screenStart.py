from __future__ import annotations
import pygame.font
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class ScreenStart:
    """Class for the initial screen."""

    def __init__(self, ai_game: AlienInvasion):
        """
        Initialize the initial screen settings.
        
        Args:
            ai_game (AlienInvasion): class of this game.
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.screen_start_strs = list()
        self.screen_start_strs_heights = list()
        self.screen_start_images = list()

        self._create_strs()
        self._prep_strs_images()
        self._calculate_str_Rect()

    def screen_start_draw(self):
        """Display the initial screen."""
        # Reset y position each time as it changes, unlike x
        self.screen_start_rect.y = self.screen_start_y
        self.screen.blit(self.screen_start_image, self.screen_start_rect)
        i = 0
        for screen_start_image in self.screen_start_images[1:]:
            self.screen_start_rect.y += self.screen_start_strs_heights[i]
            i += 1
            self.screen.blit(screen_start_image, self.screen_start_rect)

    def _create_strs(self):
        """Create text for the initial screen."""
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
        """Render text as images and prepare for Rect calculation."""
        screen_start_strs_widths = list()

        for screen_start_str in self.screen_start_strs:
            screen_start_image = self.font.render(screen_start_str, True,
                                            self.text_color, self.settings.bg_color)
            screen_start_strs_widths.append(screen_start_image.get_width())
            self.screen_start_strs_heights.append(screen_start_image.get_height())
            self.screen_start_images.append(screen_start_image)

        self.screen_start_strs_width = max(screen_start_strs_widths)
        self.screen_start_strs_height = sum(self.screen_start_strs_heights)

    def _calculate_str_Rect(self):
        """Calculate the Rect for the text images."""
        self.screen_start_image = self.screen_start_images[0]
        self.screen_start_rect = self.screen_start_image.get_rect()

        screen_start_x = (self.settings.screen_width - self.screen_start_strs_width) // 2
        self.screen_start_y = (self.settings.screen_height - self.screen_start_strs_height) // 2

        self.screen_start_rect.x = screen_start_x