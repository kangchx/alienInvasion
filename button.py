from __future__ import annotations
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class Button:
    """The Buttion class, with message shown on it."""
    def __init__(self, ai_game: AlienInvasion, msg: str):
        """
        Initialize button attributes.
        
        Args:
            ai_game (AlienInvasion): class of this game.
            msg (str): message to show on the button.
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create a rect object for the button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Create the button
        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        """
        Render msg as an image and center it on the button.
        
        Args:
            msg (str): message to show on the button.
        """
        self.msg_image = self.font.render(msg, True, self.text_color,  self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw a button filled with color, then draw text."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)   
