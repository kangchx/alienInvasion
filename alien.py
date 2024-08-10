from __future__ import annotations
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class Alien(Sprite):
    """A class representing a single alien."""

    def __init__(self, ai_game: AlienInvasion, x: float | None = 0.0, y: float | None = 0.0):
        """
        Initialize the alien and set its starting position.
        
        Args:
            ai_game (AlienInvasion): class of this game.
            x (float): x of the position of the Alien.
            y (float): y of the position of the Alien.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its initial position
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Store the alien's exact position
        self.x = float(x)  # float() ensures it's a float type
        self.y = float(y)

        # Each alien initially starts near the top left of the screen
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed_x * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Check if the alien is at the edge of the screen horizontally, return `True` if so."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def check_bottom(self):
        """Check if the alien has reached the bottom, return `True` if so."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def alien_drop(self):
        """Move downwards."""
        self.y += self.settings.alien_speed_y
        self.rect.y = self.y