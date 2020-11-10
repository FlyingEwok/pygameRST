import pygame

# intialize pygame
pygame.init()

# Sound effects
enemyDeathSound = pygame.mixer.Sound('sounds/EnemyDeathSound.wav')
playerDeathSound = pygame.mixer.Sound('sounds/PlayerDeathSound.wav')
#levelCompletedSound = pygame.mixer.Sound('sounds/LevelCompletedSound.wav')
jumpSound = pygame.mixer.Sound('sounds/JumpSound.wav')
collectKeySound = pygame.mixer.Sound('sounds/CollectKeySound.wav')

# Background Music
# levelTheme = pygame.mixer.music.load('sounds/LevelTheme.wav')
# menuTheme = pygame.mixer.music.load('sounds/MenuTheme.wav')