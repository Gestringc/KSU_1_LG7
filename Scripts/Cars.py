# This file creates the Car sprite, defines movements, defines animation, and defines collision
#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
## Defining and building of the cars class. ##

class Car(pygame.sprite.Sprite):

    def __init__ (self, position, groups):
        super().__init__(groups)
        self.pos = pygame.math.Vector2(position)
        self.import_assets()
        print(self.animations)  ## Debug
        self.frame_index = 0
        self.move_dir = "Left"
        self.image = self.animations["Left"][self.frame_index]
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.math.Vector2((0, 0)) ### what vector do cars need to be?
        self.speed = 50  # what speed to cars need to be?
        self.collision_objects = 0  ##Collision_Group
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)


#-----------------------------------------------------------------------------------------------------------------------
## Need to define the collision with objects, to be finished ##
#-----------------------------------------------------------------------------------------------------------------------
## Images for Cars import ##
        redCar = pg.image.load("red.png").convert()
        ##scale image?
        screen.blit(redCar,) #what x,y are we putting car - lane 1?

        GreenCar = pg.image.load("green.png").convert()
        ##scale image?
        screen.blit(GreenCar,) #what x,y are we putting car - lane 2?

        YellowCar = pg.image.load("yellow.png").convert()
        ##scale image?
        screen.blit(YellowCar, )  # what x,y are we putting  car - lane 3?

 # -----------------------------------------------------------------------------------------------------------------------
        ## The movement for cars is defined here ##





