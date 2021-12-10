import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300), DOUBLEBUF)
pygame.display.set_caption('Hello PyGame')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 폰트 로딩 및 텍스트 객체 초기화
fontObj = pygame.font.Font('../../assets/fonts/NanumPen.ttf', 32)
textSurfaceObj = fontObj.render('나눔펜 Font!', True, GREEN)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150, 100)

# 메인 루프
while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)  # 화면을 하얀색으로 바꾼다

    # 텍스트 오브젝트를 출력
    screen.blit(textSurfaceObj, textRectObj)

    pygame.display.flip()  # 화면 전체를 업데이트

