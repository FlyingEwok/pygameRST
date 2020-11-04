import levelclass
import platformclass
import invisablehitmarkerclass
import enemyclass
import pygame

# Create platforms for the level
class Level_01(levelclass.Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
 
        self.level_limit = -1000
        screenHeight = pygame.display.get_surface().get_size()[1]

        # Place player
        player.rect.x = 340
        player.rect.y = screenHeight - player.rect.height
 
        # Array with width, height, x, and y of platform
        levelPlatform =[
                 [210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1120, 680]
                 ]

        levelHitMarker = [
                 [1, 140, 500, 360],
                 [1, 140, 709, 360]
                 ]

        enemyList = [
                [1, 1, 800, 520],
                [1, 1, 666, 550]
                ]
 
        self.addPlatforms(levelPlatform)
        self.addHitmarker(levelHitMarker)
        self.addEnemy(enemyList)

        
