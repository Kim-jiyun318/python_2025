import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self, root): #tkinter때 객체로 생성하는것은 대부분은 인스턴스 변수이다.
        self.root = root   

        #캔버스 생성
        self.canvas = tk.Canvas(root, width = 500, height = 500)
        self.canvas.pack()

        #공 생성
        self.shape

    
