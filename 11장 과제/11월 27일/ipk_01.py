#https://github.com/beagglechung/2025_Python/blob/main/inheri%2Bpoly%2Btkinter/ipk_04.py
from tkinter import *

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f"승용차{self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

#객체 생성
car = Car("car1")
truck = Truck("truck1")

#tkinter 구성
root = Tk()
root.title("문제1")
root.geometry("400x300")

Label(root, text = "버튼을 눌러보세요.")

frame = Frame(root)
frame.pack(pady = 10)

#버튼 기능 함수에 정의하기
def show_car():
    result.set(car.drive())

def show_truck():
    result.set(truck.drive())


''' 그냥 함수를 콜백하고 그 함수에 기능을 정의하면 된다
c_button = Button(frame, text = "자동차 주행", command = car1.drive())
c_button.pack()
t_button = Button(frame, text = "트럭 주행", command = truck1.drive())
t_button.pack()
'''
Button(frame, text="자동차 주행", command=show_car).pack(side="left", padx=10)
Button(frame, text="트럭 주행", command=show_truck).pack(side="left", padx=10)


#result = Label(root, text = " ")
result = StringVar(value=" ") #python은 텍스트변경을 실시간으로 감지할 수 없기 때문에 임시 공간에 저장해준다.
label2 = Label(root, textvariable=result, font=("맑은 고딕", 11))
label2.pack()
#result.config(root, text = " ") config

root.mainloop()