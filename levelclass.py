import pygame
import rgbColours
import enemyclass
import platformclass
import invisablehitmarkerclass
import invisableFloor
import gravitySwitch

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def create(self):
        """ Constructor. Pass in a handle to player. Needed for when moving
        platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.hitmarker_list = pygame.sprite.Group()
        self.floor_list = pygame.sprite.Group()
        self.gravitySwitch_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()        
        self.player_list.add(self.player)
        self.screenHeight = pygame.display.get_surface().get_size()[1]
        self.screenWidth = pygame.display.get_surface().get_size()[0]
        self.background = None
        # How far this world has been scrolled left/right
        self.world_shift = 0

    def destroy(self):
        for platform in self.platform_list:
            self.platform_list.remove(platform)
        for hitmarker in self.hitmarker_list:
            self.hitmarker_list.remove(hitmarker)
        for floor in self.floor_list:
            self.floor_list.remove(floor)
        for switch in self.gravitySwitch_list:
            self.gravitySwitch_list.remove(switch)
        for enemy in self.enemy_list:
            self.enemy_list.remove(enemy)
        for player in self.player_list:
            self.player_list.remove(player)

    def reset(self):
        self.destroy()
        self.create()
    
    def __init__(self, player):
        self.player = player
        self.create()
        
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.hitmarker_list.update()
        self.floor_list.update()
        self.gravitySwitch_list.update()
        self.enemy_list.update()
        self.player_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # screen.fill(rgbColours.BLUE)
        screen.blit(self.background, (self.world_shift, 0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.hitmarker_list.draw(screen)
        self.floor_list.draw(screen)
        self.gravitySwitch_list.draw(screen)
        self.enemy_list.draw(screen)
        self.player_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        backgroundWidth = self.getBackgroundWidth()

        # prevents screen from scrolling to the left
        if (self.world_shift + shift_x) > 0:
            self.world_shift = 0
            shift_x = 0

        # Prevents screen from scrolling past the background width on the right
        if self.world_shift < -1*(backgroundWidth - self.screenWidth):
            self.world_shift = -1*(backgroundWidth - self.screenWidth)

        # Prevents from updating the postion of the items
        if self.world_shift <= 0 and self.world_shift >= -1*(backgroundWidth - self.screenWidth):
            # Keep track of the shift amount
            self.world_shift += shift_x 

            # Go through all the sprite lists and shift
            for platform in self.platform_list:
                platform.rect.x += shift_x

            for marker in self.hitmarker_list:
                marker.rect.x += shift_x

            for floor in self.floor_list:
                floor.rect.x += shift_x

            for switch in self.gravitySwitch_list:
                switch.rect.x += shift_x

            for enemy in self.enemy_list:
                enemy.rect.x += shift_x

    def addPlatforms(self, levelPlatform):
        # Go through the array above and add objects        
        for platform in levelPlatform:
            block = platformclass.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
    
    def addHitmarker(self, levelHitMarker):
        for hitmarker in levelHitMarker:
            marker = invisablehitmarkerclass.HitMarker(hitmarker[0], hitmarker[1])
            marker.rect.x = hitmarker[2]
            marker.rect.y = hitmarker[3]
            self.hitmarker_list.add(marker)

    def addEnemy(self, enemyList):
        for enemy in enemyList:
            enemy1 = enemyclass.Enemy()
            enemy1.level = self
            enemy1.rect.x = enemy[0]
            enemy1.rect.y = enemy[1]
            self.enemy_list.add(enemy1)

    def addFloor(self, levelFloor):
        for floor in levelFloor:
            block = invisableFloor.Floor(floor[0], floor[1])
            block.rect.x = floor[2]
            block.rect.y = floor[3]
            block.player = self.player
            self.floor_list.add(block)

    def addSwitch(self, levelGravitySwitch):
        for switch in levelGravitySwitch:
            block = gravitySwitch.Switch(switch[0], switch[1])
            block.rect.x = switch[2]
            block.rect.y = switch[3]
            block.player = self.player
            self.gravitySwitch_list.add(block)

    def placePlayer(self, x, y):
        # Place player
        self.player.rect.x = x
        self.player.rect.y = y

    def getBackgroundWidth(self):
        return self.background.get_width()