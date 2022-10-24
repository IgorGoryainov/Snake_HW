import pygame
import settings
from random import randint, choice

directions = ['right', 'left', 'forward', 'down']


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.head = pygame.Surface((25, 25))
        self.head_color = (255, 51, 102)
        self.tail_color = (204, 153, 102)

        self.head_pose = self.head.get_rect()
        self.head.fill(self.head_color)
        self.head_pose.center = (randint(0, settings.WIDTH), randint(0, settings.HEIGHT))
        self.moving_direction = choice(directions)

    def change_head_pose(self):

    def update(self):
        self.rect.x += 5