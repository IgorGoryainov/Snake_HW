import pygame
import settings
from random import randint, choice

directions = ['right', 'left', 'forward', 'down']


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.snake_size, settings.snake_size))
        self.head_color = (255, 51, 102)
        self.tail_color = (204, 153, 102)

        self.rect = self.image.get_rect()
        self.image.fill(self.head_color)
        positions_x = list(range(0, settings.WIDTH, 30))
        positions_y = list(range(0, settings.HEIGHT, 30))
        self.rect.center = (choice(positions_x), choice(positions_y))
        self.moving_direction = choice(directions)

        self.tail = []
        self.score = 0

    def change_head_pose(self):
        if self.moving_direction == "right":
            self.rect.x += 30
        elif self.moving_direction == "left":
            self.rect.x -= 30
        elif self.moving_direction == "up":
            self.rect.y -= 30
        elif self.moving_direction == "down":
            self.rect.y += 30

    def set_screen(self, screen):
        self.screen = screen

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
            print("kek")
            return True



    def draw_tail(self):
        for elem in self.tail:
            pygame.draw.rect(self.screen, self.tail_color, [elem[0]-settings.snake_size/2, elem[1]-settings.snake_size/2, settings.snake_size, settings.snake_size])

    def update(self):
        self.tail.insert(0, [self.rect.centerx, self.rect.centery])
        self.tail.pop()
        self.draw_tail()
        self.change_head_pose()