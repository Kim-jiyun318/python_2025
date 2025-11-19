class Bank:
    #balance = 1000
    insert_rate= 0.3 #예금이자
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance #각자의 계좌니까 인스턴스변수

    def deposit(self, money):
        self.balance += money
        print(f"저축 후 잔고: {self.balance}")
    
    def withdraw(self, money):
        if self.balance < money:
            print("잔액 부족")
            return None
        self.balance -= money
        print("인출 성공")
        print(f"인출 후 잔고: {self.balance}")

bank = Bank("Kim", "0000", 1000) #클래스 변수를 지정하라는 걸 잘못 이해했다.

print(f"초기 잔고: {bank.balance}")

bank.deposit(500)
bank.withdraw(200)
class Bank:
    #balance = 1000
    insert_rate= 0.3 #예금이자
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance #각자의 계좌니까 인스턴스변수

    def deposit(self, money):
        self.balance += money
        print(f"저축 후 잔고: {self.balance}")
    
    def withdraw(self, money):
        if self.balance < money:
            print("잔액 부족")
            return None
        self.balance -= money
        print("인출 성공")
        print(f"인출 후 잔고: {self.balance}")

bank = Bank("Kim", "0000", 1000) #클래스 변수를 지정하라는 걸 잘못 이해했다.

print(f"초기 잔고: {bank.balance}")

bank.deposit(500)
bank.withdraw(200)
bank.withdraw(1400)