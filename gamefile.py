import pygame

pygame.init()

display_width = 0
display_height = 0
gameDisplay = pygame.display.set_mode((display_height,display_width),pygame.FULLSCREEN)
pygame.display.set_caption('Game')


#class Character():
   # def __init__(self):







"""
class Platform():
    def __init__(self):









class Dangers():
    def __init__(self):


"""


def GameLoop():
    run = True
    while run == True:

        for event in pygame.event.get():                                         #gets a list of all of the events in pygame, loops through all events
            if event.type == pygame.QUIT:                                        #If the red cross if pushed it quits the program
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False
            pygame.quit()


GameLoop()

#=====================================================================================================================
"""Notes



"""
