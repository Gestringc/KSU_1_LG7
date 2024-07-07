## Importation of needed modules, to be updated as needed ##
import pygame
import sys
from Scripts.Froggie import Froggie
from Cars import Car
import pygame.freetype

#-----------------------------------------------------------------------------------------------------------------------
## Initialization of pygame

pygame.init()
pygame.freetype.init()

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

#-----------------------------------------------------------------------------------------------------------------------
## Game Window and Related Variables

Game_Screen = pygame.display.set_mode((1500, 800))
# grass_image = pygame.image.load("./Images/Backgrounds/Grass1.jpg")
Game_Screen.fill(color= (0, 255, 255))
pygame.display.set_caption("Froggie")  #can change title if we decide
pygame.display.flip()
victory = False
font = pygame.freetype.Font(None, 36)
#-----------------------------------------------------------------------------------------------------------------------
##### Here is where we will CREATE the car images with your code  ## *********************************************************************
redCar = pygame.image.load("../Cars/red.png").convert_alpha()
redCar_scale = pygame.transform.scale(redCar, (50, 50)) ## Adjust sizes as needed
redCar_scale_rect = pygame.Rect(0, 800//3, 50, 50)
# redCar_scale_rect.x = 0
# redCar_scale_rect.y = 800//3
# speed1 = [2]

greenCar = pygame.image.load("../Cars/green.png").convert_alpha()
greenCar_scale = pygame.transform.scale(greenCar, (50, 50))## Adjust sizes as needed
greenCar_scale_rect = pygame.Rect(0, 800//2, 50, 50)
# greenCar_scale_rect.x = 0
# greenCar_scale_rect.y = 800//2
# speed2 = [2]

yellowCar = pygame.image.load("../Cars/yellow.png").convert_alpha()
yellowCar_scale = pygame.transform.scale(yellowCar, (50, 50)) ## Adjust Sizes as needed
yellowCar_scale_rect = pygame.Rect(0, 2 * (800 // 3), 50, 50)
# yellowCar_scale_rect.x = 0
# yellowCar_scale_rect.y = 2 * (800 // 3)
# speed3 = [2]



#************************************************************************************************************
Clock = pygame.time.Clock()
### create a list for car colors same as variable names above
car_colors = [redCar_scale, greenCar_scale, yellowCar_scale]
# car_speeds = [speed1, speed2, speed3]
counter = [0 ,0 ,0]
### Create the three time intervals the cars will generate intervals = [x, y, z]
intervals = [1, 3, 0.5]
roads = [800//3, 800//2, 2 * (800 // 3)]  # these will define the three different roads
#-----------------------------------------------------------------------------------------------------------------------
## Froggie Sprite Generation  ##
all_sprites = AllSprites()
obstacle_sprites = pygame.sprite.Group()
Starting_Point = (750, 800)# Bottom of the y-axis, middle of the x-axis
Froggie = Froggie(Starting_Point, all_sprites)

#-----------------------------------------------------------------------------------------------------------------------
## The back ground music is imported and played in a loop ##
#
# Froggie_Music = pygame.mixer.Sound("./Music/Music1.mp3")
# Froggie_Music.set_volume(.2)
# Froggie_Music.play(-1)
# #-----------------------------------------------------------------------------------------------------------------------
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
    #
    # for i in range(0, 1500, grass_image.get_width()):
    #     for j in range(0, 800, grass_image.get_height()):
    #         Game_Screen.blit(grass_image, (i, j))

    if Froggie.rect.y <= 0:
        text_surface, rect = font.render("Froggie Lives!!!", (255,255,255), size=50)
        Game_Screen.blit(text_surface,(Game_Screen.get_width() / 2 - rect.width / 2, Game_Screen.get_height() / 2 - rect.height / 2))
        all_sprites.draw(Game_Screen)
        pygame.display.flip()

    Game_Screen.fill((0, 255, 255))

    Game_Screen.blit(redCar_scale, (0, (800 // 3)))
    Game_Screen.blit(greenCar_scale, (0, (800 // 2)))
    Game_Screen.blit(yellowCar_scale, (0, 2 * (800 // 3)))
#************************ Here we will create a loop for actually generating the cars based off
    # of time  ********************************************************
    for i in range (3): # 3 being the number of roads
        counter[i] += Delta_Time
        if counter[i] > intervals[i]: #### Generate car
                counter[i] = 0
                new_car = (car_colors[i], (0, roads[i]))
                car_colors[i], car_colors[i - 1] = car_colors[i - 1], car_colors[i]  # Cycle car color
                # all_sprites.add(new_car)

    ###obstacle_sprites.add(new_car)  ADD CAR VARIABLE HERE
    all_sprites.draw(Game_Screen)
    pygame.display.flip()