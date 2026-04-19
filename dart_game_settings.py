class Settings():
    """Class to save the settings."""

    def __init__(self):
        """Initialize static settings."""
        # screen
        self.screen_w = 700
        self.screen_h = 600
        self.bg_color = (210, 210, 210)

        # darts-target
        self.target_w = 100
        self.target_h = 100
        self.target_red = (255, 0, 0)
        self.inner_w = 70
        self.inner_h = 70
        self.target_white = (255, 255, 255)
        self.middle_w = 40
        self.middle_h = 40

        # shooter point
        self.line_w = 4
        self.line_h = 15
        self.line_color = (0, 0, 0)

        # darts
        self.darts_w = 4
        self.darts_h = 15
        self.darts_color = (0, 0, 0)
        self.darts_limit = 4 # Amount you can use at the same time
        self.max_missing = 6 # Maximum amount you're allowed to miss

        # level button colors
        self.easy_color = (0, 180, 0)
        self.medium_color = (240, 130, 0)
        self.diffic_color = (210, 0, 0)

        # factor on how much faster the game gets
        self.level_up = 1.2

        # score for each time hitting the target
        self.score_hit = 50 

        # Level you can take or overwrite
        self.lvl = "easy"
        # Levels that get chosen for the game with the attribute above. 
        self.level_settings()


    def level_settings(self):
        """Settings for the game."""
        if self.lvl == "easy":
            self.point_speed = 1.5
            self.darts_speed = 2.2
            self.target_speed = 2.0
            self.target_direction = 1

        elif self.lvl == "medium":
            self.point_speed = 2.5
            self.darts_speed = 3.2
            self.target_speed = 3.0
            self.target_direction = 1
            
        elif self.lvl == "difficult":
            self.point_speed = 4.5
            self.darts_speed = 4.2
            self.target_speed = 4.0
            self.target_direction = 1

    def leveling_up(self):
        """Level up during the game."""
        self.point_speed *= self.level_up
        self.darts_speed *= self.level_up
        self.target_speed *= self.level_up