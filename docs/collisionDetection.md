# 충돌 테스트
```
import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello PyGame')

FpsClock = pygame.time.Clock()

WHITE = (255,  255,  255)
BLACK = (0,  0,  0)
BLUE = (0, 0, 255)

pos_x = 200  # 자동차의 x
pos_y = 150  # 자동차의 y

block = pygame.Rect(50, 50, 50, 50)
car = pygame.Rect(pos_x, pos_y, 100, 50)

def collision_check(obj1, obj2):
    if obj1.top < obj2.bottom and obj2.top < obj1.bottom and obj1.left < obj2.right and obj2.left < obj1.right:
        return True
    else:
        return False

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

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, block)
    pygame.draw.rect(screen, BLUE, car)

    car.x = pos_x
    car.y = pos_y

    if collision_check(car, block):
        print('Crash!!')

    pygame.display.update()
    FpsClock.tick(30)
```
설명은 아래 링크를 참조 바랍니다.
https://www.jbmpa.com/pygame/13