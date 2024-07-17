# This file creates the Froggie sprite, defines movements, defines animation, and defines collision
#----------------------------------------------------------------------------------------------------------------------#
## Import of functions ##

import pygame
import sys
from os import walk

#----------------------------------------------------------------------------------------------------------------------#
## Defining and building of the FroggieI class ##
class Froggie(pygame.sprite.Sprite):
    def __init__ (self, position, groups, blockers, blocker_mask_dict):
        self.pos = pygame.math.Vector2(position)
        self.blockers = blockers
        self.blocker_mask_dict = blocker_mask_dict
        super().__init__(groups)
        self.import_assets()
        print(self.animations) ## Debug
        self.frame_index = 0
        self.move_dir = "Forward"
        self.image = self.animations["Forward"][self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = position)
        self.direction = pygame.math.Vector2((0, 0))
        self.speed = 75
        self.collision_objects = 0
        self.hitbox = self.rect.inflate(0, -self.rect.height/2)
        self.Jump_Sound = pygame.mixer.Sound("./Music/Jump2.mp3")
        self.Jump_Sound.set_volume(0.2)

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
    def is_blocked(self, future_direction):
        future_rect = self.rect.move((self.speed * future_direction[0], self.speed * future_direction[1]))

        for blocker in self.blockers:
            img, rect = blocker  # Unpack the image and rect from the blocker tuple
            # Check the future position for collisions, not the current position
            blocker_mask = self.blocker_mask_dict[(rect.x, rect.y, rect.width, rect.height)]
            offset_x = rect.x - future_rect.x
            offset_y = rect.y - future_rect.y
            if blocker_mask.overlap(self.mask, (offset_x, offset_y)):
                return True

        return False

    #-----------------------------------------------------------------------------------------------------------------------
## The movement for Froggie is defined here ##

    def move_player(self, deltaTime):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.speed * deltaTime
            self.rect.centerx = round(self.pos.x)
            self.hitbox.centerx = self.rect.centerx

            self.pos.y += self.direction.y * self.speed * deltaTime
            self.rect.centery = round(self.pos.y)
            self.hitbox.centery = self.rect.centery

#-----------------------------------------------------------------------------------------------------------------------
## Keyboard imputs for player are defined, WASD and Arrow keys both allowed ##
## Allows for continuous Keyboard Input ##

    def input(self):
        Counter = 0
        keyboard_keys = pygame.key.get_pressed()
        if (keyboard_keys[pygame.K_LEFT] or keyboard_keys[pygame.K_a]) and not self.is_blocked((-1, 0)):
            self.direction.x = -1
            self.move_dir = 'Left'
            Counter += 1
            self.Jump_Sound.play()
        elif (keyboard_keys[pygame.K_RIGHT ] or keyboard_keys[pygame.K_d]) and not self.is_blocked((1, 0)):
            self.direction.x = 1
            self.move_dir = 'Right'
            Counter += 1
            self.Jump_Sound.play()
        else:
            self.direction.x = 0

        if (keyboard_keys[pygame.K_UP] or keyboard_keys[pygame.K_w]) and not self.is_blocked((0, -1)):
            self.direction.y = -1
            self.move_dir = 'Forward'
            Counter += 1
            self.Jump_Sound.play()
        elif (keyboard_keys[pygame.K_DOWN] or keyboard_keys[pygame.K_s]) and not self.is_blocked((0, 1)):
            self.direction.y = 1
            self.move_dir = 'Down'
            Counter += 1
            self.Jump_Sound.play()
        else:
            self.direction.y = 0

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
