import pygame
import random
import sys

WIDTH = 500
HEIGHT = 800
WINNING_SCORE = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2인용 에어하키 게임 (Pygame)")

clock = pygame.time.Clock()

#변수 선언
PLAYER_SCORE = [0, 0]

CENTER_LINE = HEIGHT // 2
GOAL_WIDTH = 150 
GOAL_HEIGHT = 10 
GOAL_CENTER = WIDTH // 2
GOAL_START = GOAL_CENTER - GOAL_WIDTH // 2
GOAL_END = GOAL_CENTER + GOAL_WIDTH // 2

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKYBLUE = (135, 206, 235)

font = pygame.font.Font(None, 48)
large_font = pygame.font.Font(None, 72)

#클래스 설정

class Puck:
    def __init__(self, screen, paddle1, paddle2, color, radius=15): 
        self.screen = screen
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.color = color
        self.radius = radius
        
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)

        self.max_speed = 10
        self.x_speed = 0
        self.y_speed = 0
        
        self.reset_position()
        
    def reset_position(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        starts = [-4, -3, -2, 2, 3, 4]
        random.shuffle(starts) 
        self.x_speed = starts[0]  
        self.y_speed = random.choice([-3, 3])
        if abs(self.x_speed) < 3: self.x_speed = 3 if self.x_speed > 0 else -3
        
    def hit_paddle(self, paddle): # 수직 방향 (상단/하단) 충돌 감지
        if self.rect.colliderect(paddle.rect):
            if paddle.player_id == 1 and self.y_speed > 0:
                if self.rect.bottom >= paddle.rect.top and self.rect.centery < paddle.rect.centery + self.radius:
                    return True
            elif paddle.player_id == 2 and self.y_speed < 0:
                if self.rect.top <= paddle.rect.bottom and self.rect.centery > paddle.rect.centery - self.radius:
                    return True
        return False
        
    def hit_paddle_side(self, paddle): # 수평 방향 (측면) 충돌 감지
        if self.rect.colliderect(paddle.rect):
            
            is_vertical_overlap = (self.rect.bottom > paddle.rect.top and self.rect.top < paddle.rect.bottom)
            
            if paddle.player_id == 1 and self.rect.centery > CENTER_LINE and is_vertical_overlap:
                if self.x_speed < 0 and self.rect.left <= paddle.rect.right and self.rect.left > paddle.rect.centerx: 
                    return True
                elif self.x_speed > 0 and self.rect.right >= paddle.rect.left and self.rect.right < paddle.rect.centerx:
                    return True

            elif paddle.player_id == 2 and self.rect.centery < CENTER_LINE and is_vertical_overlap:
                if self.x_speed < 0 and self.rect.left <= paddle.rect.right and self.rect.left > paddle.rect.centerx:
                    return True
                elif self.x_speed > 0 and self.rect.right >= paddle.rect.left and self.rect.right < paddle.rect.centerx:
                    return True
        return False


    def draw(self):
        # 퍽의 위치를 속도만큼 업데이트
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        # 좌우 벽 충돌 처리
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_speed *= -1
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.x_speed *= -1

        # 골대 충돌 처리
        if self.rect.top <= GOAL_HEIGHT and GOAL_START <= self.rect.centerx <= GOAL_END:
            return "Goal_P1"
        if self.rect.bottom >= HEIGHT - GOAL_HEIGHT and GOAL_START <= self.rect.centerx <= GOAL_END:
            return "Goal_P2"
            
        # 벽 충돌 처리 (골대 영역 밖의 상단/하단 벽)
        if self.rect.top <= 0: self.y_speed *= -1
        if self.rect.bottom >= HEIGHT: self.y_speed *= -1
            
        
        #패들 충돌 처리
        # P1 (하단 패들) 충돌
        if self.hit_paddle(self.paddle1):
            self.y_speed *= -1
            center_x = self.rect.centerx
            paddle_center_x = self.paddle1.rect.centerx
            diff = center_x - paddle_center_x
            self.x_speed += diff * 0.2
            if abs(self.x_speed) > self.max_speed: self.x_speed = self.max_speed if self.x_speed > 0 else -self.max_speed

        # P2 (상단 패들) 충돌
        if self.hit_paddle(self.paddle2):
            self.y_speed *= -1
            center_x = self.rect.centerx
            paddle_center_x = self.paddle2.rect.centerx
            diff = center_x - paddle_center_x
            self.x_speed += diff * 0.2
            if abs(self.x_speed) > self.max_speed: self.x_speed = self.max_speed if self.x_speed > 0 else -self.max_speed

        # P1/P2 측면 충돌 (수평 충돌)
        if self.hit_paddle_side(self.paddle1) or self.hit_paddle_side(self.paddle2):
            self.x_speed *= -1
            
        # 퍽 그리기
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)
        
        return None

class Paddle: 
    def __init__(self, screen, color, y_start, width, height, controls, player_id, y_min, y_max):
        self.screen = screen
        self.color = color
        self.player_id = player_id
        
        self.rect = pygame.Rect(WIDTH // 2 - width // 2, y_start, width, height)

        self.x_speed = 0 
        self.y_speed = 0
        self.move_speed = 8
        
        self.y_min = y_min
        self.y_max = y_max
        
        self.controls = controls
        
    def set_speed(self, key, is_pressed):
        if key == self.controls["left"]: self.x_speed = -self.move_speed if is_pressed else 0
        if key == self.controls["right"]: self.x_speed = self.move_speed if is_pressed else 0
        if key == self.controls["up"]: self.y_speed = -self.move_speed if is_pressed else 0
        if key == self.controls["down"]: self.y_speed = self.move_speed if is_pressed else 0

    def draw(self): 
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        if self.rect.left <= 0: self.rect.left = 0
        elif self.rect.right >= WIDTH: self.rect.right = WIDTH
            
        if self.rect.top < self.y_min: self.rect.top = self.y_min
        elif self.rect.bottom > self.y_max: self.rect.bottom = self.y_max

        pygame.draw.rect(self.screen, self.color, self.rect)

def draw_field(screen):
    screen.fill(SKYBLUE)
    pygame.draw.line(screen, WHITE, (0, CENTER_LINE), (WIDTH, CENTER_LINE), 3)
    pygame.draw.rect(screen, BLACK, (GOAL_START, 0, GOAL_WIDTH, GOAL_HEIGHT))
    pygame.draw.rect(screen, BLACK, (GOAL_START, HEIGHT - GOAL_HEIGHT, GOAL_WIDTH, GOAL_HEIGHT))

def display_scores(screen, p1_score, p2_score):
    p1_text = font.render(str(p1_score), True, BLUE)
    p2_text = font.render(str(p2_score), True, RED)
    
    screen.blit(p1_text, (WIDTH - 50, CENTER_LINE + 10))
    screen.blit(p2_text, (50, CENTER_LINE - 50))



paddle_width = 100
paddle_height = 15

p1_y_max = HEIGHT - 35
p1_y_min = CENTER_LINE + 10
p1_controls = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN}
paddle1 = Paddle(screen, BLUE, p1_y_max - paddle_height, paddle_width, paddle_height, p1_controls, 1, p1_y_min, p1_y_max) 

p2_y_min = 35
p2_y_max = CENTER_LINE - 10
p2_controls = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s}
paddle2 = Paddle(screen, RED, p2_y_min, paddle_width, paddle_height, p2_controls, 2, p2_y_min, p2_y_max) 

puck = Puck(screen, paddle1, paddle2, WHITE) 

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            paddle1.set_speed(event.key, True)
            paddle2.set_speed(event.key, True)
        
        if event.type == pygame.KEYUP:
            paddle1.set_speed(event.key, False)
            paddle2.set_speed(event.key, False)
    
    # 필드 그리기
    draw_field(screen)

    # 퍽 움직임 및 득점 확인
    goal_result = puck.draw()
    
    # 패들 움직임 및 그리기
    paddle1.draw()
    paddle2.draw()

    # 득점 및 승리 조건 처리
    if goal_result:
        if goal_result == "Goal_P1":
            PLAYER_SCORE[0] += 1
        elif goal_result == "Goal_P2":
            PLAYER_SCORE[1] += 1

        if PLAYER_SCORE[0] >= WINNING_SCORE or PLAYER_SCORE[1] >= WINNING_SCORE:
            winner = 1 if PLAYER_SCORE[0] >= WINNING_SCORE else 2
            
            # 최종 승리 문구 및 점수 표시 로직
            win_message = f" {PLAYER_SCORE[0]}  :  {PLAYER_SCORE[1]}"
            win_text = large_font.render(win_message, True, BLACK)
            text_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

            draw_field(screen)
            screen.blit(win_text, text_rect)
            pygame.display.flip()

            pygame.time.wait(2000) 
            running = False

        else:
            paddle1 = Paddle(screen, BLUE, p1_y_max - paddle_height, paddle_width, paddle_height, p1_controls, 1, p1_y_min, p1_y_max) 
            paddle2 = Paddle(screen, RED, p2_y_min, paddle_width, paddle_height, p2_controls, 2, p2_y_min, p2_y_max) 
            puck = Puck(screen, paddle1, paddle2, WHITE)
            
            pygame.display.flip()
            pygame.time.wait(1000)

    # 점수 계산
    display_scores(screen, PLAYER_SCORE[0], PLAYER_SCORE[1])

    #  화면 업데이트와 fps
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()