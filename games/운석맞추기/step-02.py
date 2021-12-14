import sys
import pygame

class Fighter:
    """
    fighter class
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()

        self.fighter = pygame.image.load('assets/images/fighter.png')
        
        # fighter 의 크기
        size = self.fighter.get_rect().size
        self.width = size[0]
        self.height = size[1]

        # fighter 초기 위치 설정
        self.x = screen.get_width() * 0.45
        self.y = screen.get_height() * 0.9  # 지구위에 놓이게 bottom에서 약간 띄운다

    def draw(self):
        """
        fighter의 위치를 변경한다.
        단, 화면밖으로 나가지 않게 처리한다.
        """
        if self.x < 0:
            self.x = 0
        elif self.x > self.screen_width - self.width:
            self.x = self.screen_width - self.width

        self.screen.blit(self.fighter, (self.x, self.y))

class Shooting:
    def __init__(self):
        # 변수 초기화
        self.screen = None
        self.screen_width = 480
        self.screen_height = 640

        self.background = None  # 백그라운드 이미지
        self.clock = None  # Clock

        self.fighter = None  # 비행기 객체

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
        
        # 객체생성
        self.fighter = Fighter(self.screen)  # fighter 객체생성

    def drawObject(self, obj, x, y):
        self.screen.blit(obj, (x, y))

    def playGame(self):
        fighter_x = 0
        while True:
            event = pygame.event.poll()
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:  # 키 다운일경우
                if event.key == pygame.K_LEFT:  # fighter 를 좌측으로
                    fighter_x = -5
                elif event.key == pygame.K_RIGHT:  # fighter 를 우측으로
                    fighter_x = 5

            if event.type in [pygame.KEYUP]: # 키업일 경우.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0

            self.drawObject(self.background, 0, 0)
            if self.playing:  # 게임이 진행중이면
                self.fighter.x += fighter_x  # fighter 포지션 변경
                # fighter 를 그린다.
                self.fighter.draw()
                pass

            else:  # 게임이 진행중이 아니면
                pass


            pygame.display.update()
            self.clock.tick(60)  # 초당 60회로 fps 설정

if __name__ == '__main__':
   shooting = Shooting()  # 클래스 호출시 클래스내의 __init__(self): 부분은 자동실행된다.
