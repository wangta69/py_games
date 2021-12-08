import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello PyGame')

FpsClock = pygame.time.Clock()

BLACK = (0,  0,  0)
BLUE = (0, 0, 255)

pos_x = 200
pos_y = 150

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                pos_x -= 5
            elif event.key == K_RIGHT:
                pos_x += 5
            elif event.key == K_UP:
                pos_y -= 5
            elif event.key == K_DOWN:
                pos_y += 5

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, Rect(pos_x, pos_y, 100, 50))

    pygame.display.update()
    FpsClock.tick(30)