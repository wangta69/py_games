# 이미지 처리
- blit : "bit block transfer"의 약어(shortand)이며 한 memory로 부터 다른 memory로 data block을 전송하는 process이다. 

## 이미지 처리 기초
```

import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))  # 윈도우 크기설정
pygame.display.set_caption('Hello PyGame')

FpsClock = pygame.time.Clock()

# Define the colors we will use in RGB format
WHITE = (255, 255, 255)

# 이미지 파일을 로딩
img = pygame.image.load('../../assets/images/bird.jpg')

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


    FpsClock.tick(30) # 초당 30 fps를 위해 딜레이를 추가
    pygame.display.flip()  # 화면 전체를 업데이트
```

## Image Sprite
```
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
```

### 이미지를 나누어 저장
위의 image sprite를 응용한 예로 이미지를 잘라서 저장도 가능하다.
```
for x in range(11):
    name = 'frame_' + str(x) + '.png'
    pygame.image.save( imgs[x], 'frame_' + str(x) + '.png' )

```
