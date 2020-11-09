import pygame_menu
import pygame
import main
''' Create a main menu using pygame menu'''

# pylint: disable=no-member

pygame.init()
surface = pygame.display.set_mode((1280, 720))

def start_the_game():
    main.main()

menu = pygame_menu.Menu(720, 1280, 'Welcome', theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
