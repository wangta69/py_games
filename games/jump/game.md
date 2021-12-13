# Jump
참조 : https://www.jbmpa.com/pygame/19

이전 공룡게임에서는 점프를 할때 선형계산을 하여 처리하였습니다.
이번장에서는 중력공식을 이용하여 좀더 실감나는 점프를 구현해 보겠습니다.
또한 Class 에 대해 알아보면서 좀더 확장성 있는 프로그램에 대해 알아 보겠습니다.

### 점프할때의 위치 좌표 공식
```
F = 1/2 * m * v^2
```
- F = Force (위/아래 힘)
- m = mass (물체의 질량)
- v = velocity (속도)

## 클래스(Class)란 무엇인가
클래스란 함수의 집합입니다. 함수의 사용이 코드의 재사용 이었던 것처럼 클래스도 이와 동일합니다.
객체(Object), 인스턴스, 상속이라는 개념이 나오는데 이 부분은 별도의 문법에서 다루고 현재는 간단한 사용법만을 다루도록 하겠습니다.

### [문법] Class 정의
```
class Car:
    def __init__(self):  # __init__ 를 생성자라고 한다.
                         # 생성자는 객제생성시 자동으로 호출(실행)되어지는 부분을 말한다.
        .............
    
    def func1(self):  # 클래스 내부에 함수가 들어오면 메소드(method)라고 일컽는다.
        .............
        
    def func2(self):
        .............
```
### [문법] Class 호출
```
carObj = Car()  # 위에 정의된 Car()를 호출함으로서 carObj 라는 객체(Object)를 생성한다.
                # carObj는 Object이고 carObj는 Car()의 인스턴스이다.
carObj.func1()
```

### [문법] 전역변수, 지역변수
변수에는 전역변수와 지역변수가 있습니다.
지역변수는 함수내에서만 사용하는 것이고 전역변수는 다른 함수에서도 사용가능한 것입니다.

## [게임코드] 기본 구성 
```
import sys
import pygame

# 게임 화면 크기
screen = None
screen_width = 800
screen_height = 500

# 색상
WHITE = (255, 255, 255)

class Car:
    def __init__(self):
        pass

def main():
    global screen, screen_width, screen_height  # 전역변수 설정

    # pygame 초기화 및 스크린 생성
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jump Test")

    clock = pygame.time.Clock()


    player = Car()  # 플레이어 자동차 생성

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)  # 배경색을 흰색으로

        pygame.display.flip()
        clock.tick(60)  # 초당 60번 실행

if __name__ == '__main__':
    main()

```
구글공룡게임 과 비슷한 모습이다.
차이가 있다면 class를 정의한 것만이 다르다.
이제 자동차를 디스플레이 해 보자

### [문법] self
self는 Class 내의 전역변수이다. self로 정의되어 있으면 class내의 어디에서나 self.변수명 으로서 호출 가능하다.

## [게임코드] 자동차 화면에 디스플레이하기
```
class Car:
    def __init__(self):
        self.image = None
        self.rect = None
        
    def load_car(self):  # 자동차 이미지를 불러와 위치를 정한다.
        # 플레이어 차량
        self.image = pygame.image.load("assets/images/smallcar.png")
        # 크기 조정
        self.image = pygame.transform.scale(self.image, (150, 57))
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_height

    def draw_car(self):  # 자동차를 스크린에 그리기
        screen.blit(self.image, [self.rect.x, self.rect.y])

..........
def main():
    ..........
    player = Car()  # 플레이어 자동차 생성
    player.load_car()  # 자동차 이미지 로드
    ..........
    while playing:
        ..........
        player.draw_car()  # 자동차를 그린다.
        ..........
```

이제 우리가 원하는 자동차가 화면상에 나타날 것이다.
이제 키보드 입력을 통해 좌우로 움직이게 구성해 보자.
## [게임코드] 자동차 움직이기
```
class Car:
    def __init__(self):
        ..........
        self.dx = 0

    ..........
    # x 좌표 이동 - 플레이어 자동차의 움직임 제어할 때 필요
    def move_x(self):
        self.rect.x += self.dx


def main():
    ..........

    while playing:
        for event in pygame.event.get():
            ..........
            if event.type == pygame.KEYDOWN:  # 방향키를 눌렀을 경우 자동차의 위치를 바꾼다.
                if event.key == pygame.K_RIGHT:
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5

        ..........
        player.move_x()
..........

```
어라! 자동차가 멈추지 않고 화면 밖으로 나가번린다.
## [게임코드] 자동차 멈추기 및 화면 밖으로 나가지 않게 처리하기
- 자동차 멈추기 기능 : 키보드에서 손을때면 화면 멈추기
- 화면밖으로 자동차 나가지 않게 하기
```
class Car:
    ..........

    def check_screen(self):  # 화면 밖으로 못 나가게 방지
        if self.rect.right > screen_width or self.rect.x < 0:
            self.rect.x -= self.dx
        if self.rect.bottom > screen_height or self.rect.y < 0:
            self.rect.y -= self.dy


def main():
    ..........

    while playing:
        for event in pygame.event.get():
            ..........
                    
            if event.type == pygame.KEYUP:  # 방향키에서 땔 경우 자동차를 멈춘다.
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        ..........

        player.check_screen()  # 화면밖으로 나가지 않게 처리

..........
    
```

## [게임코드] 점프
- 스페이스 바를 눌렀을때 자동차 점핑 기능 구현
```
..........

# 속도와 질량 기본 값
VELOCITY = 7  # 속도
MASS = 2  # 질량

class Car:
    def __init__(self):
        ..........
        self.dy = 0
        self.isJump = 0  # 바닥(0), 점프중 (1), 이중점프(2)
        self.v = VELOCITY  # 속도
        self.m = MASS  # 질량

    ..........
    
    def jump(self, j):  # 점프상태 변경
        self.isJump = j
        
    def doJump(self):
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:
            # isJump 값이 2일 경우 속도를 리셋
            # 점프 한 상태에서 다시 점프를 위한 값

            # 이 코드를 주석처리하면 이중점프를 못한다.
            if self.isJump == 2:
                self.v = VELOCITY

            # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(0.5 * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.rect.y -= round(F)

            # 속도 줄여줌
            self.v -= 1

            # 바닥에 닿았을때, 변수 리셋
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                self.isJump = 0
                self.v = VELOCITY


def main():
    ..........

    while playing:
        keys = pygame.key.get_pressed()  # 키가 눌린 상태 체크
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_SPACE]):
            if player.isJump == 2:
                player.jump(1)

        for event in pygame.event.get():
            ..........
                    
                # 스페이스키를 눌렀을 때,
                # 0이면 바닥인 상태 : 1로 변경
                # 1이면 점프를 한 상태 : 2로 변경, 점프한 위치에서 다시 점프를 하게 된다. 즉, 이중점프
                if event.key == pygame.K_SPACE:
                    if player.isJump == 0:  # 자동차가 바닥에 있으면
                        player.jump(1)
                    elif player.isJump == 1:  # 현재 점핑 중일 경우
                        player.jump(2)
                    
        ..........
        player.doJump()  # 플레이어의 y 좌표를 움직여주는 메서드 추가, 점프하는 것
..........

```
또 다시 멋진 게임이 하나 탄생했습니다.
