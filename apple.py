import pygame
from random import randint, choice
import settings


class Apple(pygame.sprite.Sprite):
    eaten = True

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.snake_size, settings.snake_size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

    def update(self):
        if self.eaten:
            positions_x = list(range(0, settings.WIDTH, 30))
            positions_y = list(range(0, settings.HEIGHT, 30))
            self.rect.centerx = choice(positions_x)
            self.rect.centery = choice(positions_y)
            self.eaten = False


    def eat(self):
        self.eaten = True



