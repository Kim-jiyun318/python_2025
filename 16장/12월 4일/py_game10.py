#10 충돌 판정

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10")

clock = pygame.time.Clock() #FPS 제어 준비

#사용자 이미지 로드
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png") #캐릭터 이미지
        self.image = pygame.transform.scale(self.image, (50, 50)) #크기 조정
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        #화면 경계 제한
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 2
    
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 50 or self.rect.right > 200:
            self.speed_x *= -1

all_sprites = pygame.sprite.Group() #추가: Sprite 그룹 생성 및 Player / Enemy 추가
enemy_group = pygame.sprite.Group()  #추가: 적 전용 그룹

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260) #빨간 박스 근처(땅 위)에 위치
all_sprites.add(enemy)
enemy_group.add(enemy)

#추가: 코인(초록 원) 용 Rect - Rect 기반 충돌 예제용
coin_rect = pygame.Rect(430, 130, 40,40)
score = 0

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 

            running = False
    #변경: 게임 오버가 아닐 때만 움직임/충돌 처리
    if not game_over:
        all_sprites.update() #추가: game_over == False 일때만 업데이트
        
        #1) Rect 기반 충돌: 플레이어 vs 코인
        if player.rect.colliderect(coin_rect):
            print("코인 충돌!")
            score += 1
            coin_rect.x = 430 if score % 2 == 0 else 350
        
        #2) Sprite 그룹끼리 충돌: 플레이어 vs enemy_group
        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            print("적과 충돌! 게임 오버")
            game_over = True #추가: 창은 유지, 상태만 게임오버로

    #======== 그림 그리기 영역 ===========
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
    
    #초록 원(코인 느낌) - coin_rect 기준으로 중앙 잡기
    pygame.draw.circle(screen, (0, 255, 0),\
                       (coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2),\
                     20,)
    

    all_sprites.draw(screen) #추가: Sprite 그룹 그리기 (Player 포함)

    pygame.display.flip()
    clock.tick(60) 
pygame.quit()