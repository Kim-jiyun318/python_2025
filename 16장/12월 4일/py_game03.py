#3 게임 루프의 구조(화면이 꺼지지 않게 해보자)
import pygame

pygame.init()

# 화면 (디스플레이) 생성
WIDTH, HEIGHT = 600, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 3")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()