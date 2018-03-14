import pygame
import math


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():

    # Get beginning bot co-ords
    bot_x = input("Please enter x location of bot: ")
    bot_y = input("Please enter y location of bot: ")

    # Where is the obstacle
    obstacle_x = input("Please enter x location of obstacle: ")
    obstacle_y = input("Please enter y location of obstacle: ")

    # Where is the final destination
    dest_x = input("Please enter x location of obstacle: ")
    dest_y = input("Please enter y location of obstacle: ")

    #Display x and y back to user.
    print("Robot is at: " + bot_x + "," + bot_y)

    #Display x and y of the obstacle back to user.
    print("Obstacle is at: " + obstacle_x + "," + obstacle_y)

    #Display x and y of the destination back to user.
    print("Destination is: " + dest_x + "," + dest_y)

    #Store locations as floats for math
    fbot_x = float(bot_x)
    fbot_y = float(bot_y)
    fobstacle_x = float(obstacle_x)
    fobstacle_y = float(obstacle_y)
    fdest_x = float(dest_x)
    fdest_y = float(dest_y)



    # Calculate angle between the bot would turn to face destination
    # This assumes robot is facing right down positve X-axis
    powAx = math.pow(fdest_x - fbot_x,2)
    powAy = math.pow(fdest_y - fbot_x,2)
    adj = math.sqrt(powAx + powAy)

    turnA = format(math.degrees(math.acos( (fdest_x - fbot_x)/(adj ))), '.4f')
    sTurnA = str(turnA)
    print("turn " + sTurnA + " degrees.")




if __name__ == "__main__":
    main()