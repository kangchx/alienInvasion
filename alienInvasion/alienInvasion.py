import sys
from time import sleep
import pygame

from settings import Settings
from gameStats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreBoard import ScoreBoard
from screenStart import ScreenStart

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""    
        self.settings = Settings()

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_heignt))
        pygame.display.set_caption("Alien Invasion")
    
        self.stats = GameStats(self)#创建一个用于存储游戏信息的实例
        self.sb = ScoreBoard(self)#记分牌实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()

        self._create_ships_show()
        #self._create_fleet()有则在初始界面上显示外星人飞船，反之则无

        #创建按钮实例
        self.play_button = Button(self, "Play")
        self.pause_button = Button(self, "Continue")

    def run_game(self):
        """开始游戏的主循环"""
        screen_start = ScreenStart(self)
        self.screen.fill(self.settings.bg_color)
        screen_start.screen_start_draw()
        pygame.display.flip()
        sleep(10)
        while True:
            self._check_events()
            
            if self.stats.game_active and not self.stats.game_pause:
                self.ship.update()
                self._update_bullets()
                self._check_bullet_alliens_collisions()
                self._update_aliens()
                self._check_ship_aliens_collisions()
                self._check_aliens_bottom()

            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
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

    def _check_press_button(self, mouse_pos):
        """响应单击按钮"""
        if self.play_button.rect.collidepoint(mouse_pos):
            #(重新)开始游戏
            if not self.stats.game_active: 
                self._game_restart()
            #继续游戏
            elif self.stats.game_pause == True:
                self.stats.game_pause = False
                pygame.mouse.set_visible(False)

    def _check_keydown_events(self,event):
        """响应键盘按下"""
        #控制飞船左右行动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #退出游戏
        elif event.key == pygame.K_q:
            sys.exit(0)
        #发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #暂停游戏
        elif event.key == pygame.K_p:
            self.stats.game_pause = True
            pygame.mouse.set_visible(True)
        #(重新)开始游戏
        elif event.key == pygame.K_s:
            if not self.stats.game_active: 
                self._game_restart()
        #继续游戏
        elif event.key == pygame.K_c:
            if self.stats.game_pause == True:
                self.stats.game_pause = False
                pygame.mouse.set_visible(False)

    def _check_keyup_events(self,event):
        """响应键盘松开"""
        #控制飞船左右行动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹情况"""
        #更新子弹位置
        self.bullets.update()
        #删除消失的子弹
        for bullet in self.bullets.copy():#注意这里用的是copy
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            else:
                break
        #print(len(self.bullets))

    def _check_bullet_alliens_collisions(self):
        """检查子弹击落外星人情况"""
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)

        if collisions:
            #计分
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #删除现有子弹，并新建外星人，同时加速
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_ship_aliens_collisions(self):
        """检测外星人和飞船之间的碰撞"""
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._game_reborn()

    def _check_aliens_bottom(self):
        """有外星人到达低端时的措施"""
        for alien in self.aliens.sprites():
            if alien.check_bottom():
                self._game_reborn()
                break

    def _check_fleet_edges(self):
        """有外星人到达水平边缘时采取的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变移动方向"""
        for alien in self.aliens.sprites():
            alien.alien_drop()
        self.settings.fleet_direction *= -1

    def _characters_empty(self):
        """清空余下的外星人和子弹和飞船编组"""
        self.aliens.empty()
        self.bullets.empty()
        self.ships.empty()

    def _characters_create(self):
        """创建外星人和飞船和飞船编组"""
        self._create_fleet()
        self.ship.ship_reborn()
        self._create_ships_show()

    def _characters_reborn(self):
        """重新生成飞船与外星人和用来被显示的飞船编组"""
        self._characters_empty()
        self._characters_create()

    def _game_reborn(self):
        """判断游戏是否继续进行"""
        if self.stats.ships_left > 1:
            #重生飞船，游戏继续            
            self.stats.ships_left -= 1
            self._characters_reborn()
            sleep(0.5)
        else:
            #游戏结束
            self._characters_empty()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            sleep(1)
    
    def _game_restart(self):
        """游戏重新开始"""
        self.settings.initialize_dynamic_settings()#重置游戏设置
        self.stats.reset_stats()#重置游戏统计信息
        self.sb.prep_score()#重置得分
        self.sb.prep_level()#重置等级
        self.stats.game_active = True
        self._characters_reborn()
        #self._characters_create()这里用reborn比create容错率更好
        pygame.mouse.set_visible(False)

    def _update_screen(self): 
        """更新屏幕图像，并切换到新屏幕"""
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

        pygame.display.flip()#更新屏幕

    def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人并计算一行和一列能够容纳多少个外星人
        #外星人间距为外星人宽度和高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        aliens_start_x = (self.settings.screen_width - (2 * number_aliens_x - 1)
                          * alien_width) / 2

        available_space_y = (self.settings.screen_heignt -
                                (3 * alien_height) - self.ship.rect.height)
        number_aliens_y = available_space_y // (2 * alien_height)

        #创建外星人群
        for row_number in range(number_aliens_y):
            for col_number in range(number_aliens_x):
                self._create_alien(row_number, col_number, aliens_start_x)

    def _create_alien(self, row_number, col_number, aliens_start_x):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = aliens_start_x + 2 * alien_width * col_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_ships_show(self):
        for ship_number in range(self.stats.ships_left):
            ship =Ship(self)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

if __name__ == '__main__':
    #创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()