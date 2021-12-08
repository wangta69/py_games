# 참조 https://devnauts.tistory.com/61
import sys
import pygame
from pygame.locals import *

pygame.init()

# Define the colors we will use in RGB format
BLACK = (0,  0,  0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255,  0)
RED = (255,  0,  0)

"""
FULLSCREEN : 전체 화면 모드를 사용
HWSURFACE : 하드웨어 가속 사용. 전체 화면 모드에서만 가능
OPENGL : OpenGL 사용 가능한 디스플레이를 초기화
DOUBLEBUF : 더블 버퍼 모드를 사용. HWSURFACE or OPENGL에서 사용을 추천
"""
screen = pygame.display.set_mode((400, 300))  # 윈도우 크기설정
# screen = pygame.display.set_mode((400, 300), FULLSCREEN | HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('Hello World!')  # 타이틀바의 텍스트를 설정
clock = pygame.time.Clock()

# 이미지 파일을 로딩
sheet = pygame.image.load('assets/explosion_sprite.png').convert_alpha()
imgs = []
for x in range(11):
    imgs.append(sheet.subsurface((190 * x, 0, 190, 190)) )
current_img = 0
while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # next image modulo 7
    print(current_img)
    current_img = (current_img + 1) % 11

    screen.fill((0, 0, 0))
    screen.blit(imgs[current_img], (85, 85))
    pygame.display.flip()


    clock.tick(12)

    pygame.display.flip()  # 화면 전체를 업데이트

# save subsurfaces as separated images

# for x in range(7):
#     name = 'frame_' + str(x) + '.png'
#     pygame.image.save( imgs[x], 'frame_' + str(x) + '.png' )
#     print name, 'saved'