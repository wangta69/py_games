import sys
import pygame
import random
from time import sleep

class Fighter:
    """
    fighter class
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()

        self.fighter = pygame.image.load('assets/images/fighter.png')
        fighterSize = self.fighter.get_rect().size
        self.width = fighterSize[0]
        self.height = fighterSize[1]

        # fighter 초기 위치 설정
        self.x = screen.get_width() * 0.45
        self.y = screen.get_height() * 0.9


    def draw(self):
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
        self.shot = []  # 발사된 미사일 좌표 (여러개)
    # def draw(self, x, y):
    #     self.screen.blit(self.missile, (x, y))

    # 미사일을 그린다.
    def draw(self):
        if len(self.shot) != 0:
            for bx, by in self.shot:
                # self.missile.draw(bx, by)
                self.screen.blit(self.missile, (bx, by))

    def play(self):
        self.sound.play()

    def shoot(self, fighter):
        """
        미사일을 발사하면 현재 fighter의 위치에서 발사되게 처리
        """
        missile_x = fighter.x + fighter.width / 2
        missile_y = fighter.y - fighter.height
        self.shot.append([missile_x, missile_y])

class Crash:
    """
    운석파괴
    """
    def __init__(self, screen):
        self.screen = screen

        self.sounds = [
            'explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav'
        ]

        self.explosion = pygame.image.load('assets/images/explosion.png')

    def draw(self, x, y):
        self.screen.blit(self.explosion, (x, y))

    # 다양한 폭발 사운드 플레이
    def play(self):
        sound = pygame.mixer.Sound('assets/sounds/' + random.choice(self.sounds))
        sound.play()

class Rock:
    """
    Rock Class
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
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
        self.speed = 2
        self.width = 0
        self.height = 0
        self.passed = 0

        # self.rec = {'top': 0, 'left': 0, 'right': 0, 'bottom': 0}  # 충돌테스트용

    def create(self, passed=False):
        """
        """
        self.rock = pygame.image.load('assets/images/' + random.choice(self.rockImages))
        rockSize = self.rock.get_rect().size
        self.width = rockSize[0]
        self.height = rockSize[1]

        self.x = random.randrange(0, self.screen_width - self.width)
        self.y = 0

        if passed == True:  # 참일경우는 파괴못한경우(놓친) 이다.
            self.passed += 1

    def draw(self):
        self.screen.blit(self.rock, (self.x, self.y))

    def collision_check(self, fighter):  # fighter와 충돌테스트
        rock = self.__collision_attr()
        obj2 = self.__collision_attr(fighter)
        if rock['top'] < obj2['bottom'] \
            and obj2['top'] < rock['bottom'] \
            and rock['left'] < obj2['right'] \
            and obj2['left'] < rock['right']:
            return True
        else:
            return False

    def __collision_attr(self, obj=None):
        if obj:
            return {'top': obj.y, 'left': obj.x, 'right': obj.x + obj.width, 'bottom': obj.y + obj.height}
        else:
            return {'top': self.y, 'left': self.x, 'right': self.x + self.width, 'bottom': self.y + self.height}

    def speed_up(self):
        """
        운석이 파괴되면 좀더 빠른 속도로 변경한다.
        """
        # self.speed += 0.02
        self.speed += 0.2
        if self.speed >= 10:
            self.speed = 10


class Shooting:
    def __init__(self):
        # 변수 초기화
        self.screen = None
        self.screen_width = 480
        self.screen_height = 640
        self.BLACK = (0, 0, 0)

        self.background = None  # 백그라운드 이미지
        self.explosion = None  # 폭발이미지
        self.gameOverSound = None  # 게임오버사운드

        self.fighter = None  # 비행기 객체
        self.missile = None  # 미사일 객체
        self.rock = None # 운석 객체
        self.crashed = None  # 운석폭발

        self.clock = None  # Clock

        self.isShot = False
        self.shotCount = 0

        self.playing = True
        self.initGame()
        self.playGame()



    def initGame(self):
        # pygame 초기화 및 스크린 생성
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shooting Game')

        self.background = pygame.image.load('assets/images/background.png')

        pygame.mixer.music.load('assets/sounds/music.wav')
        pygame.mixer.music.play(-1)

        self.gameOverSound = pygame.mixer.Sound('assets/sounds/gameover.wav')
        self.clock = pygame.time.Clock()

        self.fighter = Fighter(self.screen)  # fighter 객체생성
        self.missile = Missile(self.screen)  # missile 객체생성
        self.rock = Rock(self.screen)  # rock 객체생성
        self.rock.create()
        self.crashed = Crash(self.screen)  # rock 객체생성

    def drawObject(self, obj, x, y):
        self.screen.blit(obj, (x, y))

    def writeScore(self, count):
        font = pygame.font.Font('assets/fonts/NanumGothic.ttf', 20)
        text = font.render('파괴한 운석 수: ' + str(count), True, (255, 255, 255))
        self.screen.blit(text, (10, 0))

    def writePassed(self):
        count = self.rock.passed
        font = pygame.font.Font('assets/fonts/NanumGothic.ttf', 20)
        text = font.render('놓친 운석 수: ' + str(count), True, (255, 0, 0))
        self.screen.blit(text, (340, 0))

    def writeMessage(self, text):
        textfont = pygame.font.Font('assets/fonts/NanumGothic.ttf', 80)
        text = textfont.render(text, True, (255, 0, 0))
        textpos = text.get_rect()
        textpos.center = (self.screen_width / 2, self.screen_height / 2)
        self.screen.blit(text, textpos)

        pygame.display.update()
        pygame.mixer.music.stop()
        self.gameOverSound.play()
        sleep(2)
        pygame.mixer.music.play(-1)
        self.playing = False

    def crash(self):
        self.writeMessage('전투기 파괴!')

    def gameOver(self):
        self.writeMessage('게임 오버!')

    def playGame(self):
        fighter_x = 0

        while True:
            self.drawObject(self.background, 0, 0)

            event = pygame.event.poll()
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighter_x -= 5

                elif event.key == pygame.K_RIGHT:
                    fighter_x += 5
                elif event.key == pygame.K_SPACE:  # 미사일을 발사한다.
                    self.missile.play()
                    self.missile.shoot(self.fighter)

            if event.type in [pygame.KEYUP]: # 키업일 경우 움직이지 않게 한다.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0

            if self.playing:  # 게임이 진행중이면
                self.fighter.x += fighter_x  # fighter 포지션 변경

                if self.rock.collision_check(self.fighter):  # fighter와 운석과의 충돌 테스트
                    self.crash()

                # fighter 를 그린다.
                self.fighter.draw()

                # 발사된 미사일이 있으면 좌표값을 올린다.
                if len(self.missile.shot) != 0:
                    for i, bxy in enumerate(self.missile.shot):
                        bxy[1] -= 10
                        self.missile.shot[i][1] = bxy[1]

                        # 운석과의 충돌 테스트
                        if bxy[1] < self.rock.y:
                            if self.rock.x < bxy[0] < self.rock.x + self.rock.width:
                                self.missile.shot.remove(bxy)
                                self.isShot = True
                                self.shotCount += 1

                        if bxy[1] <= 0:
                            try:
                                self.missile.shot.remove(bxy)  # 리스트에 있는 미사일을 삭제한다.
                            except:
                                pass

                self.missile.draw()  # 미사일을 그린다.

                self.rock.y += self.rock.speed

                if self.rock.y > self.screen_height:  # 놓친 경우
                    self.rock.create(True)

                if self.rock.passed == 3:  # 3번 놓치면 게임종결
                    self.gameOver()

                if self.isShot:  # 운석이 맞았으면 폭발이미지를 노출하고 운석속도를 좀더 빠르게 처리한다.
                    self.crashed.draw(self.rock.x, self.rock.y)
                    self.crashed.play()  # 폭발사운드 플레이

                    self.rock.create()  # 새로운 운석을 만들어 준다.
                    self.rock.speed_up()  # 운석의 떨어지는 속도를 올린다.
                    self.isShot = False

                self.rock.draw()
            else:  # 게임이 진행중이 아니면

                pass

            self.writeScore(self.shotCount)  # 스코어를 올린다.
            self.writePassed()  # 놓친 횟수 출력

            pygame.display.update()

            self.clock.tick(60)

if __name__ == '__main__':
   shooting = Shooting()
