import sys
import pygame

screen = None
# 게임 화면 크기
screen_width = 800
screen_height = 500

# 색상
WHITE = (255, 255, 255)

class Car:
    def __init__(self):
        self.image = None
        self.rect = None
        self.dx = 0

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
        if self.rect.bottom > screen_height or self.rect.y < 0:
            self.rect.y -= self.dy


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # 방향키를 눌렀을 경우 자동차의 위치를 바꾼다.
                if event.key == pygame.K_RIGHT:
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5
                    
            if event.type == pygame.KEYUP:  # 방향키에서 땔 경우 자동차를 멈춘다.
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        screen.fill(WHITE)  # 배경색을 흰색으로

        player.draw_car()  # 자동차를 그린다.
        player.move_x()

        player.check_screen()  # 화면밖으로 나가지 않게 처리

        pygame.display.flip()
        clock.tick(60)  # 초당 60번 실행

if __name__ == '__main__':
    main()
