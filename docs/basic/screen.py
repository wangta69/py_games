import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))  # 윈도우 크기 설정 
pygame.display.set_caption('Hello PyGame')  # 타이틀바의 텍스트를 설정

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 윈도우 닫기 클릭시
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # 검은색으로 채우기
    pygame.display.update()  # vs. pygame.display.flip()
