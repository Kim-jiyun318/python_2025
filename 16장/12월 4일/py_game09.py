#9 Sprite 클래스 & 그룹 (중급 기본기)
#시험 때 이 코드가 주어진다
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9")

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

#추가: Sprite 그룹 생성 및 Player 추가
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    all_sprites.update() #추가: 스프라이트 그룹 업데이트(Player.update() 자동 호출)
    

    #======== 그림 그리기 영역 ===========
    screen.fill((170, 200, 255)) 
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60)) 
    pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40)) 
    pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20) 
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5) 

    all_sprites.draw(screen) #추가: Sprite 그룹 그리기 (Player 포함)

    pygame.display.flip()
    clock.tick(60) 
pygame.quit()