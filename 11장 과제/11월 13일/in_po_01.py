class Car:
    def __init__(self, speed):
        self.speed = speed
    
    def get_speed(self):
        return f"현재 속도: {self.speed}km/h"

class SportsCar(Car): #상속시 빼먹으면 안됨
    #super().__init__() super()생성자는 자식 클래스의 생성자 내에서

    def __init__(self, speed, turbo): #문제를 보면 turbo는 입력받는다.
        super().__init__(speed)
        self.turbo = turbo
    
    def get_speed(self):
        #super().get_speed()
        if self.turbo: # self.turbo == True 와 같다
            return "현재 속도: 200lm/h (터보 ON)"
        else:
            return "현재 속도: 100km/h (터보 OFF)"

car1 = Car(80)
print(car1.get_speed())

sport1 = SportsCar(150, True)
print(sport1.get_speed())

sport2 = SportsCar(120, False)
class Car:
    def __init__(self, speed):
        self.speed = speed
    
    def get_speed(self):
        return f"현재 속도: {self.speed}km/h"

class SportsCar(Car): #상속시 빼먹으면 안됨
    #super().__init__() super()생성자는 자식 클래스의 생성자 내에서

    def __init__(self, speed, turbo): #문제를 보면 turbo는 입력받는다.
        super().__init__(speed)
        self.turbo = turbo
    
    def get_speed(self):
        #super().get_speed()
        if self.turbo: # self.turbo == True 와 같다
            return "현재 속도: 200lm/h (터보 ON)"
        else:
            return "현재 속도: 100km/h (터보 OFF)"

car1 = Car(80)
print(car1.get_speed())

sport1 = SportsCar(150, True)
print(sport1.get_speed())

sport2 = SportsCar(120, False)
print(sport2.get_speed())