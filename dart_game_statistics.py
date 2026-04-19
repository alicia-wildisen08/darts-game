class GameStatistics():
    """Class to manage the games statistics."""

    def __init__(self, dg):
        """Initialize statistics that can change during the game."""
        self.settings = dg.settings
        self.active = False
        self.highscore = 0 
        self.reset_stats()

    def reset_stats(self):
        """Statistics that change during the game and that you can reset."""
        self.tries = self.settings.max_missing 
        self.score = 0
        self.level = 1