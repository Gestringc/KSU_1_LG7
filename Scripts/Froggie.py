# This file creates the Froggie sprite, defines movements, defines animation, and defines collision
#-----------------------------------------------------------------------------------------------------------------------
## Importing of needed functions and variables.##
import pygame
import sys
from os import walk
import os ## Debug

#-----------------------------------------------------------------------------------------------------------------------
## Defining and building of the player class. ##
print(f'Current working directory: {os.getcwd()}')
print(f'Exists? {os.path.isdir("./Images/Froggie")}')
class Froggie(pygame.sprite.Sprite):
    def __init__ (self, position, groups):
        self.pos = pygame.math.Vector2(position)
        super().__init__(groups)
        self.import_assets()
        print(self.animations) ## Debug
        self.frame_index = 0
        self.move_dir = "Forward"
        self.image = self.animations["Forward"][self.frame_index]
        self.rect = self.image.get_rect(center = position)
        self.direction = pygame.math.Vector2((0, 0))
        self.speed = 75
        self.collision_objects = 0 ##Collision_Group
        self.hitbox = self.rect.inflate(0, -self.rect.height/2)
        self.Jump_Sound = pygame.mixer.Sound("./Music/Jump2.mp3")
        self.Jump_Sound.set_volume(0.2)

#-----------------------------------------------------------------------------------------------------------------------
## Need to define the collision with objects, to be finished ##
#-----------------------------------------------------------------------------------------------------------------------
## Images for Froggie import ##
    def import_assets(self):
        Main_Path = "./Images/Froggie"
        print(os.path.isdir(Main_Path)) ## Debug
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
        if (keyboard_keys[pygame.K_LEFT] or keyboard_keys[pygame.K_a]):
            self.direction.x = -1
            self.move_dir = 'Left'
            Counter += 1
            self.Jump_Sound.play()
        elif (keyboard_keys[pygame.K_RIGHT ] or keyboard_keys[pygame.K_d]):
            self.direction.x = 1
            self.move_dir = 'Right'
            Counter += 1
            self.Jump_Sound.play()
        else:
            self.direction.x = 0

        if (keyboard_keys[pygame.K_UP] or keyboard_keys[pygame.K_w]):
            self.direction.y = -1
            self.move_dir = 'Forward'
            Counter += 1
            self.Jump_Sound.play()
        elif (keyboard_keys[pygame.K_DOWN] or keyboard_keys[pygame.K_s]):
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