import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello PyGame')

FpsClock = pygame.time.Clock()

WHITE = (255,  255,  255)
BLACK = (0,  0,  0)
BLUE = (0, 0, 255)

pos_x = 200
pos_y = 150

block = {'rect': pygame.Rect(50, 50, 50, 50)}
car = {'rect': pygame.Rect(200, 150, 100, 50)}

# def doRectsOverlap(rect1, rect2):
#     for a, b in [(rect1, rect2), (rect2, rect1)]:
#         # Check if a's corners are inside b
#         if ((isPointInsideRect(a.left, a.top, b)) or
#             (isPointInsideRect(a.left, a.bottom, b)) or
#             (isPointInsideRect(a.right, a.top, b)) or
#             (isPointInsideRect(a.right, a.bottom, b))):
#             return True
#
#     return False
#
# def isPointInsideRect(x, y, rect):
#     if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
#         return True
#     else:
#         return False

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
    pygame.draw.rect(screen, BLACK, block['rect'])
    pygame.draw.rect(screen, BLUE, car['rect'])

    car['rect'].x = pos_x
    car['rect'].y = pos_y

    print('car', car['rect'].top, car['rect'].width)
    # 비행기가 동굴의 top이나 bottom에 다으면 게임 종료
    if block['rect'].x <= car['rect'].x and block['rect'].x + block['rect'].width <= car['rect'].x :
        pass

    pygame.display.update()
    FpsClock.tick(30)