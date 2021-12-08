import sys
import pygame
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

pos_x = 200
pos_y = 150
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT]):
        pos_x -= 5
    elif (keys[pygame.K_RIGHT]):
        pos_x += 5
    elif (keys[pygame.K_UP]):
        pos_y -= 5
    elif (keys[pygame.K_DOWN]):
        pos_y += 5

    SURFACE.fill((0, 0, 0))

    pygame.draw.rect(SURFACE, (0, 0, 255), Rect(pos_x, pos_y, 100, 50))

    pygame.display.update()
    FPSCLOCK.tick(30)