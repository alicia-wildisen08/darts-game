import pygame

class ShooterPoint():
    """Make a class for the point where you shoot the darts."""

    def __init__(self, dg):
        """Initialize attributes."""
        self.settings = dg.settings
        self.screen = dg.screen
        self.screen_rect = self.screen.get_rect()

        self.line_rect = pygame.Rect(0, 0, self.settings.line_w,
                                     self.settings.line_h)
        
        self.line_rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False 

        self.line_x = float(self.line_rect.x)

    def draw_shooting_point(self):
        """Draw the shooting point on the screen."""
        self.screen.fill(self.settings.line_color, self.line_rect)

    def moving_point(self):
        """Moving the shooting point."""        
        if self.line_rect.right <= (self.settings.screen_w - 10)and self.moving_right:
            self.line_x += self.settings.point_speed
        if self.line_rect.left >= 10 and self.moving_left:
            self.line_x -= self.settings.point_speed

        self.line_rect.x = self.line_x

    def center_shooting_point(self):
        """Center the shooting point after restarting the game."""
        self.line_rect.midbottom = self.screen_rect.midbottom
        self.line_x = float(self.line_rect.x)