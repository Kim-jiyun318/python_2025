#부모 클래스의 메서드도 호출하고 싶을 때(오버라이딩:부모 클래스의 메서드를 필요에 따라 변경)
class Animal:
    def __init__(self, name=""):
        self.name=name
    def eat(self):
        print("동물이 먹고 있습니다.")
    
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def eat(self): 
        super().eat()
        print("강아지가 먹고 있습니다.")

d = Dog() #객체만 생성. 출력 아님
d.eat() #Dog의 eat 메서드 호출: 먼저 부모 클래스의 메서드 호출, 그다음 자기거에서 프린트