from tkinter import *
from tkinter import messagebox
import random
import time

tk = Tk()
tk.title("Bouncing Ball Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) 

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

lives = 5 #추가:남은 목숨 계산
score = 0
score_result = None
lives_result = None

class Ball:
    def __init__(self, canvas, paddle, color): 
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) 
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100) 

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts) 
        self.x = starts[0]  
        self.y = -3 

        self.canvas_height = self.canvas.winfo_height() 
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) 

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                global score
                score += 1
                return True
        return False
    
    def draw(self):
        global score_result, lives
        
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 

        if pos[1] <= 0:
            self.y = 3 
            
        if pos[3] >= self.canvas_height: 
            if not self.hit_bottom:
                lives -= 1 #추가:바닥에 닿을 때마다 목숨 차감
                if lives > 0: 
                    self.hit_bottom = True
                else:      #추가: 만약 목숨을 다 잃으면 게임 종료
                    self.hit_bottom = True

        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:
                self.y = -3 

        if pos[0] <= 0: 
            self.x = 3
        if pos[2] >= self.canvas_width: 
            self.x = -3

class Paddle: 
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0 
        self.canvas_width = self.canvas.winfo_width() 
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) 
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def stop(self, evt):
        self.x = 0

    def draw(self): 
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, 'blue') 
ball = Ball(canvas, paddle, 'red') 

score_result = canvas.create_text(50, 10, text=f"Score: {score}", font=("맑은 고딕", 16), fill='black')
lives_result = canvas.create_text(450, 10, text=f"Lives: {lives}", font=("맑은 고딕", 16), fill='red') #추가:남은 목숨 표시

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        
        canvas.itemconfig(score_result, text=f"Score: {score}")
        canvas.itemconfig(lives_result, text=f"Lives: {lives}") #추가:남은 목숨 표시(줄어든 만큼 표기 변경)

    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)

    if ball.hit_bottom == True:
        if lives > 0:
            
            canvas.delete(ball.id)
            canvas.delete(paddle.id)
            
            paddle = Paddle(canvas, 'blue') 
            ball = Ball(canvas, paddle, 'red')
            ball.hit_bottom = False
            
            tk.update()
            time.sleep(0.5)

        else:
            messagebox.showinfo("GAME OVER", f"GAME OVER! 최종 점수: {score}점\n버튼을 눌러 재시작")
            
            canvas.delete(ALL)
            
            score = 0
            lives = 5
            ball.hit_bottom = False
            
            paddle = Paddle(canvas, 'blue') 
            ball = Ball(canvas, paddle, 'red')
            
            score_result = canvas.create_text(50, 10, text=f"Score: {score}", font=("맑은 고딕", 16), fill='black')
            lives_result = canvas.create_text(450, 10, text=f"Lives: {lives}", font=("맑은 고딕", 16), fill='red') #캔버스에 표기
            
            tk.update()

tk.mainloop()