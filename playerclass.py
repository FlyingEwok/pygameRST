import pygame
import main
import rgbColours

class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Sprite for the character
        self.image = pygame.image.load('images/astronaut.png')
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # Set inverted gravity variable
        self.invertedGravity = False

        self.isOnSwitch = False 
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        block_hit_list1 = pygame.sprite.spritecollide(self, self.level.gateway_list, False)
        
        for x in block_hit_list1:
            block_hit_list.append(x)

        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
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

        switchHit = pygame.sprite.spritecollide(self, self.level.gravitySwitch_list, False)
        if not self.isOnSwitch:
            for switch in switchHit:
                self.isOnSwitch = True
                if not self.invertedGravity:
                    if self.change_y > 0:
                        self.rect.bottom = switch.rect.top
                        self.invertedGravity = True
                        # invert player sprite here
                        for aswitch in self.level.gravitySwitch_list:
                            aswitch.image.fill(rgbColours.RED)
                else:
                    if self.change_y < 0:
                        self.rect.top = switch.rect.bottom
                        self.invertedGravity = False
                        # invert player sprite here
                        for aswitch in self.level.gravitySwitch_list:
                            aswitch.image.fill(rgbColours.GREEN)

        if len(switchHit) == 0 and self.isOnSwitch:
            self.isOnSwitch = False
        print(self.isOnSwitch)

        # Enemy collision detection 
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in enemy_hit_list:
            if self.change_y > 0:
                enemy.destroy()
            else:
                self.die()            
 
    def calc_grav(self):        
        if not self.invertedGravity:
            """ Calculate effect of gravity. """
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += 0.35      # Default gravity = 0.35, High gravity = 0.55, Lowest gravity = 
    
            # See if we are on the ground.
            if self.rect.y >= main.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = main.SCREEN_HEIGHT - self.rect.height
        else:
            """ Calculate effect of gravity. """
            if self.change_y == 0:
                self.change_y = -1
            else:
                self.change_y -= 0.35      # Default gravity = 0.35, High gravity = 0.55, Lowest gravity = 
    
            # See if we are on the ground.
            if self.rect.y >= main.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = main.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
        if not self.invertedGravity:
            # move down a bit and see if there is a platform below us.
            # Move down 2 pixels because it doesn't work well if we only move down 1
            # when working with a platform moving down.
            self.rect.y += 2        
            
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            block_hit_list1 = pygame.sprite.spritecollide(self, self.level.floor_list, False)
            
            for x in block_hit_list1:
                block_hit_list.append(x)

            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if len(block_hit_list) > 0 or self.rect.bottom >= main.SCREEN_HEIGHT:
                self.change_y = -10
        else:
            self.rect.y -= 2        
            
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            block_hit_list1 = pygame.sprite.spritecollide(self, self.level.floor_list, False)
            
            for x in block_hit_list1:
                block_hit_list.append(x)

            self.rect.y += 2

            # If it is ok to jump, set our speed upwards
            if len(block_hit_list) > 0 or self.rect.top >= main.SCREEN_HEIGHT:
                self.change_y = 10

    def die(self):
        self.level.reset()
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0