import pygame.font

class PlayButton():
    """Overall class for the games buttons."""

    def __init__(self, dg, text):
        """Initialize attributes and the buttons characteristics.""" 
        self.screen = dg.screen
        self.screen_rect = self.screen.get_rect()

        # charecteristics of the play button
        self.play_width, self.play_height = 180, 60
        self.play_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.play_font = pygame.font.SysFont(None, 48)

        self.play_rect = pygame.Rect(0, 0, self.play_width, self.play_height)
        self.play_rect.center = self.screen_rect.center

        self._play_text(text)

    def _play_text(self, text):
        """Put text on the playbutton."""
        self.image = self.play_font.render(text, True, self.text_color,
                                           self.play_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.play_rect.center

    def draw_playbutton(self):
        """Draw the playbutton on the screen."""
        self.screen.fill(self.play_color, self.play_rect)
        self.screen.blit(self.image, self.image_rect)


        
class LevelButton():
    """Overall class for the games buttons."""

    def __init__(self, dg, text, color):
        """Initialize attributes and the buttons characteristics."""
        self.screen = dg.screen
        self.screen_rect = self.screen.get_rect()

        # characteristics of the level buttons
        self.level_width, self.level_height = 130, 40
        self.text_color = (255, 255, 255)
        self.level_font = pygame.font.SysFont(None, 30)

        self.level_rect = pygame.Rect(0, 0, self.level_width, self.level_height)
        self.level_rect.center = self.screen_rect.center

        self._level_text(text, color)

    def _level_text(self, text, color):
        """Put text on the playbutton."""
        self.image = self.level_font.render(text, True, self.text_color,
                                           color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.level_rect.center

    def draw_levelbutton(self, color):
        """Draw the playbutton on the screen."""
        self.screen.fill(color, self.level_rect)
        self.screen.blit(self.image, self.image_rect)