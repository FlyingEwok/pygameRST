import levelclass
import platformclass
import invisablehitmarkerclass
import enemyclass
import pygame

# Create platforms for the level
class Level_02(levelclass.Level):
    """ Definition for level 2. """
    
    def create(self):        
        super(Level_02, self).create()

        ## Players x and y position
        playerStartX = 340
        playerStartY = self.screenHeight - self.player.rect.height

        # place player
        self.placePlayer(playerStartX, playerStartY)

        # Create background
        self.background = pygame.image.load('images/Test-Background.png')
 
        # Array with width, height, x, and y of platform
        self.levelPlatform =[
                 [2, 720, 0, 0],
                 [210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280],
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
        """ Create level 2. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)