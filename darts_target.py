import pygame

class DartTarget():
    """Class for the darts target."""

    def __init__(self, dg):
        """Initialize attributes."""
        self.settings = dg.settings
        self.screen = dg.screen
        self.screen_rect = self.screen.get_rect()

        self.outer_rect = pygame.Rect(0, 0, self.settings.target_w,
                                      self.settings.target_h)
        self.middle_rect = pygame.Rect(0, 0, self.settings.inner_w,
                                        self.settings.inner_h)
        self.inner_rect = pygame.Rect(0, 0, self.settings.middle_w,
                                      self.settings.middle_h)
        
        self.outer_rect.midtop = self.screen_rect.midtop
        self.outer_rect.y += 10

        self.middle_rect.center = self.outer_rect.center
        self.inner_rect.center = self.middle_rect.center

        self.outer_x = float(self.outer_rect.x)
        self.middle_x = float(self.middle_rect.x)
        self.inner_x = float(self.inner_rect.x)

    def draw_target(self):
        """Draw the target on screen."""
        self.screen.fill(self.settings.target_red, self.outer_rect)
        self.screen.fill(self.settings.target_white, self.middle_rect)
        self.screen.fill(self.settings.target_red, self.inner_rect)

    def moving_target(self):
        """Move the target."""
        if self.outer_rect.right >= self.settings.screen_w or self.outer_rect.left <= 0:
            self.settings.target_direction *= -1

        self.outer_x += self.settings.target_speed * self.settings.target_direction
        self.middle_x += self.settings.target_speed * self.settings.target_direction
        self.inner_x += self.settings.target_speed * self.settings.target_direction

        self.outer_rect.x = self.outer_x
        self.middle_rect.x = self.middle_x
        self.inner_rect.x = self.inner_x

    def center_target(self):
        """Center the target after restarting the game."""
        self.outer_rect.midtop = self.screen_rect.midtop
        self.outer_rect.y += 10

        self.middle_rect.center = self.outer_rect.center
        self.inner_rect.center = self.middle_rect.center

        self.outer_x = float(self.outer_rect.x)
        self.middle_x = float(self.middle_rect.x)
        self.inner_x = float(self.inner_rect.x)