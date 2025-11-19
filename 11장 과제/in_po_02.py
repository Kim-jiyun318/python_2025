class Vehicle:
    def drive(self): #아무것도 정의 안해도 self는 필요하구나
        #Q. return 추상 메서드 역할이라고 한다. 무슨 뜻이지?
        pass  #이것도 오버라이딩이라고 할 수 있을까?

class Truck(Vehicle):
    def drive(self):
        return f"트럭이 화물을 운송합니다."

class Car(Vehicle):
    def drive(self):
        return f"승용차가 사람을 태우고 있습니다."

vehivles = [Truck(), Car(), Truck()]

for v in vehivles:
class Vehicle:
    def drive(self): #아무것도 정의 안해도 self는 필요하구나
        #Q. return 추상 메서드 역할이라고 한다. 무슨 뜻이지?
        pass  #이것도 오버라이딩이라고 할 수 있을까?

class Truck(Vehicle):
    def drive(self):
        return f"트럭이 화물을 운송합니다."

class Car(Vehicle):
    def drive(self):
        return f"승용차가 사람을 태우고 있습니다."

vehivles = [Truck(), Car(), Truck()]

for v in vehivles:
    print(v.drive())