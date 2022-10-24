import pygame
import settings


class GameProcess:
    def __init__(self):
        self.WIDTH = settings.WIDTH
        self.HEIGHT = settings.HEIGHT
        self.FPS = settings.FPS
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def init_game(self):
        pygame.init()

    def set_surface(self):
        pygame.display.set_caption("Snake")

    def get_events(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False

    def update_screen(self):
        self.clock.tick(self.FPS)
        self.screen.fill((204, 255, 255))
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()