import sys
import pygame
import random

class Fighter:
    """
    fighter class
    """
    def __init__(self, parent):  # 초기화시 Shooting 게임의 screen 정보를 가져온다.
        self.screen = parent.screen
        self.screen_width = parent.screen.get_width()
        self.screen_height = parent.screen.get_height()
        self.fighter = pygame.image.load('assets/images/fighter.png')
        
        # fighter 의 크기
        size = self.fighter.get_rect().size
        self.width = size[0]
        self.height = size[1]

        # fighter 초기 위치 설정
        self.x = self.screen_width * 0.45
        self.y = self.screen_height * 0.9  # 지구위에 놓이게 bottom에서 약간 띄운다

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
    def __init__(self, parent):
        self.screen = parent.screen
        self.rock = parent.rock
        self.smash = parent.smash
        self.dashboard = parent.dashboard
        self.missile = pygame.image.load('assets/images/missile.png')
        self.sound = pygame.mixer.Sound('assets/sounds/missile.wav')
        self.fired = []  # 발사된 미사일 좌표 (여러개)

    # 미사일을 그린다.
    def draw(self):
        if len(self.fired) != 0:
            for i, bxy in enumerate(self.fired):
                bxy[1] -= 10  # 미사일의 y 좌표값을 변경한다.
                self.screen.blit(self.missile, (bxy[0], bxy[1]))

                if bxy[1] < self.rock.y:  # 운석과의 충돌 테스트
                    if self.rock.x < bxy[0] < self.rock.x + self.rock.width:
                        self.smash.play()  # smash 사운드
                        self.smash.set_timer(self.rock.x, self.rock.y)  # smash에 timer를 작동시킨다.
                        self.dashboard.score += 1  # dashboard score를 올린다.
                        self.fired.remove(bxy)  # 미사일을 삭제한다.
                        self.rock.create()  # 새로운 운석을 만들어 준다.
                        self.rock.speed_up()  # 운석의 떨어지는 속도를 올린다.

                if bxy[1] <= 0:  # 화면에서 사라진 경우
                    try:
                        self.fired.remove(bxy)  # 리스트에 있는 미사일을 삭제한다.
                    except IndexError as e:
                        pass

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
    def __init__(self, parent):
        self.screen = parent.screen
        self.fighter = parent.fighter
        self.dashboard = parent.dashboard
        self.screen_width = parent.screen.get_width()
        self.screen_height = parent.screen.get_height()
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
            self.dashboard.missed += 1  # 놓친 숫자를 올니다.

        self.screen.blit(self.rock, (self.x, self.y))

    def collision_check(self):  # fighter와 충돌테스트
        rock = self.__collision_attr()
        obj2 = self.__collision_attr(self.fighter)
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
        self.speed += 0.2  # 속도를 0.2 만큼 올린다.
        if self.speed >= 10:  # 속도가 10보다 크면 10으로 유지한다.
            self.speed = 10

class Smash:
    """
    운석파괴
    """

    def __init__(self, parent):
        self.screen = parent.screen
        self.x = 0
        self.y = 0
        self.timer = 0

        self.sounds = [
            'explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav'
        ]

        self.explosion = pygame.image.load('assets/images/explosion.png')

    def draw(self):
        if self.timer != 0:
            self.screen.blit(self.explosion, (self.x, self.y))
            seconds = (pygame.time.get_ticks() - self.timer) / 1000
            if seconds > 0.05:
                self.timer = 0

    # 다양한 폭발 사운드 플레이
    def play(self):
        sound = pygame.mixer.Sound('assets/sounds/' + random.choice(self.sounds))
        sound.play()

    def set_timer(self, x, y):
        self.x = x
        self.y = y
        self.timer = pygame.time.get_ticks()
        pass


class Dashboard:
    def __init__(self, parent):
        self.screen = parent.screen
        self.screen_width = parent.screen.get_width()
        self.screen_height = parent.screen.get_height()

        self.font20 = pygame.font.Font('assets/fonts/NanumGothic.ttf', 20)
        self.font80 = pygame.font.Font('assets/fonts/NanumGothic.ttf', 80)
        self.gameOverSound = pygame.mixer.Sound('assets/sounds/gameover.wav')

        self.missed = 0  # 놓친 운석수
        self.score = 0  # 파괴한 운석수
        self.end = False
        self.message = ''

    def draw(self):
        self.diplay_score()
        self.dispaly_missed()
        self.display_message()
        
    def diplay_score(self):
        text = self.font20.render('파괴한 운석 수: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (10, 0))

    def dispaly_missed(self):
        text = self.font20.render('놓친 운석 수: ' + str(self.missed), True, (255, 0, 0))
        self.screen.blit(text, (340, 0))

    def set_end(self, message):
        self.end = True
        self.message = message

    def display_message(self):
        if self.end:
            text = self.font80.render(self.message, True, (255, 0, 0))
            text_pos = text.get_rect()
            text_pos.center = (self.screen_width / 2, self.screen_height / 2)
            self.screen.blit(text, text_pos)
            
            pygame.mixer.music.stop()  # 기존 음악 삭제
            self.gameOverSound.play()  # 게임 종료음 출력
            pygame.mixer.music.play(-1)


class Shooting:
    def __init__(self):
        # 변수 초기화
        self.screen = None
        self.screen_width = 480
        self.screen_height = 640

        self.background = None  # 백그라운드 이미지
        self.clock = None  # Clock

        self.fighter = None  # 비행기 객체
        self.rock = None  # 운석 객체
        self.smash = None  # 운석폭발 효과
        self.missile = None  # 미사일 객체
        self.dashboard = None  # 대쉬보드 객체

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
        # 배경사운드 설정
        pygame.mixer.music.load('assets/sounds/music.wav')
        pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()
        
        # 객체생성
        self.dashboard = Dashboard(self)
        self.fighter = Fighter(self)  # fighter 객체생성
        self.rock = Rock(self)  # rock 객체생성
        self.rock.create()  # 운석을 만든다
        self.smash = Smash(self)  # smash 객체생성
        self.missile = Missile(self)  # missile 객체생성 (반드시 rock 객체 생성후 넣어둔다.)



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

            if event.type in [pygame.KEYUP]:  # 키업일 경우.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter_x = 0

            self.drawObject(self.background, 0, 0)
            if self.dashboard.missed == 3:  # 운석을 3번 놓치면 게임종료
                self.dashboard.set_end('게임 오버!')
                self.playing = False
                
            if self.playing:  # 게임이 진행중이면
                self.fighter.x += fighter_x  # fighter 포지션 변경

                if self.rock.collision_check():  # fighter와 운석과의 충돌 테스트
                    self.dashboard.set_end('전투기 파괴!')
                    self.playing = False

                self.fighter.draw()  # fighter 를 그린다.
                self.missile.draw()  # 미사일을 그린다.
                self.rock.draw()  # 운석을 그린다.
                self.smash.draw()  # 폭발효과를 그린다.
                self.dashboard.draw()  # 대쉬보드(파괴한 운석수, 놓친 운석수)를 표시
            else:  # 게임이 진행중이 아니면
                self.dashboard.draw()  # 대쉬보드(파괴한 운석수, 놓친 운석수)를 표시
                pass

            pygame.display.update()
            self.clock.tick(60)  # 초당 60회로 fps 설정


if __name__ == '__main__':
   shooting = Shooting()  # 클래스 호출시 클래스내의 __init__(self): 부분은 자동실행된다.
