import pygame
from Player import Player
from Apple import Apple
from gameProcess import GameProcess

running = [True]


process = GameProcess()
process.init_game()
process.set_surface()

player = Player()
player.eat_apple()
player.set_screen(process.screen)
apple = Apple()
process.all_sprites.add(player)
process.all_sprites.add(apple)

while running[0]:
    if player.check_eaten(apple.rect.centerx, apple.rect.centery):
        apple.eat()
    directions = process.get_events(running)
    running[0] = not player.check_crash()
    if directions:
        player.moving_direction = directions
    process.update_screen()


pygame.quit()
