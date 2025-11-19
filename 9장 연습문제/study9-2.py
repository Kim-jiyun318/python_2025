class Dog:
    def __init__(self, name, age, tricks): #인스턴스 변수를 괄호에 전부 추가하기
        self.name = name
        self.age = age
        #self.tricks = [] 이렇게 하면 tricks에 어떤 값을 넣든 항상 초기화된다고 한다.
        self.tricks = tricks
    
    def bark(self):
        print(f"{self.name}가 짖고 있습니다!")

    def info(self):                  
        print(f"이름: {self.name}, 나이: {self.age}살")
    
    def show_tricks(self):
        tricks_str=', '.join(self.tricks) #리스트형식으로 안 보이게 하려고 join 사용
        print(f"{self.name}의 장기는 {tricks_str}입니다.")


'''    
def bark(name):
    print(f"{name}가 짖고 있습니다!")
                                    들여쓰기를 잘못했따. 이러면 그냥 외부 함수일 뿐이다. 
def info(name, age):                또한 클래스의 메서드는 항상 첫 번째 인자를 self로 받아야 한다.
    print(f"이름: {name}, 나이: {age}살") 첫 번째 인자를 self로 받았다면 name이나 age에 접근가능
                                        ->따로 인자를 써줄 필요 없으며, 객체에만 명시한다.
'''

#----------구현-----------
baduk = Dog("바둑이", 3, ["뒹굴기", "달리기"]) #문제 2번에서, 여기를 수정해 주어야 하는 거였다.
mung = Dog("멍멍이", 5, ["먹기"])  #근데 리스트로 굳이 하지는 않아도 되는 건가
'''
bark(baduk)
bark(mung)

info(baduk)    객체 지향적으로 수정해 보자. 
info(mung)      클래스의 메서드로 정의하는 것이다. 객체.메소드()
'''                 

baduk.bark()
mung.bark()

baduk.info()
mung.info()

baduk.show_tricks()
class Dog:
    def __init__(self, name, age, tricks): #인스턴스 변수를 괄호에 전부 추가하기
        self.name = name
        self.age = age
        #self.tricks = [] 이렇게 하면 tricks에 어떤 값을 넣든 항상 초기화된다고 한다.
        self.tricks = tricks
    
    def bark(self):
        print(f"{self.name}가 짖고 있습니다!")

    def info(self):                  
        print(f"이름: {self.name}, 나이: {self.age}살")
    
    def show_tricks(self):
        tricks_str=', '.join(self.tricks) #리스트형식으로 안 보이게 하려고 join 사용
        print(f"{self.name}의 장기는 {tricks_str}입니다.")


'''    
def bark(name):
    print(f"{name}가 짖고 있습니다!")
                                    들여쓰기를 잘못했따. 이러면 그냥 외부 함수일 뿐이다. 
def info(name, age):                또한 클래스의 메서드는 항상 첫 번째 인자를 self로 받아야 한다.
    print(f"이름: {name}, 나이: {age}살") 첫 번째 인자를 self로 받았다면 name이나 age에 접근가능
                                        ->따로 인자를 써줄 필요 없으며, 객체에만 명시한다.
'''

#----------구현-----------
baduk = Dog("바둑이", 3, ["뒹굴기", "달리기"]) #문제 2번에서, 여기를 수정해 주어야 하는 거였다.
mung = Dog("멍멍이", 5, ["먹기"])  #근데 리스트로 굳이 하지는 않아도 되는 건가
'''
bark(baduk)
bark(mung)

info(baduk)    객체 지향적으로 수정해 보자. 
info(mung)      클래스의 메서드로 정의하는 것이다. 객체.메소드()
'''                 

baduk.bark()
mung.bark()

baduk.info()
mung.info()

baduk.show_tricks()
mung.show_tricks()