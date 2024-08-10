from __future__ import annotations
import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class ScoreBoard:
    """A class to display score information."""

    def __init__(self, ai_game: AlienInvasion):
        """Initialize attributes related to displaying the score."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for displaying the score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Render the current score as an image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            score_str, 
            True,
            self.text_color, self.settings.bg_color
        )

        # Display the current score in the top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render the high score as an image."""
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, 
            True,
            self.text_color, 
            self.settings.bg_color
        )

        # Display the high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Render the level as an image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, 
            True,
            self.text_color, 
            self.settings.bg_color
        )

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Display the score information on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Check if there is a new high score and update it if there is."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
