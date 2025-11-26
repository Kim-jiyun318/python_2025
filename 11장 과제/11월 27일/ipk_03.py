#이것도 중요!! 오버라이딩이랑 그리는 과정을 잘 숙지하자
from tkinter import *
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self): raise NotImplementedError
        #pass
    def perimeter(self): raise NotImplementedError
        #pass
    def draw(self, canvas): raise NotImplementedError
        #pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.w = w
        self.h = h
        super().__init__(x, y)
    
    def area(self): return self.w * self.h #이런 방법이 있구나
    
    def perimeter(self): return 2 * (self.w + self.h)
    
    def draw(self, canvas):
        #canvas.create_rectangle(50, 50, 110, 110, fill = "tomato")
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = "tomato")
        #좌표를 계산하는 게 X, 가로(폭)와 세로(높이)의 개념끼리 더했다.

class Circle(Shape):
    def __init__(self, x, y, r):
        self.r = r
        super().__init__(x, y)
    
    def area(self): return math.pi * self.r * self.r
    
    def perimeter(self): return 2 * math.pi * self.r
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = "skyblue") #왼쪽 위/오른쪽 아래를 각각 계산
        #반지름만큼 중심에서 이동하는 원리이다.
    
#tkinter
root = Tk()
root.title("문제3")
#root.geometry("300x400") 창 자체의 크기가 아니라 캔버스 크기였다. 어쩐지

canvas = Canvas(root, width=300, height=220, bg = "white")
canvas.pack()

var = StringVar(value="rect")
info = StringVar(value="도형을 선택하고 그리기를 누르세요.")
'''
label2 = Label(root, textvariable = info) #엑? 이게 아니라고?
label2.pack(pady=10)
'''
Label(root, textvariable=info).pack()

frame = Frame(root); frame.pack(anchor="center") #이렇게 한줄로 만들 수 있네

'''
shape_var = IntVar()
Radiobutton(frame, text="사각형" , value=1 , variable=shape_var).pack(side="left")
Radiobutton(frame, text="원" , value=2 , variable=shape_var).pack(side="left")
'''                      #이렇게 StringVar로 설정하는 방법도 있다! 앞에는 초기설정도 해놨다
Radiobutton(frame, text="사각형" , value="rect" , variable=var).pack(side="left")
Radiobutton(frame, text="원" , value="cirvle" , variable=var).pack(side="left")

def show_shape():
    canvas.delete('all')

    '''
    if shape_var == 1: #역시 잘못됐을 줄 알았다. .get()을 써서 값을 가져오는 거였구나!
        Rectangle.draw()
        label2.set(f"면적={Rectangle.area()}, 둘레={Rectangle.perimeter()}")
    elif shape_var == 2:
        Circle.draw()
        label2.set(f"면적={Circle.area()}, 둘레={Circle.perimeter()}")
    '''

    if var.get() == "rect":
        s = Rectangle(50, 50, 100, 60) #선택된 도형을 '''생성'''하여->조건 충족! 객체 생성!
    else:
        s = Circle(150, 110, 40) #Q. 왜 인자를 3개밖에 전달 안하지? 클래스 내 함수에서는 4개였는데
    s.draw(canvas) #어느 것이 되든 draw()를 붙여주면 알아서 깔쌈하게 구분해서 그려준다.
    info.set(f"면적={s.area():.2f}, 둘레={s.perimeter():.2f}") #그러고보니 메서드 호출은 객체에 붙여서 하는 거였지.
                                                               #바보같이 클래스명에 메서드를 붙였다.
Button(root, text="그리기" , command = show_shape).pack(pady=10)

root.mainloop()