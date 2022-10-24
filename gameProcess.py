import pygame


class GameProcess:
    def __init__(self):
        self.WIDTH = 360
        self.HEIGHT = 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 15
        self.clock = pygame.time.Clock()

    def init_game(self):
        pygame.init()

    def set_surface(self):
        pygame.display.set_caption("Snake")
        self.screen.fill((204, 255, 255))

    def get_events(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False

    def update_screen(self, all_sprites):
        pygame.display.flip()
        self.clock.tick(self.FPS)
        all_sprites.draw(self.screen)