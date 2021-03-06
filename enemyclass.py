import pygame
import main
import rgbColours
import sounds

class Enemy(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the enemy controls.
    """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set enemy sprite
        self.image = pygame.image.load('images/RobotEnemy1.png')
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of enemy
        self.change_x = 2
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None

        self.debug = False
        self.name = None

    def update(self):
        """ Move the enemy. """
        # Gravity
        self.calc_grav()
 
        # Move left/right, advance by two steps to perform hit detection eariler
        # to avoid enemies intersecting with platforms
        self.rect.x += self.change_x * 2
        
        
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        block_hit_list1 = pygame.sprite.spritecollide(self, self.level.hitmarker_list, False)
        
        self.rect.x -= self.change_x

        for x in block_hit_list1:
            block_hit_list.append(x)

        for block in block_hit_list: 
            # If we are moving right,
            # change movement direction to left
            if self.change_x > 0:
                self.change_x = -2
                self.image = pygame.image.load('images/RobotEnemy1Left.png')
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.change_x = 2
                self.image = pygame.image.load('images/RobotEnemy1.png')
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        block_hit_list1 = pygame.sprite.spritecollide(self, self.level.floor_list, False)
        
        for x in block_hit_list1:
            block_hit_list.append(x)
            
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom 
 
            # Stop our vertical movement
            self.change_y = 0
        
        self.printDebug()
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35       # Default gravity = 0.35, High gravity = 0.55, Lowest gravity = 
 
        # See if we are on the ground.
        if self.rect.y >= main.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = main.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= main.SCREEN_HEIGHT:
            self.change_y = -10

    def destroy(self):
        sounds.enemyDeathSound.play()
        self.level.enemy_list.remove(self)
    
    def printDebug(self):
        if self.debug:
            (height, width) = (self.image.get_height(), self.image.get_width())
            self.image = pygame.Surface([width, height], pygame.SRCALPHA)
            self.image.fill(rgbColours.CYAN)
            print(f"{self.name} is at x: {self.rect.x} y: {self.rect.y} change_x: {self.change_x} change_y: {self.change_y}")
 