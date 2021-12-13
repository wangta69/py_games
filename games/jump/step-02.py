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

    def load_car(self):  # 자동차 이미지를 불러와 위치를 정한다.
        # 플레이어 차량
        self.image = pygame.image.load("assets/images/smallcar.png")
        # 크기 조정
        self.image = pygame.transform.scale(self.image, (150, 57))
        self.rect = self.image.get_rect()
        self.rect.bottom = screen_height

    def draw_car(self):  # 자동차를 스크린에 그리기
        screen.blit(self.image, [self.rect.x, self.rect.y])


def main():
    global screen, screen_width, screen_height

    # pygame 초기화 및 스크린 생성
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jump Test")

    clock = pygame.time.Clock()

    player = Car()  # 플레이어 자동차 생성
    player.load_car()  # 자동차 이미지 로드

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)  # 배경색을 흰색으로

        player.draw_car()  # 자동차를 그린다.

        pygame.display.flip()
        clock.tick(60)  # 초당 60번 실행

if __name__ == '__main__':
    main()
