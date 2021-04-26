import pygame
from player import Player

pygame.init()

larg, alt = 640, 480
screen = pygame.display.set_mode([larg, alt])
clock = pygame.time.Clock()

player = Player(larg/5, alt/2)
continuar = True
while continuar:
    clock.tick(30)
    screen.fill([17,17,17])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False
    player.listen()
    player.show(screen)
    pygame.display.update()

exit()