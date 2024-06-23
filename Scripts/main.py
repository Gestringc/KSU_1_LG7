## Importation of needed modules, to be updated as needed ##
import pygame
import sys
import random
from Froggie import Froggie

#-----------------------------------------------------------------------------------------------------------------------
## Initialization of pygame

pygame.init()

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

#-----------------------------------------------------------------------------------------------------------------------
## Game Window and Related Variables

Game_Screen = pygame.display.set_mode((1500, 800))
Game_Screen.fill(color= (0, 255, 255) )
pygame.display.flip()
victory = False

#-----------------------------------------------------------------------------------------------------------------------
## Froggie Sprite Generation  ##
all_sprites = AllSprites()
obstacle_sprites = pygame.sprite.Group()
Starting_Point = (750, 800)# Bottom of the y-axis, middle of the x-axis
Froggie = Froggie(Starting_Point, all_sprites)

#-----------------------------------------------------------------------------------------------------------------------
## The back ground music is imported and played in a loop ##

Froggie_Music = pygame.mixer.Sound("./Music/Froggie_Music.mp3")
Froggie_Music.set_volume(1)
Froggie_Music.play(-1)

#-----------------------------------------------------------------------------------------------------------------------
## Primary Game Loop ##
# Create clock to get delta time later.
Clock = pygame.time.Clock()
while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    Delta_Time = Clock.tick(120)/1000
# handle all sprites' updates
    all_sprites.update(Delta_Time)

    Game_Screen.fill((0, 255, 255))
    all_sprites.draw(Game_Screen)
    pygame.display.flip()