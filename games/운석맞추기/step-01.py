import sys
import pygame

class Shooting:
    def __init__(self):
        # 변수 초기화
        self.screen = None
        self.screen_width = 480
        self.screen_height = 640
        self.BLACK = (0, 0, 0)

        self.background = None  # 백그라운드 이미지
        self.clock = None  # Clock

        self.playing = True
        self.initGame()  # 게임초기화
        self.playGame()  # 게임진행

    def initGame(self):
        # pygame 초기화 및 스크린 생성
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shooting Game')
        
        # 지구와 우주가 보이는 배경화면 설정
        self.background = pygame.image.load('assets/images/background.png')
        self.clock = pygame.time.Clock()

    def drawObject(self, obj, x, y):
        self.screen.blit(obj, (x, y))

    def playGame(self):
        while True:
            event = pygame.event.poll()
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            self.drawObject(self.background, 0, 0)
            pygame.display.update()
            self.clock.tick(60)  # 초당 60회로 fps 설정

if __name__ == '__main__':
   shooting = Shooting()  # 클래스 호출시 클래스내의 __init__(self): 부분은 자동실행된다.
