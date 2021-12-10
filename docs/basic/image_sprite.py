import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))  # 윈도우 크기설정
pygame.display.set_caption('Hello PyGame')  # 타이틀바의 텍스트를 설정
FpsClock = pygame.time.Clock()

# 이미지 파일을 로딩
sheet = pygame.image.load('../../assets/images/explosion_sprite.png')  # .convert_alpha()
# 이미지를 11개로 나눈다
imgs = []
for x in range(11):
    imgs.append(sheet.subsurface((190 * x, 0, 190, 190)))
current_img = 0

while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # next image
    current_img = (current_img + 1) % 11

    screen.fill((0, 0, 0))
    screen.blit(imgs[current_img], (85, 85))
    pygame.display.flip()

    FpsClock.tick(12) # 초당 12 fps를 위해 딜레이를 추가

    pygame.display.flip()  # 화면 전체를 업데이트

# save subsurfaces as separated images
# for x in range(11):
#     name = 'frame_' + str(x) + '.png'
#     pygame.image.save( imgs[x], 'frame_' + str(x) + '.png' )
