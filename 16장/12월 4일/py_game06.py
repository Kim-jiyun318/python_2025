#6 Surface와 Rect(이미지적용버전)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6")

#사용자 이미지 로드
img = pygame.image.load("dukbird.png") #<-여기에 파일 이름 입력!(현재 파일보다 상위 폴더에 파일을 넣어야 함)
img = pygame.transform.scale(img, (50, 50)) #<-크기 조절(원한다면)
rect = img.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    #실시간 키 입력(get_pressed)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # 화면 경계 제한
    if rect.left < 0:
        rect.left = 0
    if rect.right > WIDTH:
        rect.right = WIDTH
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT
    
    #화면 그리기
    screen.fill((200, 200, 200))
    screen.blit(img, rect) #네모 대신 이미지 그리기
    pygame.display.flip()

pygame.quit()