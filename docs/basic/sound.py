import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300), DOUBLEBUF)
pygame.display.set_caption('Hello PyGame')

# 사운드 파일을 로딩
soundObj = pygame.mixer.Sound('../../assets/sounds/bg.mp3')

# 메인 루프
while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 마우스 이벤트 처리
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # 왼쪽 버튼 클릭시 플레이
                soundObj.play()
            elif event.button == 3:  # 오른쪽 버튼 클릭시 스톱
                soundObj.stop()

