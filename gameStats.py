from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alienInvasion import AlienInvasion

class GameStats:
    """Track statistics for the game."""

    def __init__(self, ai_game: AlienInvasion):
        """
        Initialize static statistics.
        
        Args:
            ai_game (AlienInvasion): class of this game.
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # The game starts in an inactive state, but also not paused
        self.game_active = False
        self.game_pause = False

        # High score should never be reset to 0
        self.high_score = 0

    def reset_stats(self):
        """Initialize dynamic statistics."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1