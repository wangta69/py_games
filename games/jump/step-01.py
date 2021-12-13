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
