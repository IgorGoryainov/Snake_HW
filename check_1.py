import pygame
from Player import Player
from gameProcess import GameProcess

running = [True]


process = GameProcess()
process.init_game()
process.set_surface()

player = Player()
process.all_sprites.add(player)


while running[0]:
    process.get_events(running)
    process.update_screen()


pygame.quit()