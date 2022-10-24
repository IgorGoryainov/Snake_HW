import pygame
from random import randint
import settings


class Apple(pygame.sprite.Sprite):
    eaten = True

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

    def update(self):
        if self.eaten:
            self.rect.x = randint(0, settings.WIDTH)
            self.rect.y = randint(0, settings.HEIGHT)
            self.eaten = False


    def eat(self):
        self.eaten = True


