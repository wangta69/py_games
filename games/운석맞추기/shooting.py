import pygame
import random
from time import sleep

screen_width = 480
screen_height = 640

# color
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyShooting')
background = pygame.image.load('assets/images/background.png')
fighter =  pygame.image.load('assets/images/fighter.png')
missile = pygame.image.load('assets/images/missile.png')
explosion = pygame.image.load('assets/images/explosion.png')
pygame.mixer.music.load('assets/sounds/music.wav')
pygame.mixer.music.play(-1)
missileSound = pygame.mixer.Sound('assets/sounds/missile.wav')
gameOverSound = pygame.mixer.Sound('assets/sounds/gameover.wav')
clock = pygame.time.Clock()

rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',
             'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',
             'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',
             'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',
             'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',
             'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']
explosionSound = ['explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav']

def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))

def writeScore(count):
    global screen
    font = pygame.font.Font('assets/fonts/NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수: ' + str(count), True, (255, 255, 255))
    screen.blit(text, (10, 0))

def writePassed(count):
    global screen
    font = pygame.font.Font('assets/fonts/NanumGothic.ttf', 20)
    text = font.render('놓친 운석 수: ' + str(count), True, (255, 0, 0))
    screen.blit(text, (340, 0))

def writeMessage(text):
    textfont = pygame.font.Font('assets/fonts/NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (screen_width/2, screen_height/2)
    screen.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)

def crash():
    global screen
    writeMessage('전투기 파괴!')

def gameOver():
    global screen
    writeMessage('게임 오버!')

def loadRock():
    return pygame.image.load('assets/images/' + random.choice(rockImage))

# def explosion():
def crashSound():
    return pygame.mixer.Sound('assets/sounds/' + random.choice(explosionSound))

fighterSize = fighter.get_rect().size
fighterWidth = fighterSize[0]
fighterHeight = fighterSize[1]

x = screen_width *0.45
y = screen_height * 0.9
fighterX = 0

missileXY = []

rock = loadRock()
rockSize = rock.get_rect().size
rockWidth = rockSize[0]
rockHeight = rockSize[1]
destroySound = crashSound()

rockX = random.randrange(0, screen_width - rockWidth)
rockY = 0
rockSpeed = 2

isShot = False
shotCount = 0
rockPassed = 0

while True:
    drawObject(background, 0, 0)

    event = pygame.event.poll()
    if event.type in [pygame.QUIT]:
        break

    if event.type in [pygame.KEYDOWN]:
        if event.key == pygame.K_LEFT:
            fighterX -= 5
        elif event.key == pygame.K_RIGHT:
            fighterX += 5
        elif event.key == pygame.K_SPACE:
            missileSound.play()
            missileX = x + fighterWidth/2
            missileY = y - fighterHeight
            missileXY.append([missileX, missileY])

    if event.type in [pygame.KEYUP]:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            fighterX = 0

    x += fighterX
    if x < 0:
        x = 0
    elif x > screen_width - fighterWidth:
        x = screen_width - fighterWidth

    if y < rockY + rockHeight:
        if (rockX > x and rockX < x + fighterWidth) or \
        (rockX + rockWidth > x  and rockX + rockWidth < x + fighterWidth):
            crash()

    drawObject(fighter, x, y)

    if len(missileXY) != 0:
        for i, bxy in enumerate(missileXY):
            bxy[1] -= 10
            missileXY[i][1] = bxy[1]

            if bxy[1] < rockY:
                if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                    missileXY.remove(bxy)
                    isShot = True
                    shotCount += 1

            if bxy[1] <= 0:
                try:
                    missileXY.remove(bxy)
                except:
                    pass

    if len(missileXY) != 0:
        for bx, by in missileXY:
            drawObject(missile, bx, by)

    writeScore(shotCount)

    rockY += rockSpeed

    if rockY > screen_height:
        rock = loadRock()
        rockSize = rock.get_rect().size
        rockWidth = rockSize[0]
        rockHeight = rockSize[1]
        rockX = random.randrange(0, screen_width - rockWidth)
        rockY = 0
        rockPassed += 1

    if rockPassed == 3:
        gameOver()

    writePassed(rockPassed)

    if isShot:
        drawObject(explosion, rockX, rockY)
        destroySound.play()

        rock = loadRock()
        rockSize = rock.get_rect().size
        rockWidth = rockSize[0]
        rockHeight = rockSize[1]
        rockX = random.randrange(0, screen_width, rockWidth)
        rockY = 0
        destroySound = crashSound()
        isShot = False

        rockSpeed += 0.02
        if rockSpeed >= 10:
            rockSpeed = 10

    drawObject(rock, rockX, rockY)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
