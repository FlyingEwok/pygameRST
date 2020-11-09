import pygame_menu
import pygame
import main
import rgbColours
''' Create a main menu using pygame menu'''

# pylint: disable=no-member

# Intialization
pygame.init()
pygame.display.set_caption("Escape The Space Station!")
icon = pygame.image.load('images/astronaut.png')
pygame.display.set_icon(icon)
surface = pygame.display.set_mode((1280, 720))

# Start game
def start_the_game():
    main.main()

# Title style
mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
mytheme.title_background_color=(0, 0, 0) # Black, like my soul
mytheme.title_font_size = 25
mytheme.title_font = pygame_menu.font.FONT_8BIT # When 16 bits are too many

# Background image
myimage = pygame_menu.baseimage.BaseImage(
    image_path="images/SpaceBackgroundWithGlass.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)
mytheme.background_color=myimage

# Text font
mytheme.widget_font = pygame_menu.font.FONT_8BIT
mytheme.widget_font_color = rgbColours.CYAN

# Create menu
menu = pygame_menu.Menu(720, 1280, 'Escape The Space Station', theme=mytheme)

# Add buttons and images
menu.add_image("images/RobotEnemy1.png", scale=(3, 3))

menu.add_button('Play', start_the_game)
menu.add_button('SuperPlay', start_the_game)
menu.add_button('Please Click Me', start_the_game)
menu.add_button('Free Pizza', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.add_image("images/astronaut.png", scale=(3, 3))
