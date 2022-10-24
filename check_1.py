import pygame
import Player

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




process = GameProcess()
player = Player.Player()
all_sprites.add(player)

process.init_game()
process.set_surface()

while running:
    player.update()
    process.get_events()
    process.update_screen()


pygame.quit()