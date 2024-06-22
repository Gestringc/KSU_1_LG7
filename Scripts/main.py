## Importation of needed modules, to be updated as needed ##
import pygame
import sys
import random
# from Froggie import Froggie --- Work in Progress

#--------------------------------------------------------------------------------------------
## Initialization of pygame

pygame.init()

#-------------------------------------------------------------------------------------------------------------------------------
## Game Window and Related Variables

Game_Screen = pygame.display.set_mode((1500, 800))
Game_Screen.fill(color= (0, 255, 255) )
pygame.display.flip()
victory = False

#----------------------------------------------------------------------------------------------------------------------------
## Froggie Start Position is Defined Here ##
Starting_Point = (750, 800) # Bottom of the y-axis, middle of the x-axis
#Froggie = #XXX Need to build sprite and keyboard inputs

#---------------------------------------------------------------------------------------------------------------------------------------------
## The back ground music is imported and played in a loop ##

Froggie_Music = pygame.mixer.Sound("./Music/Froggie_Music.mp3")
Froggie_Music.play(-1)

#-----------------------------------------------------------------------------------------------------------------------------------------
## Primary Game Loop ##
while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()