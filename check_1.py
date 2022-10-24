import pygame
from Player import Player
from gameProcess import GameProcess

running = [True]

all_sprites = pygame.sprite.Group()

process = GameProcess()
player = Player()
all_sprites.add(player)

process.init_game()
process.set_surface()

while running[0]:
    player.update()
    process.get_events(running)
    process.update_screen(all_sprites)


pygame.quit()