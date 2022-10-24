import pygame
from random import randint


class Apple(pygame.sprite.Sprite):
    eaten = True
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (100 / 2, 200 / 2)

    def update(self):
        if self.eaten:
            self.rect.x = randint(0, 360)
            self.rect.y = randint(0, 480)
            self.eaten = False