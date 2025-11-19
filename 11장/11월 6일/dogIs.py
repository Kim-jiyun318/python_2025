class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal): #직접 상속:둘이 같은 클래스
    def speak(self):
        print("멍멍!")

dog = Dog()
dog.speak()