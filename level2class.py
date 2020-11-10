import levelclass
import pygame

# Create platforms for the level
class Level_02(levelclass.Level):
    """ Definition for level 2. """
    
    def create(self):        
        super(Level_02, self).create()

        ## Players x and y position
        playerStartX = 340
        playerStartY = 520

        # place player
        self.placePlayer(playerStartX, playerStartY)

        # Create background
        self.background = pygame.image.load('images/SpaceBackgroundWithGlass.png')
 
        # Array with width, height, x, and y of platform
        self.levelPlatform = [
                 [1, 720, 0, 0],
                 [210, 20, 440, 450],
                 [210, 20, 0, 250]
                 ]

        self.levelHitMarker = [
                 [1, 140, 440, 310],
                 [1, 140, 650, 310]
                 ]

        self.levelFloor = [
                 [self.getBackgroundWidth() + 20, 20, 0, 581],
                 [self.getBackgroundWidth(), 20, 0, -20]
                 ]

        self.enemyList = [
                
                ]

        self.levelGravitySwitch = [
                
                ]

        self.levelGateway = [
                [60, self.screenHeight, self.getBackgroundWidth(), 0]
                ]

        self.levelKey = [
                
        ]
 
        self.addPlatforms(self.levelPlatform)
        self.addHitmarker(self.levelHitMarker)
        self.addFloor(self.levelFloor)
        self.addGateway(self.levelGateway)
        self.addKey(self.levelKey)
        self.addEnemy(self.enemyList)
        self.addSwitch(self.levelGravitySwitch)

    def __init__(self, player):
        """ Create level 2. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)