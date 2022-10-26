import pygame
import settings
from random import choice
import os

directions = ['right', 'left', 'forward', 'down']

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.snake_size, settings.snake_size))
        self.head_color = (255, 102, 153)
        self.tail_color = (204, 153, 102)
        self.border_color = (153, 51, 0)

        self.rect = self.image.get_rect()
        self.image.fill(self.head_color)
        positions_x = list(range(0, settings.WIDTH, 30))
        positions_y = list(range(0, settings.HEIGHT, 30))
        self.rect.center = (choice(positions_x), choice(positions_y))
        self.moving_direction = choice(directions)
        self.current_direction = None

        self.tail = []
        self.score = 0

    def check_crash(self):
        if self.tail[1:].count([self.rect.centerx, self.rect.centery]) == 1:
            return True

    def change_head_pose(self):
        if self.current_direction == "right":
            self.rect.x += 30
        elif self.current_direction == "left":
            self.rect.x -= 30
        elif self.current_direction == "up":
            self.rect.y -= 30
        elif self.current_direction == "down":
            self.rect.y += 30

    def set_screen(self, screen):
        self.screen = screen

    def check_bound(self):
        if self.rect.left > settings.WIDTH:
            self.rect.centerx = 0 - settings.snake_size
        elif self.rect.right < 0:
            self.rect.centerx = settings.WIDTH + settings.snake_size
        elif self.rect.top > settings.HEIGHT:
            self.rect.centery = 0 - settings.snake_size
        elif self.rect.bottom < 0:
            self.rect.centery = settings.HEIGHT + settings.snake_size


    def test(self):
        for i in range(self.score):
            self.tail.insert(0, [self.rect.centerx, self.rect.centery])
        for i in range(self.score):
            self.tail.pop()

    def eat_apple(self):
        self.tail.insert(0, [self.rect.centerx, self.rect.centery])

    def check_eaten(self, apple_x, apple_y):
        if (self.rect.centerx == apple_x) and (self.rect.centery == apple_y):
            self.eat_apple()
            self.score += 1
            return True

    def check_valid_direction(self):
        if any((self.moving_direction == "right" and not self.current_direction == "left",
                self.moving_direction == "left" and not self.current_direction == "right",
                self.moving_direction == "up" and not self.current_direction == "down",
                self.moving_direction == "down" and not self.current_direction == "up")):
            self.current_direction = self.moving_direction


    def draw_tail(self):
        for elem in self.tail:
            pygame.draw.rect(self.screen, self.border_color, (elem[0]-settings.snake_size/2, elem[1]-settings.snake_size/2, settings.snake_size, settings.snake_size))
            pygame.draw.rect(self.screen, self.tail_color, [elem[0]-settings.snake_size/2+1, elem[1]-settings.snake_size/2+1, settings.snake_size-2, settings.snake_size-2])

    def update(self):
        self.check_valid_direction()
        self.tail.insert(0, [self.rect.centerx, self.rect.centery])
        #self.check_crash()
        self.check_bound()
        self.tail.pop()
        self.draw_tail()
        self.change_head_pose()