# Drawing

```
import sys
import pygame
from math import pi
from pygame.locals import *

pygame.init()

# Define the colors we will use in RGB format
BLACK = (0,  0,  0)
WHITE = (255, 255, 255)
RED = (255,  0,  0)
GREEN = (0, 255,  0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((400, 300))  # 윈도우 크기설정
pygame.display.set_caption('Hello PyGame')  # 타이틀바의 텍스트를 설정

while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)  # r g b 로 윈도우 채움
    
    # 사각형 그리기
    # [x, y, w, h]
    # width: 2, width가 있으면 테두리를 그리고 나머지는 공백을
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # 폴리건 그리기
    # [[시작점X, 시작점Y], ..... [끝점X, 끝점Y]]
    pygame.draw.polygon(screen, BLACK, [[50, 50], [0, 100], [100, 100]], 5)
    pygame.draw.polygon(screen, BLUE, [[200, 50], [150, 100], [250, 100]])

    # 원그리기
    # [중심점X, 중심점Y], 반경길이
    pygame.draw.circle(screen, BLUE, [60, 250], 40, 2)
    pygame.draw.circle(screen, BLUE, [60, 100], 40)

    # 타원그리기 (타원은 사각형안에 원을 넣어두는 형식이다)
    # [시작점X, 시작점Y, width, height] 이라는 사각형안에 원이 들어가는 것이다.
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    
    # arc
    # 타원 그리기와 비슷하나 4개의 굴곡을 각각 처리할 수 있다
    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 5)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    # Draw on the screen a GREEN line from (0,0) to (100, 150)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 150], 5)

    # Draw on the screen a GREEN line from (0,300) to (100, 150)
    # 5 pixels wide.
    pygame.draw.line(screen, BLUE, [0, 300], [100, 150], 5)

    # 5 pixels wide.
    pygame.draw.lines(screen, RED, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw on the screen a BLUE lines from (100,180) to (150,190) to (300,180) to (320,130)
    # 5 pixels wide.
    pygame.draw.lines(screen, BLUE, True, [[100, 180], [150, 190], [300, 180], [320, 130]], 5)

    # Draw on the screen a GREEN line from (0,50) to (50, 80)
    # 5 pixels wide.
    pygame.draw.aaline(screen, BLUE, [0, 50], [50, 80], True)

    # Draw on the screen a GREEN line from (0,100) to (150, 180)
    # 5 pixels wide.
    pygame.draw.aaline(screen, GREEN, [0, 100], [150, 180], False)

    # Draw on the screen a RED lines from (0,80) to (50, 90) to (200, 80) to (220, 30)
    # Closed = False, Blend = True,  1 pixel wide.
    pygame.draw.aalines(screen, RED, False, [[0, 80], [50, 90], [200, 80], [220, 30]], True)

    # Draw on the screen a BLUE lines from (100,180) to (150,190) to (300, 180) to (320, 130)
    # Closed = True,  Blend = False, 1 pixel wide.
    pygame.draw.aalines(screen, BLUE, True, [[100, 180], [150, 190], [300, 180], [320, 130]], True)

    # 전체 화면을 업데이트 할 경우
    # 모든 그리기가 완료된후 실행되어야 함
    # pygame.display.flip()
    pygame.display.update()


pygame.quit()

```