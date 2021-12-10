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

    # tree
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

        screen.fill(WHITE)

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:  # 만약 나무가 화면의 좌측끝(맨앞) 으로 오면 다시 화면의 뒤로 이동시킨다.
            tree_x = screen_width

        # draw tree
        screen.blit(tree, (tree_x, tree_y))

        # update
        pygame.display.update()
        fps.tick(30)  # 초당 30번 실행



if __name__ == '__main__':
    main()
