from tkinter import *
from tkinter import messagebox
import random
import time
import sys

WIDTH = 500
HEIGHT = 800
WINNING_SCORE = 5

tk = Tk()
tk.title("2인용 에어하키 게임")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) 

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0, bg='skyblue')
canvas.pack()
tk.update()

PLAYER_SCORE = [0, 0]
p1_score_result = None
p2_score_result = None

CENTER_LINE = HEIGHT // 2
GOAL_WIDTH = 150 
GOAL_HEIGHT = 10 
GOAL_CENTER = WIDTH // 2
GOAL_START = GOAL_CENTER - GOAL_WIDTH // 2
GOAL_END = GOAL_CENTER + GOAL_WIDTH // 2


class Puck:
    def __init__(self, canvas, paddle1, paddle2, color, radius=15): 
        self.canvas = canvas
        self.canvas_height = HEIGHT 
        self.canvas_width = WIDTH 
        self.id = canvas.create_oval(0, 0, radius * 2, radius * 2, fill=color) 
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.radius = radius
        
        self.reset_position()
        self.max_speed = 10
        
    def reset_position(self):
        x_start = self.canvas_width // 2 - self.radius
        y_start = self.canvas_height // 2 - self.radius
        self.canvas.coords(self.id, x_start, y_start, x_start + self.radius * 2, y_start + self.radius * 2)

        starts = [-4, -3, -2, 2, 3, 4]
        random.shuffle(starts) 
        self.x = starts[0]  
        self.y = random.choice([-3, 3])
        if abs(self.x) < 3: self.x = 3 if self.x > 0 else -3
        
    def hit_paddle(self, pos, paddle):
        paddle_pos = self.canvas.coords(paddle.id) 

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if (paddle.player_id == 1 and pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
                return True
            elif (paddle.player_id == 2 and pos[1] <= paddle_pos[3] and pos[1] >= paddle_pos[1]):
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 

        # 좌우에 위치한 벽에 부딪혔을때
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x *= -1 

        # 골대에 닿았을 때
        if pos[1] <= GOAL_HEIGHT and pos[0] >= GOAL_START and pos[2] <= GOAL_END:
            return "Goal_P1"
        if pos[3] >= HEIGHT - GOAL_HEIGHT and pos[0] >= GOAL_START and pos[2] <= GOAL_END:
            return "Goal_P2"
            
        # 골대쪽 벽에 부딪혔을 때
        if pos[1] <= 0: self.y *= -1
        if pos[3] >= self.canvas_height: self.y *= -1
            
        # 패들이 퍽을 쳐낼때(히트 판정)
        if self.hit_paddle(pos, self.paddle1):
            if self.y > 0: self.y *= -1
            center_x = (pos[0] + pos[2]) / 2
            paddle_center_x = (self.canvas.coords(self.paddle1.id)[0] + self.canvas.coords(self.paddle1.id)[2]) / 2
            diff = center_x - paddle_center_x
            self.x += diff * 0.2
            if abs(self.x) > self.max_speed: self.x = self.max_speed if self.x > 0 else -self.max_speed

        if self.hit_paddle(pos, self.paddle2):
            if self.y < 0: self.y *= -1
            center_x = (pos[0] + pos[2]) / 2
            paddle_center_x = (self.canvas.coords(self.paddle2.id)[0] + self.canvas.coords(self.paddle2.id)[2]) / 2
            diff = center_x - paddle_center_x
            self.x += diff * 0.2
            if abs(self.x) > self.max_speed: self.x = self.max_speed if self.x > 0 else -self.max_speed
        
        return None

class Paddle: 
    def __init__(self, canvas, color, y_start, width, height, controls, player_id, y_min, y_max):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.id = canvas.create_rectangle(0, 0, self.width, self.height, fill=color)
        self.canvas.move(self.id, WIDTH // 2 - self.width // 2, y_start)

        self.x_speed = 0 
        self.y_speed = 0
        self.canvas_width = WIDTH
        self.move_speed = 8
        self.player_id = player_id
        
        self.y_min = y_min
        self.y_max = y_max
        
        self.canvas.bind_all(f'<KeyPress-{controls["left"]}>', self.turn_left) 
        self.canvas.bind_all(f'<KeyPress-{controls["right"]}>', self.turn_right)
        self.canvas.bind_all(f'<KeyPress-{controls["up"]}>', self.turn_up)
        self.canvas.bind_all(f'<KeyPress-{controls["down"]}>', self.turn_down)
        self.canvas.bind_all(f'<KeyRelease-{controls["left"]}>', self.stop_x)
        self.canvas.bind_all(f'<KeyRelease-{controls["right"]}>', self.stop_x)
        self.canvas.bind_all(f'<KeyRelease-{controls["up"]}>', self.stop_y)
        self.canvas.bind_all(f'<KeyRelease-{controls["down"]}>', self.stop_y)

    def turn_left(self, evt): self.x_speed = -self.move_speed
    def turn_right(self, evt): self.x_speed = self.move_speed
    def turn_up(self, evt): self.y_speed = -self.move_speed
    def turn_down(self, evt): self.y_speed = self.move_speed

    def stop_x(self, evt):
        if evt.keysym in ("Left", "Right", "a", "d"): self.x_speed = 0
    def stop_y(self, evt):
        if evt.keysym in ("Up", "Down", "w", "s"): self.y_speed = 0

    def draw(self): 
        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id)
        
        # 좌우 캔버스를 벗어나지 않도록
        if pos[0] <= 0: self.canvas.move(self.id, -pos[0], 0)
        elif pos[2] >= self.canvas_width: self.canvas.move(self.id, self.canvas_width - pos[2], 0)
            
        # 자기 구역과 상하 캔버스를 벗어나지 않도록
        if pos[1] < self.y_min: self.canvas.move(self.id, 0, self.y_min - pos[1])
        elif pos[3] > self.y_max: self.canvas.move(self.id, 0, self.y_max - pos[3])



canvas.create_line(0, CENTER_LINE, WIDTH, CENTER_LINE, fill="white", dash=(4, 4), width=3)
# 골대 색깔
canvas.create_rectangle(GOAL_START, 0, GOAL_END, GOAL_HEIGHT, fill="black", outline="black", width=2)
canvas.create_rectangle(GOAL_START, HEIGHT - GOAL_HEIGHT, GOAL_END, HEIGHT, fill="black", outline="black", width=2)

# 패들 모양
paddle_width = 100
paddle_height = 15

# P1 (하단 구역) 범위 설정
p1_y_max = HEIGHT - 35
p1_y_min = CENTER_LINE + 10
p1_controls = {"left": "Left", "right": "Right", "up": "Up", "down": "Down"}
paddle1 = Paddle(canvas, 'blue', p1_y_max - paddle_height, paddle_width, paddle_height, p1_controls, 1, p1_y_min, p1_y_max) 

# P2 (상단) 범위 설정
p2_y_min = 35
p2_y_max = CENTER_LINE - 10
p2_controls = {"left": "a", "right": "d", "up": "w", "down": "s"}
paddle2 = Paddle(canvas, 'red', p2_y_min, paddle_width, paddle_height, p2_controls, 2, p2_y_min, p2_y_max) 

puck = Puck(canvas, paddle1, paddle2, 'white') 

# 점수 계산
score_font = ("맑은 고딕", 24, "bold")
p1_score_result = canvas.create_text(WIDTH - 50, CENTER_LINE + 30, text=f"{PLAYER_SCORE[0]}", font=score_font, fill='blue')
p2_score_result = canvas.create_text(50, CENTER_LINE - 30, text=f"{PLAYER_SCORE[1]}", font=score_font, fill='red')


while True:
    #퍽과 패들의 위치 갱신
    goal_result = puck.draw()
    
    paddle1.draw()
    paddle2.draw()

    #점수 갱신
    canvas.itemconfig(p1_score_result, text=f"{PLAYER_SCORE[0]}")
    canvas.itemconfig(p2_score_result, text=f"{PLAYER_SCORE[1]}")
    
    #득점 판정
    if goal_result:
        if goal_result == "Goal_P1":
            PLAYER_SCORE[0] += 1
            message = "Player 1 (하단) 득점!"
        elif goal_result == "Goal_P2":
            PLAYER_SCORE[1] += 1
            message = "Player 2 (상단) 득점!"

        # 승리 조건 검사(어느 한 쪽이 5점을 달성했다면)
        if PLAYER_SCORE[0] >= WINNING_SCORE or PLAYER_SCORE[1] >= WINNING_SCORE:
            winner = 1 if PLAYER_SCORE[0] >= WINNING_SCORE else 2
            
            messagebox.showinfo("게임 종료", f"플레이어 {winner} 승리! 최종 점수: {PLAYER_SCORE[0]} : {PLAYER_SCORE[1]}")
            
            # 게임 리셋
            canvas.delete(ALL) 
            PLAYER_SCORE = [0, 0]
            
            
            canvas.create_line(0, CENTER_LINE, WIDTH, CENTER_LINE, fill="white", dash=(4, 4), width=3)
            
            canvas.create_rectangle(GOAL_START, 0, GOAL_END, GOAL_HEIGHT, fill="black", outline="black", width=2)
            canvas.create_rectangle(GOAL_START, HEIGHT - GOAL_HEIGHT, GOAL_END, HEIGHT, fill="black", outline="black", width=2)

            paddle1 = Paddle(canvas, 'blue', p1_y_max - paddle_height, paddle_width, paddle_height, p1_controls, 1, p1_y_min, p1_y_max) 
            paddle2 = Paddle(canvas, 'red', p2_y_min, paddle_width, paddle_height, p2_controls, 2, p2_y_min, p2_y_max) 
            puck = Puck(canvas, paddle1, paddle2, 'white') 
            
            p1_score_result = canvas.create_text(WIDTH - 50, CENTER_LINE + 30, text=f"{PLAYER_SCORE[0]}", font=score_font, fill='blue')
            p2_score_result = canvas.create_text(50, CENTER_LINE - 30, text=f"{PLAYER_SCORE[1]}", font=score_font, fill='red')

        else: #득점만 하고 5점에 도달하지 못했다면
            messagebox.showinfo("득점", message)
            
            canvas.delete(puck.id)
            canvas.delete(paddle1.id)
            canvas.delete(paddle2.id)
            
            paddle1 = Paddle(canvas, 'blue', p1_y_max - paddle_height, paddle_width, paddle_height, p1_controls, 1, p1_y_min, p1_y_max) 
            paddle2 = Paddle(canvas, 'red', p2_y_min, paddle_width, paddle_height, p2_controls, 2, p2_y_min, p2_y_max) 
            puck = Puck(canvas, paddle1, paddle2, 'white')
            
            canvas.itemconfig(p1_score_result, text=f"{PLAYER_SCORE[0]}")
            canvas.itemconfig(p2_score_result, text=f"{PLAYER_SCORE[1]}")
            
            tk.update()
            time.sleep(1)

 
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)
tk.mainloop()