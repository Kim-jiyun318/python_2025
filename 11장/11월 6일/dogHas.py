class Animal: 
    def speak(self):
        print("동물이 소리를 냅니다.")
      
class Dog:
    def __init__(self):
        self.animal = Animal() #is-a과 달리 클래스의 객체를 생성해 주었다.
                               #그리고 클래스끼리 직접 상속하지 않는다.(괄호 안에 클래스명이 없다.)
    def speak(self):
        #Animal의 기능을 사용하면서 추가 행동을 할 수도 있음
        self.animal.speak()
        print("멍멍!")

dog = Dog()
dog.speak()