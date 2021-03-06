"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#def displayLocation():


def main():
    """ Main function for the game. """
    pygame.init()

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Set the width and height of the screen [width, height]
    size = (800, 800)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Robot Testing")

    # Starting position of the bot
    bot_x = 50
    bot_y = 710
    #bot_direction = "right"

    # Speed and direction of bot
    #bot_change_x = 0
    #bot_change_y = 0

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # Load and set up graphics.
    background_image = pygame.image.load("files/spaceshooter/Backgrounds/darkPurple_800.800.png").convert()
    player_image = pygame.image.load("files/spaceshooter/Backgrounds/playerShip1_blue_small.png").convert()
    player_image.set_colorkey(WHITE)
    rot_bot = player_image

    # Hide the mouse cursor
    pygame.mouse.set_visible(0)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    bot_x += -3
                elif event.key == pygame.K_RIGHT:
                    bot_x += 3
                elif event.key == pygame.K_UP:
                    bot_y += -3
                elif event.key == pygame.K_DOWN:
                    bot_y += 3

            # User let up on a key
            elif event.type == pygame.KEYUP:
               # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0

            # Mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                rot_bot = pygame.transform.rotate(rot_bot,5)


        # --- Game logic should go here
        #mydata = input('Prompt :')

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        #screen.fill(WHITE)
        screen.blit(background_image, [0, 0])


        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        #player_position = pygame.mouse.get_pos()
        #x = player_position[0]
        #y = player_position[1]

        #Rotating the scree:
        #pygame.transform.rotate()
        #rotate(Surface, angle) -> Surface
        screen.blit(rot_bot, [bot_x, bot_y])

        # --- Drawing code should go here
        #Robot Rectangle
        #pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 25, 25])
        #Moving of bot
        # Move the rectangle starting point
        #rect_x += rect_change_x
        #rect_y += rect_change_y

        botLocation = font.render("Robot Location: " , True, BLACK)
        screen.blit(botLocation, [10, 10])

        # Border of active grid
        pygame.draw.line(screen, BLACK, [50, 50], [750, 50], 2)
        pygame.draw.line(screen, BLACK, [50, 50], [50, 750], 2)
        pygame.draw.line(screen, BLACK, [750, 50], [750, 750], 2)
        pygame.draw.line(screen, BLACK, [50, 750], [750, 750], 2)


        # Draw on the screen several lines from (0,10) to (100,110)
        # 5 pixels wide using a for loop
        for y_offset in range(0, 30, 10):
            pygame.draw.line(screen, RED, [100, 310 + y_offset], [200, 410 + y_offset], 3)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()