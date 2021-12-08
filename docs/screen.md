# 스크린
```
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))  # 윈도우 크기 설정 
"""
screen = pygame.display.set_mode((400, 300), FULLSCREEN | HWSURFACE | DOUBLEBUF)
FULLSCREEN : 전체 화면 모드를 사용
HWSURFACE : 하드웨어 가속 사용. 전체 화면 모드에서만 가능
OPENGL : OpenGL 사용 가능한 디스플레이를 초기화
DOUBLEBUF : 더블 버퍼 모드를 사용. HWSURFACE or OPENGL에서 사용을 추천
"""
pygame.display.set_caption('Hello PyGame')  # 타이틀바의 텍스트를 설정

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 윈도우 닫기 클릭시
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # 검은색으로 채우기
    pygame.display.update()  # vs. pygame.display.flip()

```