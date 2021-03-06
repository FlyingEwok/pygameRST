import pygame

# initialize pygame
# pylint: disable=no-member
pygame.init()

# Sound effects
enemyDeathSound = pygame.mixer.Sound('sounds/EnemyDeathSound.wav')
playerDeathSound = pygame.mixer.Sound('sounds/PlayerDeathSound.wav')
levelCompletedSound = pygame.mixer.Sound('sounds/LevelCompletedSound.wav')
jumpSound = pygame.mixer.Sound('sounds/JumpSound.wav')
collectKeySound = pygame.mixer.Sound('sounds/CollectKeySound.wav')
gravitySwitch = pygame.mixer.Sound('sounds/GravitySwitch.wav')
gateSound = pygame.mixer.Sound('sounds/GateOpenSound.wav')