import pygame
import rgbColours
import sounds

# floor for player to collide with
class Gateway(pygame.sprite.Sprite): 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        # pylint: disable=no-member
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(rgbColours.TRANSPARENT)
        self.rect = self.image.get_rect()

    def update(self):
        if len(self.player.level.key_list) == 0:
            sounds.gateSound.play()
            self.player.level.gateway_list.remove(self)