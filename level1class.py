import levelclass
import platformclass
import invisablehitmarkerclass
import enemyclass
import pygame

# Create platforms for the level
class Level_01(levelclass.Level):
    """ Definition for level 1. """
    
    def create(self):        
        # Call the base class create function
        super(Level_01, self).create()

        # Players x and y position
        playerStartX = 340
        playerStartY = self.screenHeight - self.player.rect.height

        # place player
        self.placePlayer(playerStartX, playerStartY)

        # Create background
        self.background = pygame.image.load('images/SpaceBackground.png')
 
        # Array with width, height, x, and y of platform
        self.levelPlatform =[
                 [1, 720, 0, 0],
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
        
        

        
