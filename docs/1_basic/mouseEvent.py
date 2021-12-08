import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello PyGame')
FpsClock = pygame.time.Clock()

"""
event.button
1: left click
2: middle click
3: right click
4: scroll up
5: scroll down
"""
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        elif event.type == MOUSEWHEEL:  # 마우스 휠을 움직일때
            print(event) # {'flipped': False, 'y': 1, 'x': 0, 'touch': False, 'window': None})
        elif event.type == MOUSEBUTTONDOWN:  # 마우스 버튼을 누를 때 발생
            print('MOUSEBUTTONDOWN', event.button, pygame.mouse.get_pos())
        elif event.type == MOUSEBUTTONUP:  # 마우스 버튼을 업할때 발생
            print('MOUSEBUTTONUP', event.button, pygame.mouse.get_pos())
        elif event.type == MOUSEMOTION:  # 마우스가 움질일때 발생
            print('MOUSEMOTION', pygame.mouse.get_pos())

    FpsClock.tick(60)
