# 키보드 제어
## KEYUP EVENT
```
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
        elif event.type == KEYUP:  ## 이벤트 타입이 KEY UP 이면
            if event.key == K_LEFT:  ## 이벤트키가 LEFT 
                pos_x -= 5
            elif event.key == K_RIGHT:  ## 이벤트키가 RIGHT 
                pos_x += 5
            elif event.key == K_UP:  ## 이벤트키가 UP 
                pos_y -= 5
            elif event.key == K_DOWN:  ## 이벤트키가 DOWN 
                pos_y += 5

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, Rect(pos_x, pos_y, 100, 50))

    pygame.display.update()
    FpsClock.tick(30)
```
## KEYDOWN EVENT
- 키다운 이벤트도 키업 이벤트와 다르지 않다
- 일반적으로 키업이벤트를 많이 사용한다.
```
......
        elif event.type == KEYDOWN:  ## 이벤트 타입이 KEY DOWN 이면
            if event.key == K_LEFT:
                pos_x -= 5
            elif event.key == K_RIGHT:
                pos_x += 5
......
```
## KEY PRESSED EVENT
```
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()  # 눌려진 키를 확인
    if (keys[pygame.K_LEFT]):
        pos_x -= 5
    elif (keys[pygame.K_RIGHT]):
        pos_x += 5
    elif (keys[pygame.K_UP]):
        pos_y -= 5
    elif (keys[pygame.K_DOWN]):
        pos_y += 5
```