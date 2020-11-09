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
        playerStartY = 520

        # place player
        self.placePlayer(playerStartX, playerStartY)

        # Create background
        self.background = pygame.image.load('images/SpaceBackgroundWithGlass.png')
 
        # Array with width, height, x, and y of platform
        self.levelPlatform =[
                 [1, 720, 0, 0],
                 [210, 20, 800, 440],
                 [210, 20, 1120, 300],
                 [20, 150, 1550, 200],
                 [420, 20, 1570, 330],
                 [20, 150, 1990, 200],
                 [210, 20, 2500, 440],
                 [210, 20, 2900, 100],
                 [210,20, 3200, 220]
                 ]

        self.levelHitMarker = [
                 [1, 140, 800, 300],
                 [1, 140, 1009, 300],
                 [1, 140, 1120, 160],
                 [1, 140, 1328, 160],
                 [1, 140, 2500, 300],
                 [1, 140, 2709, 300],
                 [1, 140, 1990, 440],
                 [1, 140, 2500, 440]
                 ]

        self.levelFloor = [
                 [self.getBackgroundWidth(), 20, 0, 581],
                 [self.getBackgroundWidth(), 20, 0, -20]
                 ]

        self.enemyList = [
                [800, 500],
                [666, 500],
                [2000, 580],
                [2200, 580],
                [2400, 580],
                [2300, 580],
                [2100, 580],
                [2050, 580],
                [2150, 580],
                [2250, 580],
                [2350, 580],
                [2450, 580],
                [1560, 200],
                [1600, 200],
                [1660, 200],
                [1700, 200],
                [1760, 200],
                [1800, 200],
                [1860, 200],
                [1900, 200],
                [380, 580],
                [420, 580],
                [580, 580],
                [620, 580],
                [880, 580],
                [900, 440],
                [1121, 300],
                [2501, 440]
                ]

        self.levelGravitySwitch = [
                [10, 10, 2670, 430],
                [10, 10, 3400, 240]

                ]

        self.levelGateway = [
                [60, self.screenHeight, self.getBackgroundWidth(), 0]
        ]
 
        self.addPlatforms(self.levelPlatform)
        self.addHitmarker(self.levelHitMarker)
        self.addFloor(self.levelFloor)
        self.addGateway(self.levelGateway)
        self.addEnemy(self.enemyList)
        self.addSwitch(self.levelGravitySwitch)

    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
        
        

        
