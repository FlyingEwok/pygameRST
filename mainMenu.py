import pygame_menu
import pygame
import main
''' Create a main menu using pygame menu'''

# pylint: disable=no-member

pygame.init()
pygame.display.set_caption("Escape The Space Station!")
icon = pygame.image.load('images/astronaut.png')
pygame.display.set_icon(icon)
surface = pygame.display.set_mode((1280, 720))

def start_the_game():
    main.main()

menu = pygame_menu.Menu(720, 1280, 'Escape The Space Station!', theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
