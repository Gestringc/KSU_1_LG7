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

class Car:
    def __init__(self, img, speed, rect):
        self.image = img
        self.speed = speed
        self.rect = rect

#-----------------------------------------------------------------------------------------------------------------------
## Game Window and Related Variables

Game_Screen = pygame.display.set_mode((1500, 800))
grass_image = pygame.image.load("./Images/Backgrounds/Grass1.jpg")
#Game_Screen.fill(color= (0, 255, 255))
pygame.display.set_caption("Froggie")  #can change title if we decide
pygame.display.flip()
victory = False
font = pygame.freetype.Font(None, 36)
#-----------------------------------------------------------------------------------------------------------------------
##### Here is where we will CREATE the car images with your code  ## *********************************************************************
redCar = pygame.image.load("./Cars/red.png").convert_alpha()
redCar_scale = pygame.transform.scale(redCar, (50, 50)) ## Adjust sizes as needed
redCar_scale_rect = pygame.Rect(0, 800//3, 50, 50)
# redCar_scale_rect.x = 0
# redCar_scale_rect.y = 800//3


greenCar = pygame.image.load("./Cars/green.png").convert_alpha()
greenCar_scale = pygame.transform.scale(greenCar, (50, 50))## Adjust sizes as needed
greenCar_scale_rect = pygame.Rect(0, 800//2, 50, 50)
# greenCar_scale_rect.x = 0
# greenCar_scale_rect.y = 800//2


yellowCar = pygame.image.load("./Cars/yellow.png").convert_alpha()
yellowCar_scale = pygame.transform.scale(yellowCar, (50, 50)) ## Adjust Sizes as needed
yellowCar_scale_rect = pygame.Rect(0, 2 * (800 // 3), 50, 50)
# yellowCar_scale_rect.x = 0
# yellowCar_scale_rect.y = 2 * (800 // 3)


car_images = [redCar_scale, greenCar_scale, yellowCar_scale]
car_speeds = [150, 100, 50]
car_positions = [pygame.Rect(0, 150, 50, 50), pygame.Rect(0, 400, 50, 50),
                 pygame.Rect(0, 650, 50, 50)]
cars = [Car(img, speed, pos) for img, speed, pos in zip(car_images, car_speeds, car_positions)]

#**************************************************************************************************************
#decor images

road = pygame.image.load("./Images/Objects/road.png").convert_alpha()
road_scale = pygame.transform.scale(road,(2000,80))


#************************************************************************************************************
Clock = pygame.time.Clock()
### create a list for car colors same as variable names above
car_colors = [redCar_scale, greenCar_scale, yellowCar_scale]
counter = [0 ,0 ,0]
### Create the three time intervals the cars will generate intervals = [x, y, z]
intervals = [2, 3, 5]
roads = [150, 400, 650]  # these will define the three different roads
#-----------------------------------------------------------------------------------------------------------------------
## Froggie Sprite Generation  ##
all_sprites = AllSprites()
obstacle_sprites = pygame.sprite.Group()
Starting_Point = (750, 800)# Bottom of the y-axis, middle of the x-axis
Froggie = Froggie(Starting_Point, all_sprites)

#-----------------------------------------------------------------------------------------------------------------------
## The back ground music is imported and played in a loop ##
#
Froggie_Music = pygame.mixer.Sound("./Music/Music1.mp3")
Froggie_Music.set_volume(.2)
Froggie_Music.play(-1)
# #-----------------------------------------------------------------------------------------------------------------------
## Primary Game Loop ##
# Create clock to get delta time later.
Clock = pygame.time.Clock()
while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    Game_Screen.fill(color=(0, 255, 255))
    Delta_Time = Clock.tick(60)/1000
    #ticker = Clock.tick(10)
    # handle all sprites' updates
    all_sprites.update(Delta_Time)

    Game_Screen.fill((0, 255, 255))
    for i in range(0, 1500, grass_image.get_width()):
        for j in range(0, 800, grass_image.get_height()):
            Game_Screen.blit(grass_image, (i, j))

    Game_Screen.blit(road_scale, (-50, 150))
    Game_Screen.blit(road_scale, (-50, 400))
    Game_Screen.blit(road_scale, (-50, 650))

    if Froggie.rect.y <= 0:
        text_surface, rect = font.render("Froggie Lives!!!", (255,255,255), size=50)
        Game_Screen.blit(text_surface,(Game_Screen.get_width() / 2 - rect.width / 2, Game_Screen.get_height() / 2 - rect.height / 2))
        all_sprites.draw(Game_Screen)
    cars_to_remove = []
    for car in cars:
        car.rect.x += car.speed * Delta_Time  # Update the car's position.
        if car.rect.x > Game_Screen.get_width():
            cars_to_remove.append(car)
        else:
            Game_Screen.blit(car.image, car.rect)

    for car in cars_to_remove:
        cars.remove(car)

    # Car generation
    for i in range(3):
        counter[i] += Delta_Time
        if counter[i] >= intervals[i]:
            counter[i] = 0
            car_image = pygame.transform.scale(car_images[i], (50, 50))  # scale car image
            new_car = Car(car_image, car_speeds[i], pygame.Rect(0, roads[i], 50,
                                                                50))  # create new car using Car class initializer and speed values from "car_speeds"
            cars.append(new_car)

    ###obstacle_sprites.add(new_car)  ADD CAR VARIABLE HERE

    all_sprites.draw(Game_Screen)
    pygame.display.flip()