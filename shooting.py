
#1 - Import library
import pygame, sys
import os
from pygame.locals import *

#2 - Initialize game
pygame.init()
DISPLAYSCREEN = pygame.display.set_mode((740, 580))
pygame.display.set_caption('THIS IS WAR!')

#3 - load images

current_path = os.path.dirname(r"d:\Users\jilli\AppData\Local\Programs\Python") # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
player_img = pygame.image.load(os.path.join(image_path, 'dude.png'))

#4 - Loop throuogh game so it doesn't halt

while 1:
    #5 - clears the screen before drawing it again
    screen.fill(0)
    #6 - draw screen elements
    screen.blit(player, (100, 100))  #draw a screen
    #7 - update the screen
    pygame.display.flip()            # Update the full display Surface to the screen
    for event in pygame.event.get(): #event is for actions made by user
                                     #like pressing a key
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
            
            
