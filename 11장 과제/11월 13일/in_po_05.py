class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self): #우리가 만든 객체를 출력할 때, 객체가 어떤 문자열로 표현될지를 정의한다. 정의하지 않으면 그냥 주소값을 내뱉는다.
        return f"메뉴: {self.name}, 가격: {self.price}"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)

        self.delivery_fee = delivery_fee
    
    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price + self.delivery_fee}(배달비 포함)"
    
class Order:
    def __init__(self):
        self.food_list = []

    def add_food(self, food):
        #self.food_list += food
        self.food_list.append(food) #여기까지는 조금 틀려도 전체적인 틀은 맞았음
    
    def show_order(self): #여기가 어려웠따
        print("====== 주문 내역 ======")
        for f in self.food_list:
            print(f) #아까 음식 객체를 리스트에 추가했는데, 그 객체를 그대로 출력한다.
                     #왜 str메서드를 썼는지 알 수 있다. 객체를 출력하기 때문...

f1 = Food("김밥", 3000)
f2 = DeliveryFood("짜장면", 6000, 2000)

order = Order()
order.add_food(f1)
order.add_food(f2)
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self): #우리가 만든 객체를 출력할 때, 객체가 어떤 문자열로 표현될지를 정의한다. 정의하지 않으면 그냥 주소값을 내뱉는다.
        return f"메뉴: {self.name}, 가격: {self.price}"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)

        self.delivery_fee = delivery_fee
    
    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price + self.delivery_fee}(배달비 포함)"
    
class Order:
    def __init__(self):
        self.food_list = []

    def add_food(self, food):
        #self.food_list += food
        self.food_list.append(food) #여기까지는 조금 틀려도 전체적인 틀은 맞았음
    
    def show_order(self): #여기가 어려웠따
        print("====== 주문 내역 ======")
        for f in self.food_list:
            print(f) #아까 음식 객체를 리스트에 추가했는데, 그 객체를 그대로 출력한다.
                     #왜 str메서드를 썼는지 알 수 있다. 객체를 출력하기 때문...

f1 = Food("김밥", 3000)
f2 = DeliveryFood("짜장면", 6000, 2000)

order = Order()
order.add_food(f1)
order.add_food(f2)
order.show_order()