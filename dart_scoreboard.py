import pygame.font

class Scoreboard():
    """A class for the games scoreboard."""

    def __init__(self, dg):
        """Initialize attributes."""
        self.settings = dg.settings
        self.miss_darts = dg.missed_darts
        self.stats = dg.stats
        self.screen = dg.screen
        self.screen_rect = self.screen.get_rect()

        # characteristiscs of the scoreboard
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 34) 

        self.score_text()
        self.level_text() 
        self.missed_darts()
        self.highscore_text() 
    

    def highscore_text(self):
        """Show the highscore on screen."""
        highscore = self.stats.highscore
        highscore_str = f"highscore: {highscore:,}"
        self.highscore_image = self.font.render(highscore_str, True, 
                                    self.text_color, self.settings.bg_color)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.bottom = self.missed_rect.top
        self.highscore_rect.left = self.missed_rect.left

    def score_text(self):
        """Show the score bottom right on the screen."""
        self.score = f"score: {self.stats.score:,}"
        self.font_image = self.font.render(self.score, True, self.text_color,
                                           self.settings.bg_color)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.right = self.settings.screen_w - 40 
        self.font_rect.y = self.settings.screen_h - 80

    def level_text(self):
        """Show the level bottom right below score on the screen."""
        self.level = f"lvl: {self.stats.level}"
        self.level_image = self.font.render(self.level, True, self.text_color,
                                            self.settings.bg_color) 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.font_rect.bottom + 10
        self.level_rect.left = self.font_rect.left

    def missed_darts(self):
        """Show missed darts bottom left on the screen."""
        missed = len(self.miss_darts)
        text = f"missed: {missed}/{self.settings.max_missing}"
        self.missed_image = self.font.render(text, True, self.text_color, 
                                             self.settings.bg_color)
        self.missed_rect = self.missed_image.get_rect()
        self.missed_rect.bottom = self.level_rect.bottom
        self.missed_rect.left = self.screen_rect.left + 10


    def draw_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.font_image, self.font_rect) 
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.missed_image, self.missed_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)