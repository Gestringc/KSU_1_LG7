# This file creates the Froggie sprite, defines movements, defines animation, and defines collision
#----------------------------------------------------------------------------------------------------------------------#
## Import of functions ##

import pygame
from os import walk

#----------------------------------------------------------------------------------------------------------------------#
## Defining and building of the Froggie class ##
class Froggie(pygame.sprite.Sprite):
    def __init__ (self, position, groups, barriers, bush, tree1, tree2, screen_width, screen_height):
        self.pos = pygame.math.Vector2(position)
        self.bushes = bush
        self.trees1 = tree1
        self.trees2 = tree2
        self.barriers = barriers
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__(groups)
        self.import_assets()
        self.frame_index = 0
        self.move_dir = "Forward"
        self.image = self.animations["Forward"][self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = position)
        self.direction = pygame.math.Vector2((0, 0))
        self.speed = 75
        self.hitbox = self.rect.inflate(0, -self.rect.height/2)
        self.Jump_Sound = pygame.mixer.Sound("./Music/Jump_Sound.mp3")
        self.Jump_Sound.set_volume(0.1)
        self.prev_direction_x = 0
        self.prev_direction_y = 0

#----------------------------------------------------------------------------------------------------------------------#
## Images for Froggie import ##
    def import_assets(self):
        Main_Path = "./Images/Froggie"
        self.animations = {}
        for (index, folder) in enumerate(walk(Main_Path)):
            if (index == 0):
                for subfolder in folder[1]:
                    self.animations[subfolder] = []
            else:
                for file in folder[2]:
                    subfolder = folder[0].split("\\")[::-1][0]
                    Image = Main_Path + "/" + subfolder + "/" + file
                    surf = pygame.image.load(Image).convert_alpha()
                    surf = pygame.transform.scale(surf, (100, 100))
                    self.animations[subfolder].append(surf)
#----------------------------------------------------------------------------------------------------------------------#
## Method for checking if Froggie is blocked by barriers ##
    def is_blocked(self):
        if pygame.sprite.spritecollideany(self, self.barriers, pygame.sprite.collide_mask):
            return True
        if pygame.sprite.spritecollideany(self, self.bushes, pygame.sprite.collide_mask):
            return True
        if pygame.sprite.spritecollideany(self, self.trees1, pygame.sprite.collide_mask):
            return True
        if pygame.sprite.spritecollideany(self, self.trees2, pygame.sprite.collide_mask):
            return True
        else:
            return False

#----------------------------------------------------------------------------------------------------------------------#
## Method to check if directin is blocked ##
    def is_direction_blocked(self, direction):
        original_position = self.rect.topleft
        self.rect.move_ip(direction)
        if self.is_blocked():
            self.rect.topleft = original_position
            return True
        self.rect.topleft = original_position
        return False

#----------------------------------------------------------------------------------------------------------------------#
## The movement for Froggie is defined here ##
## Froggie is limited from going off of the bottom, left, and right of the screen. Top is victory condition so no need ##

    def move_player(self, deltaTime):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            new_x = self.pos.x + self.direction.x * self.speed * deltaTime
            new_y = self.pos.y + self.direction.y * self.speed * deltaTime

            half_width = self.rect.width / 2
            half_height = self.rect.height / 2

            if new_x - half_width < 0 and self.direction.x < 0 or new_x + half_width > self.screen_width and self.direction.x > 0:
                new_x = self.pos.x
            if new_y + half_height > self.screen_height and self.direction.y > 0:
                new_y = self.pos.y

            self.pos.x, self.pos.y = new_x, new_y
            self.rect.centerx = int(self.pos.x)
            self.hitbox.centerx = self.rect.centerx
            self.rect.centery = int(self.pos.y)
            self.hitbox.centery = self.rect.centery

    #----------------------------------------------------------------------------------------------------------------------#
## Keyboard inputs for player are defined, WASD and Arrow keys both allowed ##
## Allows for continuous Keyboard Input ##

    def input(self):
        Counter = 0
        keyboard_keys = pygame.key.get_pressed()
        prev_direction_x = self.direction.x if self.direction.x != 0 else self.prev_direction_x
        prev_direction_y = self.direction.y if self.direction.y != 0 else self.prev_direction_y

        if (keyboard_keys[pygame.K_LEFT] or keyboard_keys[pygame.K_a]) and not self.is_direction_blocked((-1, 0)):
            self.direction.x = -1
            self.move_dir = 'Left'
            Counter += 1
        elif (keyboard_keys[pygame.K_RIGHT ] or keyboard_keys[pygame.K_d]) and not self.is_direction_blocked((1, 0)):
            self.direction.x = 1
            self.move_dir = 'Right'
            Counter += 1
        else:
            self.direction.x = 0

        if (keyboard_keys[pygame.K_UP] or keyboard_keys[pygame.K_w]) and not self.is_direction_blocked((0, -1)):
            self.direction.y = -1
            self.move_dir = 'Forward'
            Counter += 1
        elif (keyboard_keys[pygame.K_DOWN] or keyboard_keys[pygame.K_s]) and not self.is_direction_blocked((0, 1)):
            self.direction.y = 1
            self.move_dir = 'Down'
            Counter += 1
        else:
            self.direction.y = 0

        if (self.direction.x != 0 and prev_direction_x != self.direction.x) or \
                (self.direction.y != 0 and prev_direction_y != self.direction.y):
            self.Jump_Sound.play()

        self.prev_direction_x = prev_direction_x
        self.prev_direction_y = prev_direction_y

#-----------------------------------------------------------------------------------------------------------------------
##

    def animate_player(self, deltaTime):
        if (self.direction.magnitude() != 0):
            self.frame_index += 10 * deltaTime
            if (self.frame_index >= len(self.animations[self.move_dir])):
                self.frame_index = 0

        else:
            self.frame_index = 0

        self.image = self.animations[self.move_dir][int(self.frame_index)]

    def update(self, deltaTime):
        self.input()
        self.move_player(deltaTime)
        self.animate_player(deltaTime)
