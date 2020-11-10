import pygame
import playerclass
import level1class
import level2class
 
 
# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
 
def main():
    """ Main Program """
    # pylint: disable=no-member
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Escape From Genesis Station!")
    icon = pygame.image.load('images/astronaut.png')
    pygame.display.set_icon(icon)
 
    # Create the player
    player = playerclass.Player()
 
    # Create all the levels
    level_list = []
    level_list.append(level1class.Level_01(player))
    level_list.append(level2class.Level_02(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    player.level = current_level
  
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
 
        # Update items in the level
        current_level.update()

        # fix player to specific part of screen while moving right, shift the world left (-x)
        if current_level.world_shift > -1*(current_level.background.get_width() - current_level.screenWidth) and player.rect.right >= 380:
            diff = player.rect.right - 380
            player.rect.right = 380
            current_level.shift_world(-diff)

        # fix player to specific part of screen while moving left, shift the world right (+x)
        if current_level.world_shift < 0 and player.rect.left <= 340:
            diff = 340 - player.rect.left
            player.rect.left = 340
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x
        if current_position > current_level.screenWidth:
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                current_level.reset()
 

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 75 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
