import sys
import pygame

screen = None
# 게임 화면 크기
screen_width = 800
screen_height = 500

# 색상
WHITE = (255, 255, 255)

# 속도와 질량 기본 값
VELOCITY = 7  # 속도
MASS = 2  # 질량

class Car:
    def __init__(self):
        self.image = None
        self.rect = None
        self.dx = 0
        self.dy = 0
        self.isJump = 0  # 바닥(0), 점프중 (1), 이중점프(2)
        self.v = VELOCITY  # 속도
        self.m = MASS  # 질량

    def load_car(self):  # 자동차 이미지를 불러와 위치를 정한다.
        # 플레이어 차량
        self.image = pygame.image.load("assets/images/smallcar.png")
        # 크기 조정
        self.image = pygame.transform.scale(self.image, (150, 57))
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_height

    def draw_car(self):  # 자동차를 스크린에 그리기
        screen.blit(self.image, [self.rect.x, self.rect.y])

    # x 좌표 이동 - 플레이어 자동차의 움직임 제어할 때 필요
    def move_x(self):
        self.rect.x += self.dx

    def check_screen(self):  # 화면 밖으로 못 나가게 방지
        if self.rect.right > screen_width or self.rect.x < 0:
            self.rect.x -= self.dx
        print('check_screen', self.rect.bottom, screen_height, self.rect.y)
        if self.rect.bottom > screen_height or self.rect.y < 0:
            self.rect.y -= self.dy
    
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
    global screen, screen_width, screen_height

    # pygame 초기화 및 스크린 생성
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jump Test")

    clock = pygame.time.Clock()

    player = Car()  # 플레이어 자동차 생성, player 라는 객체를 생성한다.
    player.load_car()  # 자동차 이미지 로드

    playing = True

    while playing:
        keys = pygame.key.get_pressed()  # 키가 눌린 상태 체크
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_SPACE]):
            if player.isJump == 2:
                player.jump(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # 키를 눌렀을 경우
                if event.key == pygame.K_RIGHT:  # 방향키를 눌렀을 경우 자동차의 위치를 바꾼다.
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5
                    
                # 스페이스키를 눌렀을 때,
                # 0이면 바닥인 상태 : 1로 변경
                # 1이면 점프를 한 상태 : 2로 변경, 점프한 위치에서 다시 점프를 하게 된다. 즉, 이중점프
                if event.key == pygame.K_SPACE:
                    if player.isJump == 0:  # 자동차가 바닥에 있으면
                        player.jump(1)
                    elif player.isJump == 1:  # 현재 점핑 중일 경우
                        player.jump(2)
                    
            if event.type == pygame.KEYUP:  # 키에서 손을 땔 경우
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        screen.fill(WHITE)  # 배경색을 흰색으로

        player.draw_car()  # 자동차를 그린다.
        player.move_x()

        player.doJump()  # 플레이어의 y 좌표를 움직여주는 메서드 추가, 점프하는 것
        player.check_screen()  # 화면밖으로 나가지 않게 처리

        pygame.display.flip()
        clock.tick(60)  # 초당 60번 실행

if __name__ == '__main__':
    main()
