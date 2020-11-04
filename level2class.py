import platformclass
import levelclass

# Create platforms for the level
class Level_02(levelclass.Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
 
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280],
                 ]
 
        self.addPlatforms(level)