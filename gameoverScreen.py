import pygame_menu
import pygame
import rgbColours
import main
import mainMenu

# pylint: disable=no-member

# Intialization
pygame.init()
pygame.display.set_caption("Escape From Genesis Station!")
icon = pygame.image.load('images/astronaut.png')
pygame.display.set_icon(icon)
surface = pygame.display.set_mode((1280, 720))

# Start game
def start_the_game():
    main.main()

def goToMainMenu():
    pygame.mixer.music.load('sounds/MenuTheme.wav')
    pygame.mixer.music.play(-1)
    mainMenu.menu.mainloop(mainMenu.surface)

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
mytheme.widget_font_color = rgbColours.DARK_RED

# Create menu
menu = pygame_menu.Menu(720, 1280, 'Escape From Genesis Station', theme=mytheme)

# Add buttons and images
menu.add_image("images/RobotEnemy1.png", scale=(3, 3))

mytheme.widget_font_size = 40
menu.add_label("YOU HAVE ESCAPED GENESIS STATION")

mytheme.widget_font_size = 30
mytheme.widget_font_color = rgbColours.CYAN
menu.add_button('Play Again', start_the_game)
menu.add_button('Main Menu', goToMainMenu)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.add_image("images/astronaut.png", scale=(3, 3))

