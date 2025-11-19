import math #원의 넓이를 계산하기 위해 pi를 불러오는 라이브러리

class Shape:
    def calculate_area(self):
        pass

class ShowOval(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        #self.cirResult = self.radius*self.radius
        return math.pi*self.radius**2 #바로 반환만 하면 되는 걸 까먹었군
    
class ShowRec(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        #self.recResult = self.width*self.height
        return self.width * self.height
#메인
def sumAll(shapes): #shapes는 전달받은 리스트
    total = 0
    for s in shapes:
        total += s.calculate_area() #계산결과를 처음부터 갖고오는 게 아니라 
    return total                    #calculate_area()메서드 호출을 통해 각각의 면적을 구하여 더하는 방식이었다. 그래서 메서드를 호출하라고 한 거구나
                                    #나는 아직 객체 생성과 메서드 호출을 헷갈리나?
c = ShowOval(5)
r = ShowRec(4, 6)

print(f"Circle의 면적: {c.calculate_area():.2f}")
print(f"Rectangle의 면적: {r.calculate_area():.2f}")
print(f"도형들의 총 넓이: {sumAll([c, r]):.2f}") #리스트 형식으로 입력받는다...그냥 리스트 형식으로 넣어버리면 그만?