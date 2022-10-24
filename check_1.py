import pygame

running = True

all_sprites = pygame.sprite.Group()

class GameProcess:
    def __init__(self):
        self.WIDTH = 360
        self.HEIGHT = 480
        self.FPS = 15
        self.clock = pygame.time.Clock()

    def init_game(self):
        pygame.init()

    def set_surface(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")
        self.screen.fill((204, 255, 255))

    def get_events(self):
        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def update_screen(self):
        global all_sprites
        pygame.display.flip()
        self.clock.tick(self.FPS)
        all_sprites.draw(self.screen)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 51, 102))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):
        self.rect.x += 5


process = GameProcess()
player = Player()
all_sprites.add(player)

process.init_game()
process.set_surface()

while running:
    player.update()
    process.get_events()
    process.update_screen()


pygame.quit()