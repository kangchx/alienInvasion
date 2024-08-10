import sys
import pygame
from time import sleep
from settings import Settings
from gameStats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreBoard import ScoreBoard
from screenStart import ScreenStart
from typing import Tuple
from pygame.event import Event

class AlienInvasion:
    """A class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""    
        self.settings = Settings()

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
        self.stats = GameStats(self)  # Create an instance to store game information
        self.sb = ScoreBoard(self)  # Scoreboard instance
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()

        self._create_ships_show()
        # self._create_fleet()  # If present, alien ships are displayed on the initial interface

        # Create button instances
        self.play_button = Button(self, "Play")
        self.pause_button = Button(self, "Continue")

    def run(self):
        """Start the main process."""
        self._run_start_screen()
        self._run_game()

    def _run_start_screen(self):
        """Start the initial interface loop."""
        screen_start = ScreenStart(self)
        while not self._check_start_screen_events():
            self.screen.fill(self.settings.bg_color)
            screen_start.screen_start_draw()
            pygame.display.flip()

    def _run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            
            if self.stats.game_active and not self.stats.game_pause:
                self.ship.update()
                self._update_bullets()
                self._check_bullet_aliens_collisions()
                self._update_aliens()
                self._check_ship_aliens_collisions()
                self._check_aliens_bottom()

            self._update_screen()

    def _check_start_screen_events(self):
        """Respond to start screen events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit(0)
                else:
                    return True

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_press_button(mouse_pos)

    def _check_press_button(self, mouse_pos: Tuple[float, float]):
        """
        Respond to button clicks.
        
        Args:
            mouse_pos (tuple): The x and y coordinates of the mouse click.
        """
        if self.play_button.rect.collidepoint(mouse_pos):
            # (Re)start the game
            if not self.stats.game_active: 
                self._game_restart()
            # Continue the game
            elif self.stats.game_pause == True:
                self.stats.game_pause = False
                pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event: Event):
        """
        Respond to keypresses.
        
        Args:
            event (Event): keyboard events.
        """
        # Control ship's left-right movement
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Quit game
        elif event.key == pygame.K_q:
            sys.exit(0)
        # Fire bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # Pause game
        elif event.key == pygame.K_p:
            self.stats.game_pause = True
            pygame.mouse.set_visible(True)
        # (Re)start game
        elif event.key == pygame.K_s:
            if not self.stats.game_active: 
                self._game_restart()
        # Continue game
        elif event.key == pygame.K_c:
            if self.stats.game_pause == True:
                self.stats.game_pause = False
                pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event: Event):
        """
        Respond to key releases.
        
        Args:
            event (Event): keyboard events.
        """
        # Control ship's left-right movement
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions."""
        # Update bullet positions
        self.bullets.update()
        # Remove disappeared bullets
        for bullet in self.bullets.copy():  # Note that we're using a copy here
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            else:
                break
        # print(len(self.bullets))

    def _check_bullet_aliens_collisions(self):
        """Check for any bullets that have hit aliens."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            # Score
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Remove existing bullets and create new fleet, also speed up
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_ship_aliens_collisions(self):
        """Check for collisions between aliens and the ship."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._game_reborn()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_bottom():
                self._game_reborn()
                break

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.alien_drop()
        self.settings.fleet_direction *= -1

    def _characters_empty(self):
        """Empty the remaining aliens, bullets, and ships groups."""
        self.aliens.empty()
        self.bullets.empty()
        self.ships.empty()

    def _characters_create(self):
        """Create aliens, ship, and ships group."""
        self._create_fleet()
        self.ship.ship_reborn()
        self._create_ships_show()

    def _characters_reborn(self):
        """Regenerate the ship, aliens, and the ships group to be displayed."""
        self._characters_empty()
        self._characters_create()

    def _game_reborn(self):
        """Decide whether the game should continue."""
        if self.stats.ships_left > 1:
            # Respawn ship, game continues            
            self.stats.ships_left -= 1
            self._characters_reborn()
            sleep(0.5)
        else:
            # Game over
            self._characters_empty()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            sleep(1)
    
    def _game_restart(self):
        """Restart the game."""
        self.settings.initialize_dynamic_settings()  # Reset game settings
        self.stats.reset_stats()  # Reset game statistics
        self.sb.prep_score()  # Reset score
        self.sb.prep_level()  # Reset level
        self.stats.game_active = True
        self._characters_reborn()
        # self._characters_create()  # Using reborn here is more error-tolerant than create
        pygame.mouse.set_visible(False)

    def _update_screen(self): 
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ships.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        elif self.stats.game_pause:
            self.pause_button.draw_button()

        pygame.display.flip()  # Update the screen

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row and column
        # Spacing between each alien is equal to one alien width and height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        aliens_start_x = (self.settings.screen_width - (2 * number_aliens_x - 1)
                          * alien_width) / 2

        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - self.ship.rect.height)
        number_aliens_y = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_aliens_y):
            for col_number in range(number_aliens_x):
                self._create_alien(row_number, col_number, aliens_start_x)

    def _create_alien(self, row_number: int, col_number: int, aliens_start_x: float):
        """
        Create an alien and place it in the fleet.

        Args:
            row_number (int): The row number for the alien's position.
            col_number (int): The column number for the alien's position.
            aliens_start_x (float): The starting x-coordinate for the fleet.
        """

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = aliens_start_x + 2 * alien_width * col_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_ships_show(self):
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
