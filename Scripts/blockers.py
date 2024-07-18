## Importation of needed modules ##

import pygame

#----------------------------------------------------------------------------------------------------------------------#
## Creation of Barrier Class ##
class Barrier(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)
#----------------------------------------------------------------------------------------------------------------------#
## Creation of Barrier Class ##
class Bush(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)
#----------------------------------------------------------------------------------------------------------------------#
## Creation of Barrier Class ##
class Tree1(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)

#----------------------------------------------------------------------------------------------------------------------#
## Creation of Barrier Class ##
class Tree2(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)

#----------------------------------------------------------------------------------------------------------------------#