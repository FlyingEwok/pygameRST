import pygame
import rgbColours
import sounds

# floor for player to collide with
class Key(pygame.sprite.Sprite): 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        # pylint: disable=no-member
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(rgbColours.BLUE)
        self.rect = self.image.get_rect()

    def update(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.player.level.player_list, False)

        if len(block_hit_list):
            sounds.collectKeySound.play()
            self.player.level.key_list.remove(self)