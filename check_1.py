import pygame
from Player import Player
from Apple import Apple
from gameProcess import GameProcess

running = [True]


process = GameProcess()
process.init_game()
process.set_surface()

player = Player()
apple = Apple()
process.all_sprites.add(player)
process.all_sprites.add(apple)

while running[0]:
    process.get_events(running)
    process.update_screen()


pygame.quit()
