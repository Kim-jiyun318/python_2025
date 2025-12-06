#10번 하기

from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) #게임창이 항상 위로 있도록

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas #접근가능해야 함
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.paddle = paddle   #패들 객체 기억하도록 수정
        self.canvas.move(self.id, 245, 100) #canvas.move(객체ID, X방향이동, Y방향이동)

        #공의 속도, 좌우로 움직이던 것을 *수정
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts) #리스트 순서 섞기
        self.x = starts[0]     #섞인 리스트의 첫 번째 값을 사용
        
        self.y = -3 #위로 올라감(-3의 속도로 시작)

        #캔버스 높이 저장(공이 부딪히는 판정의 거리)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() #수정
    
    #추가: 공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self, pos):         #self를 따로 생각하면 안 되는 건가 봐??
        paddle_pos = self.canvas.coords(self.paddle.id) #패들의 위치 좌표 가져오기

        #가로 방향으로 공과 패들이 겹치는지 확인
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: #공의 아래쪽(y2)이 패들의  위, 아래 사이에 있는지 확인
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):#수정(06번 판)
        self.canvas.move(self.id, self.x, self.y) #매 프레임 공이 위로 1픽셀씩
        pos = self.canvas.coords(self.id) #현재 공의 위치 가져오기 [x1, y1, x2, y2]
        #print(self.canvas.coords(self.id)) coords는 좌표값

        if pos[1] <= 0: #천장에 닿음 -> 아래로 방향 전환
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        #여기까지는 위아래로만 움직였지만...

        #추가: 패들과 부딪혔는지 검사
        if self.hit_paddle(pos) == True:
            self.y = -3

        if pos[0] <=0: #왼쪽 벽에 닿으면-> 오른쪽으로 튕김
            self.x = 3
        if pos[2] >= self.canvas_width: #오른쪽 벽에 닿으면-> 왼쪽으로 튕김
            self.x = -3
            
class Paddle: #패들 클래스 추가
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0 #처음에는 가만히!
        self.canvas_width = self.canvas.winfo_width() #벽에 부딪히는 거리를 계산하기 위한 너비 저장

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2 #왼쪽으로 이동하는 속도
    
    def turn_right(self, evt):
        self.x = 2 #오른쪽으로 이동하는 속도
    
    def draw(self): #패들을 x축에서만 이동
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        #화면 왼쪽/오른쪽 끝을 넘지 않게 막기
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

paddle = Paddle(canvas, 'blue') #수정-패들 먼저 생성하기 위해 볼 객체와 패들 객체 위치를 서로 바꿔주었다.
ball = Ball(canvas, paddle, 'red') #수정 #왜 paddle까지 전달할까?

while True:
    ball.draw()
    paddle.draw() #추가
    tk.update_idletasks() #tkinter 내부 작업 처리
    tk.update()
    time.sleep(0.01)

tk.mainloop()