#중요함!! 

from tkinter import *

class Pet:
    def speak(self):
        return f"..."
    
class Dog(Pet):
    def speak(self):
        return f"멍멍!"

class Cat(Pet):
    def speak(self):
        return f"야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet #문제를 잘못 읽었는데 그냥 has-a관계를 설명하는 거였다.
                       #복잡하게 생각하지 말기!!

#TKinter
root = Tk()
root.title("문제2")
root.geometry("400x200")

Label(root , text = "반려동물을 선택하고 '말하기'를 누르세요.", font=("맑은 고딕", 11)).pack(pady=10)

#https://blog.naver.com/youndok/222583032300 클래스의 합성에 대해 참조할 글
#사람 객체(빼먹음)
person = Person("홍길동") #근데 Person 말고는 인스턴스 변수도 없긴 했다.

#버튼
#문제에서 제일 이해가 안 됐던 게 이해됐다. 왜 소문자를 제시하고 할당하라 했는가 하면...객체를 생성하라는? 의미였던 것...아닐까?
def pick_dog():
    '''
    person = Dog("홍길동") #person.pet = Dog()인 걸 눈치챘어도 적용하지 못한 건 객체가 존재X였기에
    person.pet             그에 대한 객체를 만들어 주었어야 했다.
    '''
    #person.pet = Dog("홍길동") #person.pet은 객체가 가진 속성이라 이해하면 된다.
    person.pet = Dog() #아까 인자 전달해 줬는데 왜 또 인자를 넣고 있어
    #label2.config(text = "강아지를 선택했습니다.", fg="blue", font=("맑은 고딕", 11)) 밑에다가 잘 해놓고...
    result.set("강아지를 선택했습니다. ") #우선 이건 선택버튼이고 강아지 선택했다는 걸 보여줘야함

def pick_cat():
    '''
    person = Cat("홍길동")
    person.pet
    '''
    person.pet = Cat() #여기에도 또 이름 넣었었네
    #label2.config(text = "고양이를 선택했습니다.", fg="blue", font=("맑은 고딕", 11))
    result.set("고양이를 선택했습니다. ")

def show_result(): #여기 보니까 person 있다. self는 클래스 내에서만 써야 한다고. 클래스 외부에서 특정 객체의 속성에 접근하려면, 객체가 앞에 와야 한다.
    result.set(f"{person.name}의 반려동물 -> {person.pet.speak()}") #이제야 라벨을 문제에서 주어진대로 person.pet.speak()의 결과값으로 바꿔줄 수 있다.
              
frame = Frame(root)
frame.pack()

Button(frame, text = "강아지 선택", command = pick_dog).pack(side = "left", padx = 10)
Button(frame, text = "고양이 선택", command = pick_cat).pack(side = "left", padx = 10)

Button(root, text = "말하기", command = show_result).pack(pady=20)

result = StringVar(value=" ")
label2 = Label(root, textvariable = result, font=("맑은 고딕", 11), fg="blue")
label2.pack(pady=10)

root.mainloop()