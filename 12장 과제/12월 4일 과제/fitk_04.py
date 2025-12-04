#헐 내가 해냄!! 와!!
from tkinter import*

class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):    
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
    
class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

#파일 처리 함수
def append_log(message):
    #with open("drive_log.txt", "w", encoding="utf-8") as file:
    with open("drive_log.txt", "a", encoding="utf-8") as file: #w는 무조건 새 파일을 열고 쓴다.
        file.write(message + '\n')

def clear_log_file():
    with open("drive_log.txt", "w"): #파일을 w모드로 열고 닫으면 파일 내용 모두 삭제됨
        pass

#tkinter
root = Tk()
root.title("문제4")
root.geometry("400x320")

Label(root , text = "차량 이름을 입력하세요.").pack(pady=6)
entry = Entry(root, width=30)  
entry.pack()

result_label = Label(root , text = "결과가 여기에 표시됩니다.")
result_label.pack(pady=20)

#호출 함수 설정
def drive_car():
    text = entry.get()
    check = text.replace(" ", "")
    if check == None:
        text = '이름없음'
    
    #message = Car(text)
    #message = car.get()

    car = Car(text)
    message = car.drive()

    append_log(message)

    result_label.config(text = message)

def drive_truck():
    #message = Truck() #이게 맞는 건가...? 틀렸다.
    #반환값을 얻으려면 일단 '객체의 메서드'를 작동시켜야 한다!
    text = entry.get()
    check = text.replace(" ", "")
    if check == None:
        text = '이름없음'

    truck = Truck(text)
    message = truck.drive()

    #message = truck.get()
    append_log(message)

    result_label.config(text = message)

def clear_log():
    clear_log_file()

    result_label.config(text = "로그 파일을 비웠습니다.")

frame = Frame(root)
frame.pack()

Button(frame, text="자동차 주행" , command=drive_car).pack(pady=6) #꼭 고정해줘
Button(frame, text="트럭 주행" , command=drive_truck).pack(pady=6)
Button(frame, text="로그 비우기" , command=clear_log).pack(pady=6)

root.mainloop()