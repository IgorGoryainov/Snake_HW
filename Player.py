import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 51, 102))
        self.rect = self.image.get_rect()
        self.rect.center = (180, 240)

    def update(self):
        self.rect.x += 5