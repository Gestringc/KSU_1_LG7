## Importation of needed modules, to be updated as needed ##
import pygame
import sys
from Scripts.Froggie import Froggie
from Cars import Car

#-----------------------------------------------------------------------------------------------------------------------
## Initialization of pygame

pygame.init()

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

#-----------------------------------------------------------------------------------------------------------------------
## Game Window and Related Variables

Game_Screen = pygame.display.set_mode((1500, 800))
Game_Screen.fill(color= (0, 255, 255))
pygame.display.set_caption("Froggie")  #can change title if we decide
pygame.display.flip()
victory = False
#-----------------------------------------------------------------------------------------------------------------------
##### Here is where we will CREATE the car images with your code  ## *********************************************************************
redCar = pygame.image.load("red.png").convert()
redCar = pygame.transform.scale(redCar, (100, 100)) ## Adjust sizes as needed

greenCar = pygame.image.load("green.png").convert()
greenCar = pygame.transform.scale(greenCar, (100, 100)) ## Adjust sizes as needed

yellowCar = pygame.image.load("yellow.png").convert()
yellowCar = pygame.transform.scale(yellowCar, (100, 100)) ## Adjust Sizes as needed

#************************************************************************************************************
Clock = pygame.time.Clock()
### create a list for car colors car_color = [] same as variable names above
### create a list for time counters counters = [0, 0, 0] all zero to start
### Create the three time intervals the cars will generate intervals = [x, y, z]
roads = [800//3, 800//2, 2 * (800 // 3)]  # these will define the three different roads
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
#************************ Here we will create a loop for actually generating the cars based off
    # of time  ********************************************************
    ## for i in range (3): 3 being the number of roads
        # counter[i] += delta time
            # if counter[i] > intervals[i]: #### Generate car
                # counter[i] = 0
                    #new_car = Car(cars_colors[i], (0, road_y_positions[i]))
                    #cars_colors[i], cars_colors[i - 1] = cars_colors[i - 1], cars_colors[i]  # Cycle car color
                    #all_sprites.add(new_car)

    ###obstacle_sprites.add(new_car)  ADD CAR VARIABLE HERE
    all_sprites.draw(Game_Screen)
    pygame.display.flip()