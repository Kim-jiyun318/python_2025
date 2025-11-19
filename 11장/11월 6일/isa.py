#1. Dog is an Animal
class Animal:
    def move(self):
        print("동물이 움직입니다.")

class Dog(Animal):
    def move(self):
        super().move()
        print("개가 달립니다.")

dog  = Dog()
dog.move()

print("==============")
#2. Student is a Person
class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student(Person):
    def study(self):
        print("학생이 공부합니다.")

stu = Student()
stu.speak()
stu.study()

print("==============")
#3. Car is a Vehicle
class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다.")

class Car(Vehicle):
    def drive(self):
        super().drive()
        print("자동차가 도로를 달립니다.")

car  = Car()
car.drive()