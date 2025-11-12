from tkinter import *
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"멍멍!"

class Cat(Animal):
    def speak(self):
        return f"야옹!"

class Duck(Animal):
    def speak(self):
        return f"꽥꽥!"

def make_sound(animal: Animal): #Q. 이게 무슨 뜻이지
    sound = animal.speak() #메서드 호출
    result.config(text=sound)
'''
def make_sound(animal):
    if animal == "dog":
        dog = Dog()
        result.config(root, text=dog)
    elif animal == "cat":
        cat = Cat()
        result.config(root, text=cat)
    elif animal == "duck":
        duck = Duck()
        result.config(root, text=duck)
'''
        
#======= GUI 구현 =======
root = Tk()
root.geometry("400x200")
root.title("동물 소리 듣기")

Label(root, text="동물 버튼을 눌러 소리를 들어보세요.", pady=10).pack()

#frame = Frame(root).pack() 이렇게 하면 안돼지
frame = Frame(root)
frame.pack()

Button(frame, text="강아지", command=lambda : make_sound(Dog()), padx=10).pack(side='left') #클래스 객체 생성하여 람다함수로 인자 전달
Button(frame, text="고양이", command=lambda : make_sound(Cat()), padx=10).pack(side='left')
Button(frame, text="오리", command=lambda : make_sound(Duck()), padx=10).pack(side='left')
'''
Button(frame, text="강아지", command=lambda ch="dog": make_sound(ch), padx=10).pack(side='left')
Button(frame, text="고양이", command=lambda ch="cat": make_sound(ch), padx=10).pack(side='left')
Button(frame, text="오리", command=lambda ch="duck": make_sound(ch), padx=10).pack(side='left')
'''

#result = Label(root, text="(여기에 울음소리가 나옵니다)", pady = 30, font=('맑은 고딕', 15, "bold")).pack()
#객체를 생성하면 그 다음 줄에 .pack()를 통해 배치해야지 위젯의 생성과 배치를 한꺼번에 해결하려 하면 안 된다.
result = Label(root, text="(여기에 울음소리가 나옵니다)", pady = 30, font=('맑은 고딕', 15, "bold"))
result.pack()

root.mainloop() 