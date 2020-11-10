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
                 [1280, 20, 0, 375],
                 [2360, 20 ,0, 275],
                 [20, 185, 2340, 295],
                 [200, 20, 2360, 460],
                 [10, 580, 0,  0],
                 [200, 20, 2710, 310],
                 [730, 20, 3110, 210],
                 [10, 210, 3830, 0],
                 [200, 20, 2760, 100],
                 [50, 20, 2610, 350]
                 ]

        self.levelHitMarker = [
                 [1, 285, 1279, 295],
                 [1, 285, 2559, 295],
                 [1, 60, 2710, 250],
                 [1, 60, 2909, 250],
                 [1, 60, 3110, 150],
                 [1, 275, 2359, 0]
                 ]

        self.levelFloor = [
                 [self.getBackgroundWidth() + 20, 20, 0, 581],
                 [self.getBackgroundWidth(), 20, 0, -20]
                 ]

        self.enemyList = [
                [1386, 530],
                [1492, 530],
                [1598, 530],
                [1704, 530],
                [1810, 530],
                [1916, 530],
                [2022, 530],
                [2128, 530],
                [2232, 530],
                [10, 325],
                [1230, 325],
                [2360, 410],
                [2510, 410],
                [2785, 260],
                [10, 530],
                [3425, 160],
                [150, 225],
                [300, 225],
                [450, 225],
                [600, 225],
                [750, 225],
                [900, 225],
                [1050, 225],
                [1200, 225]
                ]

        self.levelGravitySwitch = [
                [10, 10, 1492, 295],
                [10, 10, 1704, 295],
                [10, 10, 1916, 295],
                [10, 10, 2128, 295],
                [10, 10, 295, 0],
                [10, 10, 590, 0],
                [10, 10, 885, 0],
                [10, 10, 1180, 0],
                [10, 10, 1475, 0],
                [10, 10, 1770, 0],
                [10, 10, 2065, 0],
                [10, 10, 3780, 200]
                ]

        self.levelGateway = [
                [60, self.screenHeight, self.getBackgroundWidth(), 0]
                ]

        self.levelKey = [
                [20, 20, 2450, 440],
                [20, 20, 3790, 190],
                [20, 20, 730, 355],
                [20, 20, 30, 0],
                [20, 20, 30, 255]
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