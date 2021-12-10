import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping Dino')
screen_width = 800
screen_height = 400

# color
WHITE = (255, 255, 255)

def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    fps = pygame.time.Clock()

    # dinosour image
    dinosour1 = pygame.image.load('assets/images/dino1.png')
    dinosour2 = pygame.image.load('assets/images/dino2.png')
    dino_height = dinosour1.get_size()[1]
    dino_bottom = screen_height - dino_height
    dino_x = 50
    dino_y = dino_bottom
    leg_swap = True
    jump_top = 200  # 점프를 하면 200까지 올린다.
    is_bottom = True  # 점프중인지 아닌지 확인
    is_go_up = False  # 올라가는 중인지 내려오는 중인지 확인

    # tree image
    tree = pygame.image.load('assets/images/tree.png')
    tree_height = tree.get_size()[1]  # (width, height)
    tree_x = screen_width  # x 는 화면에 끝에 둔다
    tree_y = screen_height - tree_height  # y 는 화면의 높이에서 tree의 높이를 뺀 위치에 둔다.

    while True:
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:  # 키보드를 누를때 현재 공룔이 바닥에 있으면
                    is_go_up = True
                    is_bottom = False

        # dino jumping
        if is_go_up:  # 위로 올라가는 중이면
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:  # 내려오지만 아직 바닥이 아닌 경우는
            dino_y += 10.0

        # dino top and bottom check
        if is_go_up and dino_y <= jump_top:  # 올라가는 중이고 점핑 한계에 도달하면
            is_go_up = False
            
        if not is_bottom and dino_y >= dino_bottom:  # 바닥보다 아래면
            is_bottom = True
            dino_y = dino_bottom

        screen.fill(WHITE)

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:  # 만약 나무가 화면의 좌측끝(맨앞) 으로 오면 다시 화면의 뒤로 이동시킨다.
            tree_x = screen_width

        # draw tree
        screen.blit(tree, (tree_x, tree_y))

        # draw dino : 번갈아 공룡이미지를 표현
        if leg_swap:
            screen.blit(dinosour1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(dinosour2, (dino_x, dino_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(30)  # 초당 30번 실행


if __name__ == '__main__':
    main()
