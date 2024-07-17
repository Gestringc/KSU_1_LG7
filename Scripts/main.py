## Importation of needed modules ##

import pygame
import sys
from Scripts.Froggie import Froggie
import pygame.freetype
from Screens import end_game_screen, pause_game_screen
from log_generation import generate_log_positions

#----------------------------------------------------------------------------------------------------------------------#
## Initialization of pygame and freetype ##

pygame.init()
pygame.freetype.init()

#----------------------------------------------------------------------------------------------------------------------#
## Creation of Car class ##
class Car:
    def __init__(self, img, speed, rect):
        self.image = img
        self.speed = speed
        self.rect = rect

#----------------------------------------------------------------------------------------------------------------------#
## Game screen initialization and background music ##

Game_Screen = pygame.display.set_mode((1500, 800))
Froggie_Music = pygame.mixer.Sound("./Music/Music1.mp3")
Froggie_Music.set_volume(.2)
Froggie_Music.play(-1)

#----------------------------------------------------------------------------------------------------------------------#
## Loading of files, and creation of font ##

grass_image = pygame.image.load("./Images/Backgrounds/Grass1.jpg")
pond = pygame.image.load('./Images/Ponds/Water.jpg').convert_alpha()
log = pygame.image.load('./Images/Ponds/log.png').convert_alpha()
dead_image = pygame.image.load("./Images/Froggie/zzz/Frog_Died.png").convert_alpha()
redCar = pygame.image.load("./Cars/red.png").convert_alpha()
greenCar = pygame.image.load("./Cars/green.png").convert_alpha()
yellowCar = pygame.image.load("./Cars/yellow.png").convert_alpha()
road = pygame.image.load("./Images/Backgrounds/road.jfif").convert_alpha()
barrier = pygame.image.load("./Images/Objects/barrier_4.png").convert_alpha()
bush = pygame.image.load("./Images/Objects/green_bush.png").convert_alpha()
tree1 = pygame.image.load("./Images/Objects/green_small_potted.png").convert_alpha()
tree2 = pygame.image.load("./Images/Objects/tree_1.png").convert_alpha()
font = pygame.freetype.Font(None, 36)
button_font = pygame.freetype.Font(None, 36)
#----------------------------------------------------------------------------------------------------------------------#
## Image Scaling ##

redCar_scale = pygame.transform.scale(redCar, (50, 50))
greenCar_scale = pygame.transform.scale(greenCar, (50, 50))
yellowCar_scale = pygame.transform.scale(yellowCar, (50, 50))
road_scale = pygame.transform.scale(road, (2000, 80))
barrier_scale = pygame.transform.scale(barrier, (40, 20))
bush_scale = pygame.transform.scale(bush, (35, 30))
tree1_scale = pygame.transform.scale(tree1, (30, 60))
tree2_scale = pygame.transform.scale(tree2, (30, 80))
pond = pygame.transform.scale(pond, (375, 170))
log = pygame.transform.scale(log, (125, 50))  # Scale the log
dead_image = pygame.transform.scale(dead_image, (800, 400))
#----------------------------------------------------------------------------------------------------------------------#
## Declaration of variables, lists, etc... ##

pond_size = (375, 170)
log_size = (125, 30)
all_log_positions = []
pond_positions = [
    # pond 1 in Grass lane 2
    (0, 480),
    # pond 2 in Grass lane 2
    (750, 480),

    # pond 3 in Grass lane 3
    (200, 230),
    # pond 4 in Grass lane 3
    (800, 230),
]
car_images = [redCar_scale, greenCar_scale, yellowCar_scale]
car_speeds = [150, 100, 200]
car_positions = [pygame.Rect(0, 150, 50, 50), pygame.Rect(0, 400, 50, 50),
                 pygame.Rect(0, 650, 50, 50)]
cars = [Car(img, speed, pos) for img, speed, pos in zip(car_images, car_speeds, car_positions)]
car_color_index = 0
Clock = pygame.time.Clock()
car_colors = [redCar_scale, greenCar_scale, yellowCar_scale]
counter = [0, 0, 0]
intervals = [2, 3, 5]
roads = [150, 400, 650]  # these will define the three different roads
all_sprites = pygame.sprite.Group()
obstacle_sprites = pygame.sprite.Group()
Starting_Point = (750, 800)

#----------------------------------------------------------------------------------------------------------------------#
## Creation of rects ##

for pond_position in pond_positions:
    log_positions = generate_log_positions(pond_position, pond_size, log_size)
    all_log_positions.extend(log_positions)
pond_rects = [pygame.Rect(x, y, pond.get_width(), pond.get_height()) for x, y in pond_positions]
log_rects = [pygame.Rect(x, y, log.get_width(), log.get_height()) for x, y in all_log_positions]

redCar_scale_rect = pygame.Rect(0, 800 // 3, 50, 50)
greenCar_scale_rect = pygame.Rect(0, 800 // 2, 50, 50)
yellowCar_scale_rect = pygame.Rect(0, 2 * (800 // 3), 50, 50)

barrier_rects = []
barrier_positions = [(500, 645), (455, 645), (1035, 145), (920, 145), (305, 400), (425, 400),(1265,645),
                     (1155,645),(1265,460),(1310,460),(750,705),(695,705),(805,705),(650,400),(750,210),(580,210)]
for pos in barrier_positions:
    rect = barrier_scale.get_rect(topleft=pos)
    barrier_rects.append(rect)

bush_rects = []
bush_positions = [(150,235),(580,365),(525,500),(650,235),(690,235)]
for pos in bush_positions:
    rect2 = bush_scale.get_rect(topleft=pos)
    bush_rects.append(rect2)

tree1_rects = []
tree1_positions = [(1400,340), (1300,340), (1200,340), (1250,240),(1350,240), (1450,240)]
for pos in tree1_positions:
    rect3 = tree1_scale.get_rect(topleft=pos)
    tree1_rects.append(rect3)

tree2_rects = []
tree2_positions = [(715,565),(20,310),(50,50),(200,50),(350,50),(500,50),
                   (650,50),(800,50),(950,50),(1100,50),(1250,50),(1400,50)]
for pos in tree2_positions:
    rect4 = tree2_scale.get_rect(topleft=pos)
    tree2_rects.append(rect4)

barriers = [(barrier_scale, rect) for rect in barrier_rects]

bushes = [(bush_scale, rect) for rect in bush_rects]

trees1 = [(tree1_scale, rect) for rect in tree1_rects]

trees2 = [(tree2_scale, rect) for rect in tree2_rects]

#----------------------------------------------------------------------------------------------------------------------#
## Creation of masks ##

pond_masks = [pygame.mask.from_surface(pond) for _ in pond_positions]
log_masks = [pygame.mask.from_surface(log) for _ in log_positions]
blockers = barriers + bushes + trees1 + trees2
blocker_mask_dict = {}
for img, rect in blockers:
    mask = pygame.mask.from_surface(img)
    blocker_mask_dict[(rect.x, rect.y, rect.width, rect.height)] = mask
#----------------------------------------------------------------------------------------------------------------------#
## Froggie Sprite Generation  ##

Froggie = Froggie(Starting_Point, all_sprites, blockers, blocker_mask_dict)

#----------------------------------------------------------------------------------------------------------------------#
## Primary Game Loop ##
# Create clock to get delta time later.
Clock = pygame.time.Clock()
while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                original_position = Froggie.rect.topleft
                Froggie.rect.topleft = original_position
                pygame.mixer.pause()  # pause game music
                pygame.display.flip
                result = pause_game_screen("Game Paused", Game_Screen, button_font, dead_image, font)
                if result:
                    Froggie.rect.topleft = Froggie.rect.topleft
                    pygame.mixer.unpause()  # resume the music
                else:
                    pygame.quit()
                    sys.exit()
    Game_Screen.fill(color=(0, 255, 255))
    Delta_Time = Clock.tick(60) / 1000
    all_sprites.update(Delta_Time)

    for i in range(0, 1500, grass_image.get_width()):
        for j in range(0, 800, grass_image.get_height()):
            Game_Screen.blit(grass_image, (i, j))

    Game_Screen.blit(road_scale, (-50, 150))
    Game_Screen.blit(road_scale, (-50, 400))
    Game_Screen.blit(road_scale, (-50, 650))

    for idx, pos in enumerate(barrier_positions):
        Game_Screen.blit(barrier_scale, pos)
    for idx, pos in enumerate(bush_positions):
        Game_Screen.blit(bush_scale,pos)
    for idx, pos in enumerate(tree1_positions):
        Game_Screen.blit(tree1_scale, pos)
    for idx, pos in enumerate(tree2_positions):
        Game_Screen.blit(tree2_scale,pos)

    Froggie_mask = pygame.mask.from_surface(Froggie.image)
    cars_to_remove = []
    pond_mask = pygame.mask.from_surface(pond)
    for car in cars:
        car.rect.x += car.speed * Delta_Time
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
                result = end_game_screen("Froggie Got Hit!!!", Game_Screen, button_font, dead_image, font)
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
            elif Froggie.rect.y <= 0:
                result = end_game_screen("Froggie Lives!!!", Game_Screen, button_font, dead_image, font)
                Froggie.pos = pygame.math.Vector2(Starting_Point)  # update the Vector2 position
                Froggie.rect.topleft = Starting_Point  # update the topleft rect attribute
                Froggie.image = dead_image
                pygame.mixer.pause()  # pause game music
                pygame.display.flip
                if result:
                    # reset game
                    Froggie.image = pygame.image.load("./Images/Froggie/Down/Forward.png")
                    Froggie.rect.topleft = Starting_Point
                    cars = []
                    counter = [0, 0, 0]
                    pygame.mixer.unpause()
                else:
                    pygame.quit()
                    sys.exit()
    Froggie_rect = pygame.Rect(Froggie.rect.x, Froggie.rect.y, Froggie.image.get_width(), Froggie.image.get_height())
    for car in cars_to_remove:
        cars.remove(car)
    Froggie_mask = pygame.mask.from_surface(Froggie.image)
    Froggie_mask_rect = Froggie_mask.get_rect(topleft=(Froggie.rect.x, Froggie.rect.y))

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
            result = end_game_screen("You drowned Froggie!", Game_Screen, button_font, dead_image, font)
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
