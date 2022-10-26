import pygame
from random import choice
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
            positions_x = list(range(int(0 + settings.snake_size), int(settings.WIDTH - settings.snake_size), int(settings.snake_size)))
            positions_y = list(range(int(0 + settings.snake_size), int(settings.HEIGHT - settings.snake_size), int(settings.snake_size)))
            self.rect.centerx = choice(positions_x)
            self.rect.centery = choice(positions_y)
            self.eaten = False


    def eat(self):
        self.eaten = True



