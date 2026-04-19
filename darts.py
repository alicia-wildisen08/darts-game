import pygame
from pygame.sprite import Sprite

class Darts(Sprite):
    """A class for the darts."""

    def __init__(self, dg):
        """Initialize attributes."""
        super().__init__()

        self.settings = dg.settings
        self.screen = dg.screen
        
        self.shooting_point = dg.shooter_point.line_rect

        self.dart = pygame.Rect(0, 0, self.settings.darts_w,
                                self.settings.darts_h)
        
        self.dart.center = self.shooting_point.center

        self.y = float(self.dart.y)

    def draw_dart(self):
        """Draw the darts on the screen."""
        self.screen.fill(self.settings.darts_color, self.dart)

    def update(self):
        """Move the darts along the y-axis after shooting them."""
        self.y -= self.settings.darts_speed 
        self.dart.y = self.y