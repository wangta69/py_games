import pygame # 파이 게임 모듈 임포트
import random
import copy

pygame.init() # 파이 게임 초기화
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정
clock = pygame.time.Clock()

# 변수
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
large_font = pygame.font.Font('../../assets/fonts/NanumGothic.ttf', 72)
small_font = pygame.font.Font('../../assets/fonts/NanumGothic.ttf', 36)
# large_font = pygame.font.SysFont('arial', 72)
# small_font = pygame.font.SysFont('arial', 36)

print(pygame.font.get_fonts())
score = 0
game_over = False

airplane_image = pygame.image.load('../../assets/images/airplane.png')
airplane_image = pygame.transform.scale(airplane_image, (100, 100)) # 이미지 크기 지정
airplane = airplane_image.get_rect(left=0, centery=SCREEN_HEIGHT // 2)
airplane_dy = 2

# 폭발 이미지
explosion_image = pygame.image.load('../../assets/images/explosion.png')  # .convert_alpha()

# 동굴 그리기 시작
rects = []
for column_index in range(80):
    rect = pygame.Rect(column_index * 10, 100, 10, 400)
    rects.append(rect)
# 동굴 그리기 끝
slope = 2 # 동굴의 기울기 설정

while True: # 게임 루프
    screen.fill(GREEN)

    event = pygame.event.poll() # 이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:  # 눌려진 키가 space 일 경우 위로 방향을 바꾼다.
            airplane_dy = -5
    elif event.type == pygame.KEYUP:  # space up 일경우 아래로 방향을 바꾼다.
        if event.key == pygame.K_SPACE:
            airplane_dy = 5

    if not game_over:
        # 시간경과시 스코어를 올린다.
        score += 1

        # 새로운 동굴을 추가한다.
        new_rect = copy.deepcopy(rects[-1])
        test_rect = copy.deepcopy(rects[-1])
        test_rect.top = test_rect.top + slope
        if test_rect.top <= 0 or test_rect.bottom >= SCREEN_HEIGHT:
            slope = random.randint(2, 6) * (-1 if slope > 0 else 1)  # 반대 방향으로 기울어 지게 하기
            new_rect.height = new_rect.height + -20  # 동굴 좁아지게 하기
        new_rect.left = new_rect.left + 10
        new_rect.top = new_rect.top + slope  # 동굴을 기울인다.
        rects.append(new_rect)

        # 동굴을 움직인다.
        for rect in rects:
            rect.left = rect.left - 10
        del rects[0]

        # 비행기의 위치를 바꾼다.
        airplane.top += airplane_dy

        # 비행기가 동굴의 top이나 bottom에 다으면 게임 종료
        if airplane.top < rects[0].top or airplane.bottom > rects[0].bottom:
            game_over = True

    # 화면 그리기
    # 화면에 동굴을 그린다.(위에서 생성한 rects 를 이용)
    for rect in rects:
        pygame.draw.rect(screen, BLACK, rect)
    screen.blit(airplane_image, airplane)

    # 스코어 디스플레이이
    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    if game_over == True:
        screen.blit(explosion_image, (0, airplane.top - 40))

        game_over_image = large_font.render('게임 종료', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))


    pygame.display.update() # 모든 화면 그리기 업데이트
    clock.tick(15) # 30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit()