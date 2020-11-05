import levelclass
import platformclass
import invisablehitmarkerclass
import enemyclass
import pygame

# Create platforms for the level
class Level_01(levelclass.Level):
    """ Definition for level 1. """
    
    def create(self):
        print("Level 1 create")

        super(Level_01, self).create()

        screenHeight = pygame.display.get_surface().get_size()[1]

        # Place player
        self.player.rect.x = 340
        self.player.rect.y = screenHeight - self.player.rect.height
 
        # Array with width, height, x, and y of platform
        self.levelPlatform =[
                 [210, 20, 500, 520],
                 [210, 20, 800, 440],
                 [210, 20, 1000, 560],
                 [210, 20, 1120, 300],
                 [210, 20, 1120, 700]
                 ]

        self.levelHitMarker = [
                 [1, 140, 500, 380],
                 [1, 140, 709, 380]
                 ]

        self.enemyList = [
                [800, 500],
                [666, 500]
                ]
 
        self.addPlatforms(self.levelPlatform)
        self.addHitmarker(self.levelHitMarker)
        self.addEnemy(self.enemyList)

    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
        self.level_limit = -1000
        

        
