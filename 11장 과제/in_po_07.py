class Food: #손코딩 해보기
    def __init__(self, name, price):
        self.name  = name
        self.price = price
    
    def total_price(self, qty):
        return self.price * qty
    
    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = delivery_fee
    
    def total_price(self, qty):
        return (self.price * qty) + self.delivery_fee
    
    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원, 배달비: {self.delivery_fee}"

class Order:
    def __init__(self, name, price):
        super().__init__(name, price)
        self.items = () #
    
    #def add(food, qty):
