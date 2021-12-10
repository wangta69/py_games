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

    while True:
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        # update
        pygame.display.update()
        fps.tick(30)  # 초당 30번 실행

if __name__ == '__main__':
    main()
