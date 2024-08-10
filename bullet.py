from __future__ import annotations
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game: AlienInvasion):
        """Create a bullet object at the ship's current position."""
        super().__init__()  # Use Sprite to allow the bullet instance to be grouped for unified management
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upward."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    # Note the difference from the Alien class, which is also a sprite.
    # Although both are sprites, Alien uses an image, so the default draw method can be used.
    # Bullet, however, is different. It requires custom drawing, so the group's draw method cannot be used.
    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
