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
                 [210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1120, 680]
                 ]

        self.levelHitMarker = [
                 [1, 140, 500, 360],
                 [1, 140, 709, 360]
                 ]

        self.enemyList = [
                [1, 1, 800, 520],
                [1, 1, 666, 550]
                ]
 
        self.addPlatforms(self.levelPlatform)
        self.addHitmarker(self.levelHitMarker)
        self.addEnemy(self.enemyList)

    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
        self.level_limit = -1000
        

        
