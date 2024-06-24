# This file creates the Car sprite, defines movements, defines animation, and defines collision
#-----------------------------------------------------------------------------------------------------------------------
## Importing of needed functions and variables.##
import pygame
import sys

#-----------------------------------------------------------------------------------------------------------------------
## Defining and building of the cars class. ##

# Car Class
class Car(pygame.sprite.Sprite):
    def __init__(self, image, Position,*groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(bottomleft=(0, Position))
        self.speed = 25

    def update(self, dt):
        self.rect.x += self.speed * dt
        if self.rect.left > 1500:
            self.kill()  # Death to all cars who travel from the game !!!!!!!!!!


#-----------------------------------------------------------------------------------------------------------------------
## Need to define the collision with objects, to be finished ##



