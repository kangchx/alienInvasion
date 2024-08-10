from __future__ import annotations
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

# The player-controlled Ship is different from Alien and Bullet
# The Ship will only be instantiated once throughout the entire game
class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game: AlienInvasion):
        """
        Initialize the ship and set its starting position.
        
        Args:
            ai_game (AlienInvasion): class of this game.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Spawn the ship
        self.ship_reborn()

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect (because rect.x can only store integers)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        # Using if instead of elif because both keys could be pressed simultaneously,
        # and to give equal priority to left and right movement
        if self.moving_left and self.rect.left > 0:
            self.x -= 1

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def ship_reborn(self):
        """(Re)spawn the ship at the bottom center of the screen (without creating a new instance)."""
        # Place the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
