import sys
import pygame
import random

class Fighter:
    """
    fighter class
    """
    def __init__(self, screen):  # 초기화시 Shooting 게임의 screen 정보를 가져온다.
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


class Missile:
    """
    Missile Class
    """
    def __init__(self, screen):
        self.screen = screen
        self.missile = pygame.image.load('assets/images/missile.png')
        self.sound = pygame.mixer.Sound('assets/sounds/missile.wav')
        self.fired = []  # 발사된 미사일 좌표 (여러개)

    # 미사일을 그린다.
    def draw(self):
        if len(self.fired) != 0:
            for i, bxy in enumerate(self.fired):
                bxy[1] -= 10  # 미사일의 y 좌표값을 변경한다.
                self.screen.blit(self.missile, (bxy[0], bxy[1]))

    def play(self):  # 미사일이 발사될때의 사운드
        self.sound.play()

    def shoot(self, fighter):
        """
        미사일을 발사하면 현재 fighter의 위치에서 발사되게 처리
        이것을 list에 넣어둔다.
        """
        missile_x = fighter.x + fighter.width / 2
        missile_y = fighter.y - fighter.height
        self.fired.append([missile_x, missile_y])


class Rock:
    """
    Rock Class
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.rockImages = [
            'rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',
            'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',
            'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',
            'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',
            'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',
            'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png'
        ]

        self.rock = None
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.speed = 2  # 운석속도

    def create(self):
        self.rock = pygame.image.load('assets/images/' + random.choice(self.rockImages))
        size = self.rock.get_rect().size
        self.width = size[0]
        self.height = size[1]

        self.x = random.randrange(0, self.screen_width - self.width)  # 0에서 특정 x 까지 랜덤으로 x위치 설정
        self.y = 0

    def draw(self):
        self.y += self.speed  # 운석의 위치값 변경
        if self.y > self.screen_height:  # 놓친 경우 (화면아래로 사라진 경우)
            self.create()

        self.screen.blit(self.rock, (self.x, self.y))


class Shooting:
    def __init__(self):
        # 변수 초기화
        self.screen = None
        self.screen_width = 480
        self.screen_height = 640

        self.background = None  # 백그라운드 이미지
        self.clock = None  # Clock

        self.fighter = None  # 비행기 객체
        self.missile = None  # 미사일 객체
        self.rock = None  # 운석 객체

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
        self.missile = Missile(self.screen)  # missile 객체생성
        self.rock = Rock(self.screen)  # rock 객체생성
        self.rock.create()  # 운석을 만든다

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
                elif event.key == pygame.K_SPACE:  # 미사일을 발사한다.
                    self.missile.play()
                    self.missile.shoot(self.fighter)

            if event.type in [pygame.KEYUP]: # 키업일 경우.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0

            self.drawObject(self.background, 0, 0)
            if self.playing:  # 게임이 진행중이면
                self.fighter.x += fighter_x  # fighter 포지션 변경

                self.fighter.draw()  # fighter 를 그린다.
                self.missile.draw()  # 미사일을 그린다.
                self.rock.draw()  # 운석을 그린다.
                pass

            else:  # 게임이 진행중이 아니면
                pass

            pygame.display.update()
            self.clock.tick(60)  # 초당 60회로 fps 설정


if __name__ == '__main__':
   shooting = Shooting()  # 클래스 호출시 클래스내의 __init__(self): 부분은 자동실행된다.
