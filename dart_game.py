import pygame
import sys
from pygame.sprite import Group
from pathlib import Path

from dart_game_settings import Settings
from shooter_point import ShooterPoint
from darts_target import DartTarget
from darts import Darts
from dart_game_statistics import GameStatistics
import dart_game_button as dgb
from dart_scoreboard import Scoreboard


class DartGame():
    """Overall class of the game (mainclass)."""

    def __init__(self):
        """Initialize attributes in the mainclasss."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,
                                               self.settings.screen_h))
        pygame.display.set_caption("Darts game!")

        self.stats = GameStatistics(self)
        self.missed_darts = Group()
        self.scoreboard = Scoreboard(self)

        self.shooter_point = ShooterPoint(self)
        self.target = DartTarget(self)
        self.darts = pygame.sprite.Group() 

        self.play_button = dgb.PlayButton(self, "Play")
        self._level_buttons()

    def _level_buttons(self):
        """Set up the level buttons."""
        self.easy_button = dgb.LevelButton(self, "Easy", self.settings.easy_color)
        self.easy_button.level_rect.y += 60
        self.easy_button.image_rect.y += 60

        self.medium_button = dgb.LevelButton(self, "Medium", 
                                        self.settings.medium_color)
        self.medium_button.level_rect.y += 110
        self.medium_button.image_rect.y += 110

        self.diffic_button = dgb.LevelButton(self, "Difficult", 
                                        self.settings.diffic_color)
        self.diffic_button.level_rect.y += 160 
        self.diffic_button.image_rect.y += 160


    def run_game(self):
        """Mainmethod => run the game."""
        while True:
            self._check_events()
            if self.stats.active:
                self.shooter_point.moving_point() 
                for dart in self.darts: 
                    dart.update()  
                self._collision() 
                self.target.moving_target() 
            self._update_screen() 
            self.clock.tick(60)


    def _check_events(self):
        """Act based on key- and mouse-events."""
        for event in pygame.event.get():
            # saving highscore and closing the game.
            if event.type == pygame.QUIT:
                self._saving_highscore()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # saving highscore and closing the game.
                if event.key == pygame.K_q: 
                    self._saving_highscore() 
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._make_dart()
                elif event.key == pygame.K_RIGHT:
                    self.shooter_point.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.shooter_point.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.shooter_point.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.shooter_point.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._mouse_activity(mouse_pos)
    
    def _mouse_activity(self, mouse_pos):
        """Take action based on mouse activity."""
        if self.play_button.play_rect.collidepoint(mouse_pos):
            self._start_game() 
        elif self.easy_button.level_rect.collidepoint(mouse_pos):
            self.settings.lvl = "easy"
        elif self.medium_button.level_rect.collidepoint(mouse_pos):
            self.settings.lvl = "medium"
        elif self.diffic_button.level_rect.collidepoint(mouse_pos):
            self.settings.lvl = "difficult"

    def _start_game(self):
        """Start the game with reseted statistics."""
        self.settings.level_settings() 

        self.darts.empty()
        self.missed_darts.empty() 
        self.stats.reset_stats()
        self.scoreboard.score_text() 
        self.scoreboard.level_text()
        self.target.center_target()
        self.shooter_point.center_shooting_point() 
        pygame.mouse.set_visible(False)
        self.stats.active = True

    def _make_dart(self):
        """Make a dart."""
        if len(self.darts) < self.settings.darts_limit:
            new_dart = Darts(self)
            self.darts.add(new_dart) 
    
    def _collision(self):
        """Take specific action based on collisions."""
        for dart in self.darts.copy():
            shoot = pygame.Rect.colliderect(self.target.outer_rect, 
                                                dart.dart)
            if shoot:
                self.darts.remove(dart) 
                self.settings.leveling_up() 
                self.stats.level += 1
                self.stats.score += self.settings.score_hit
                self.scoreboard.score_text()
                self.scoreboard.level_text()
                # checking for new highscore
                if self.stats.score > self.stats.highscore:
                    self.stats.highscore = self.stats.score
                    self.scoreboard.highscore_text()

            # When you miss the target
            self._missing_target(dart)

    def _missing_target(self, dart):
        """Take action after missing the target."""
        if self.stats.tries > 0:
            if dart.dart.bottom <= 0:
                self.darts.remove(dart) 
                self.stats.tries -= 1
                self.missed_darts.add(dart) 
                self.scoreboard.missed_darts() 
        else:
            self.stats.active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """Update the screen."""
        self.screen.fill(self.settings.bg_color)
        self.shooter_point.draw_shooting_point() 
        self.target.draw_target() 
        for dart in self.darts: 
            dart.draw_dart()
        self.scoreboard.draw_score() 
        if not self.stats.active:
            self.play_button.draw_playbutton()
            self.easy_button.draw_levelbutton(self.settings.easy_color)
            self.medium_button.draw_levelbutton(self.settings.medium_color)
            self.diffic_button.draw_levelbutton(self.settings.diffic_color) 
        pygame.display.flip()

    def reading_highscore(self):
        """Reading saved highscore in."""
        path = Path("saving_highscore.txt")
        h_score = path.read_text(encoding="utf-8")
        h_str = int(h_score)
        self.stats.highscore = h_str
        self.scoreboard.highscore_text() 

    def _saving_highscore(self):
        """Saving highscore after closing the game."""
        path = Path("saving_highscore.txt")
        h_str = str(self.stats.highscore)
        path.write_text(h_str)



if __name__ == "__main__":
    dg = DartGame()
    dg.reading_highscore() 
    dg.run_game() 