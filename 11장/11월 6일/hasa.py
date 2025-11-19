#1. Dog has an Animal
class Animal:
    def move(self):
        print("동물이 움직입니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()
    
    def move(self):
        self.animal.move()
        print("개가 달립니다.")

dog = Dog()
dog.move()

print("==============")
#2. Student has a Person
class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student:
    def __init__(self):
        self.person = Person()
    
    def study(self):
        self.person.speak()
        print("학생이 공부합니다.")

stu = Student()
stu.study()
