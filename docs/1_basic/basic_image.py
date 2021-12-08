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
img = pygame.image.load('assets/sample.jpg')

while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)  # r g b 로 윈도우 채움

    # # 이미지 파일 그리기
    # screen.blit(img, (50, 100))

    # 이미지 파일 회전하여 그리기
    x = 200
    y = 100
    degree = 10
    rotated = pygame.transform.rotate(img, degree)  # 이미지를 회전한다.
    rect = rotated.get_rect()  # get_rect(centerx=300, bottom=800) # get_rect(topleft=(100, 300))
    # print('rect:', rect)
    # < rect(0, 0, 864, 1004) >
    rect.center = (x, y)
    # print('rect:', rect)
    # <rect(-232, -402, 864, 1004)>
    screen.blit(rotated, rect)


    clock.tick(30) # 초당 30 fps를 위해 딜레이를 추가
    pygame.display.flip()  # 화면 전체를 업데이트

