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
## Game Over Screen Function ##
def end_game_screen(message):
    running = True
    retry_text, retry_button = button_font.render("Play Again", (255, 255, 255), size=36)
    quit_text, quit_button = button_font.render("Quit", (255, 255, 255), size=36)

    retry_rect = pygame.Rect(Game_Screen.get_width() / 2 - retry_button.width / 2, Game_Screen.get_height() / 2,
                             retry_button.width, retry_button.height)
    quit_rect = pygame.Rect(Game_Screen.get_width() / 2 - quit_button.width / 2, Game_Screen.get_height() * 2 / 3,
                            quit_button.width, quit_button.height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    return False

        Game_Screen.blit(dead_image, (350, 200))
        text_surface, rect = font.render(message, (255, 255, 255), size=100)
        Game_Screen.blit(text_surface, (Game_Screen.get_width() / 2 - rect.width / 2, 45))
        Game_Screen.blit(retry_text, retry_rect)
        Game_Screen.blit(quit_text, quit_rect)
        pygame.display.flip()

    return False
#-----------------------------------------------------------------------------------------------------------------------
## Function for generating log positions ##
def generate_log_positions(pond_position, pond_size, log_size):
    pond_x, pond_y = pond_position
    pond_width, pond_height = pond_size
    log_width, log_height = log_size

    log_x = pond_x + (pond_width - log_width) // 2  # centering log horizontally

    log_positions = [
        (log_x, y) for y in range(pond_y, pond_y + pond_height, log_height) if y + log_height <= pond_y + pond_height
    ]

    return log_positions
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
Game_Screen = pygame.display.set_mode((1500, 800))
grass_image = pygame.image.load("./Images/Backgrounds/Grass1.jpg")
#Game_Screen.fill(color= (0, 255, 255))
pygame.display.set_caption("Froggie")  #can change title if we decide
pygame.display.flip()
## Ponds are created Here ##
## Ponds are created Here ##
pond = pygame.image.load('./Images/Ponds/Water.jpg').convert_alpha()
pond = pygame.transform.scale(pond, (375, 170))
log = pygame.image.load('./Images/Ponds/log.png').convert_alpha()
log_width = 125  # 1/3 of the Pond width
log = pygame.transform.scale(log, (log_width, 50))  # Scale the log
victory = False
font = pygame.freetype.Font(None, 36)
dead_image = pygame.image.load("./Images/Froggie/zzz/Frog_Died.png").convert_alpha()
dead_image = pygame.transform.scale(dead_image, (800, 400))
button_font = pygame.freetype.Font(None, 36)
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

pond_positions = [
    # pond 1 in Grass lane 2
    (0, 480),
    # pond 2 in Grass lane 2
    (750, 480),

    # pond 3 in Grass lane 3
    (200, 230),
    # pond 4 Grass 3
    (800, 230),
]

pond_size = (375, 170)
log_size = (log_width, 30)
all_log_positions = []
for pond_position in pond_positions:
    log_positions = generate_log_positions(pond_position, pond_size, log_size)
    all_log_positions.extend(log_positions)
pond_rects = [pygame.Rect(x, y, pond.get_width(), pond.get_height()) for x, y in pond_positions]
log_rects = [pygame.Rect(x, y, log.get_width(), log.get_height()) for x, y in all_log_positions]

pond_masks = [pygame.mask.from_surface(pond) for _ in pond_positions]
log_masks = [pygame.mask.from_surface(log) for _ in log_positions]
#-----------------------------------------------------------------------------------------------------------------------
##### Here is where we will CREATE the car images with your code  ## *********************************************************************
redCar = pygame.image.load("./Cars/red.png").convert_alpha()
redCar_scale = pygame.transform.scale(redCar, (50, 50)) ## Adjust sizes as needed
redCar_scale_rect = pygame.Rect(0, 800//3, 50, 50)


greenCar = pygame.image.load("./Cars/green.png").convert_alpha()
greenCar_scale = pygame.transform.scale(greenCar, (50, 50))## Adjust sizes as needed
greenCar_scale_rect = pygame.Rect(0, 800//2, 50, 50)


yellowCar = pygame.image.load("./Cars/yellow.png").convert_alpha()
yellowCar_scale = pygame.transform.scale(yellowCar, (50, 50)) ## Adjust Sizes as needed
yellowCar_scale_rect = pygame.Rect(0, 2 * (800 // 3), 50, 50)

car_images = [redCar_scale, greenCar_scale, yellowCar_scale]
car_speeds = [150, 100, 200]
car_positions = [pygame.Rect(0, 150, 50, 50), pygame.Rect(0, 400, 50, 50),
                 pygame.Rect(0, 650, 50, 50)]
cars = [Car(img, speed, pos) for img, speed, pos in zip(car_images, car_speeds, car_positions)]

car_color_index = 0
#**************************************************************************************************************
#decor images

road = pygame.image.load("./Images/Backgrounds/road.jfif").convert_alpha()
road_scale = pygame.transform.scale(road,(2000,80))

barrel = pygame.image.load("./Images/Objects/barrel_1.png").convert_alpha()
barrel_scale = pygame.transform.scale(barrel,(20,30))
# barrel_scale_rect = pygame.Rect(0, 0,20,30) #determine location***

barrier = pygame.image.load("./Images/Objects/barrier_4.png").convert_alpha()
barrier_scale = pygame.transform.scale(barrier,(40,20))
# barrier_scale_rect = pygame.Rect(0, 0, 40, 20) #determine location****

bin = pygame.image.load("./Images/Objects/bin_open.png").convert_alpha()
bin_scale = pygame.transform.scale(bin,(20, 30))
# bin_scale_rect = pygame.Rect(0, 0, 20, 30)

bush = pygame.image.load("./Images/Objects/green_bush.png").convert_alpha()
bush_scale = pygame.transform.scale(bush, (35,30))
# bush_scale_rect = pygame.Rect(0, 0, 35,30)

#tree1 = pygame.image.load("./Images/Objects/green_small_potted.png").convert_alpha()
#tree1_scale = pygame.transform.scale(tree1, (30,60))
# tree1_scale_rect = pygame.Rect(0, 0, 30, 60)

tree2 = pygame.image.load("./Images/Objects/tree_1.png").convert_alpha()
tree2_scale = pygame.transform.scale(tree2, (30,80))
# tree2_scale_rect = pygame.Rect(0, 0, 30, 80)

#************************************************************************************************************
Clock = pygame.time.Clock()
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

    for i in range(0, 1500, grass_image.get_width()):
        for j in range(0, 800, grass_image.get_height()):
            Game_Screen.blit(grass_image, (i, j))

    #objects/decor
    Game_Screen.blit(road_scale, (-50, 150))
    Game_Screen.blit(road_scale, (-50, 400))
    Game_Screen.blit(road_scale, (-50, 650))
    # Game_Screen.blit(barrel_scale,(80,50)) #add in later after roads/waterways are set
    # Game_Screen.blit(barrier_scale,(150,50))
    # Game_Screen.blit(bin_scale,(120,50))
    # Game_Screen.blit(bush_scale,(100,80))
    # Game_Screen.blit(tree1_scale,(170,50))
    # Game_Screen.blit(tree2_scale,(210,40))
    Froggie_mask = pygame.mask.from_surface(Froggie.image)
    cars_to_remove = []
    pond_mask = pygame.mask.from_surface(pond)
    pond_mask = pygame.mask.from_surface(pond)
    for car in cars:
        car.rect.x += car.speed * Delta_Time  # Update the car's position.
        if car.rect.x > Game_Screen.get_width():
            cars_to_remove.append(car)
        else:
            Game_Screen.blit(car.image, car.rect)
            frog_mask = pygame.mask.from_surface(Froggie.image)
            car_mask = pygame.mask.from_surface(car.image)
            offset = (Froggie.rect.topleft[0] - car.rect.topleft[0],
                      Froggie.rect.topleft[1] - car.rect.topleft[1])
            collision_point = frog_mask.overlap(car_mask, offset)
            if pygame.sprite.collide_mask(Froggie, car):
                result = end_game_screen("You killed Froggie!!!")
                Froggie.pos = pygame.math.Vector2(Starting_Point)  # update the Vector2 position
                Froggie.rect.topleft = Starting_Point  # update the topleft rect attribute
                Froggie.image = dead_image
                pygame.mixer.pause()  # pause game music
                pygame.display.flip
                if result:
                    # reset game
                    Froggie.image = pygame.image.load("./Images/Froggie/Down/Forward.png")  # reset froggie sprite
                    Froggie.rect.topleft = Starting_Point  # reposition froggie to the start
                    cars = []  # remove all cars
                    counter = [0, 0, 0]  # reset car generation timer
                    pygame.mixer.unpause()  # resume the music
                else:
                    pygame.quit()
                    sys.exit()
            elif  Froggie.rect.y <= 0:
                result = end_game_screen("Froggie Lives!!!")
                Froggie.pos = pygame.math.Vector2(Starting_Point)  # update the Vector2 position
                Froggie.rect.topleft = Starting_Point  # update the topleft rect attribute
                Froggie.image = dead_image
                pygame.mixer.pause()  # pause game music
                pygame.display.flip
                if result:
                # reset game
                    Froggie.image = pygame.image.load("./Images/Froggie/Down/Forward.png")  # reset froggie sprite
                    Froggie.rect.topleft = Starting_Point  # reposition froggie to the start
                    cars = []  # remove all cars
                    counter = [0, 0, 0]  # reset car generation timer
                    pygame.mixer.unpause()  # resume the music
                else:
                    pygame.quit()
                    sys.exit()
    Froggie_rect = pygame.Rect(Froggie.rect.x, Froggie.rect.y, Froggie.image.get_width(), Froggie.image.get_height())
    for car in cars_to_remove:
        cars.remove(car)
    Froggie_mask = pygame.mask.from_surface(Froggie.image)
    Froggie_mask_rect = Froggie_mask.get_rect(topleft=(Froggie.rect.x, Froggie.rect.y))

    # Create masks for ponds and logs
    pond_mask = pygame.mask.from_surface(pond)
    log_mask = pygame.mask.from_surface(log)

    # Check for collisions with ponds
    # Check for collisions with ponds
    in_ponds = [Froggie_mask.overlap(pond_mask, (pond_rect.x - Froggie.rect.x, pond_rect.y - Froggie.rect.y)) for
                pond_mask, pond_rect in zip(pond_masks, pond_rects)]
    on_logs = [Froggie.rect.colliderect(log_rect) for log_rect in log_rects]
    total_pond_rects = [pygame.Rect(x, y, *pond_size) for x, y in pond_positions]
    safe_pond_width = 125
    safe_pond_rects = [pygame.Rect(x + (pond_size[0] - safe_pond_width) / 2, y, safe_pond_width, pond_size[1]) for x, y
                       in
                       pond_positions]

    for total_pond_rects, safe_pond_rect in zip(total_pond_rects, safe_pond_rects):
        if total_pond_rects.collidepoint(Froggie.rect.center) and not safe_pond_rect.collidepoint(Froggie.rect.center):
            result = end_game_screen("You drowned Froggie!")
            Froggie.pos = pygame.math.Vector2(Starting_Point)
            Froggie.rect.topleft = Starting_Point

            if result:
                # reset game
                Froggie.image = pygame.image.load("./Images/Froggie/Down/Forward.png")  # reset froggie sprite
                Froggie.rect.topleft = Starting_Point  # reposition froggie to the start
                cars = []  # remove all cars
                counter = [0, 0, 0]  # reset car generation timer
                pygame.mixer.unpause()  # resume the music
            else:
                pygame.quit()
                sys.exit()
    # Car generation
    color_indexes = [0, 1, 2]
    for i in range(3):
        counter[i] += Delta_Time
        if counter[i] >= intervals[i]:
            counter[i] = 0
            car_image = pygame.transform.scale(car_images[car_color_index % len(car_images)], (50, 50))
            new_car = Car(car_image, car_speeds[i], pygame.Rect(0, roads[i], 50, 50))  # create new car
            cars.append(new_car)
            car_color_index += 1

    for pos in pond_positions:
        Game_Screen.blit(pond, pos)
    for log_position in all_log_positions:
        Game_Screen.blit(log, log_position)

    all_sprites.draw(Game_Screen)
    pygame.display.flip()

    