# 이미지 처리
- blit : "bit block transfer"의 약어(shortand)이며 한 memory로 부터 다른 memory로 data block을 전송하는 process이다. 
```

# 이미지 파일을 로딩
img = pygame.image.load('assets/sample.jpg')

while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)  # r g b 로 윈도우 채움

    # # 이미지 파일 그리기
    # screen.blit(img, (50, 100))

    # 이미지 파일 회전하여 그리기
    x = 200
    y = 100
    degree = 10
    rotated = pygame.transform.rotate(img, degree)  # 이미지를 회전한다.
    rect = rotated.get_rect()  # get_rect(centerx=300, bottom=800) # get_rect(topleft=(100, 300))
    # print('rect:', rect)
    # < rect(0, 0, 864, 1004) >
    rect.center = (x, y)
    # print('rect:', rect)
    # <rect(-232, -402, 864, 1004)>
    screen.blit(rotated, rect)


    clock.tick(30) # 초당 30 fps를 위해 딜레이를 추가
    pygame.display.flip()  # 화면 전체를 업데이트
```
