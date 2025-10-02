class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age #private 아님
    
x = Friend("홍길동", 20)
x.setAge(-5)
print(x.age)