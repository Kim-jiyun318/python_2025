class User:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if isinstance(other, User): #User 객체일 때만 비교
            return self.name == other.name #이름이 같은지 검사. name만 비교한다.
        return False                       #객체 자체를 비교하는 게 아니다.

user1 = User("Kim")
user2 = User("Lee")
user3 = User("Park")
user5 = User("Kim") #user1과 이름은 같지만 다른 객체

users = [user1, user2]

print(user1 in users)
print(user2 in users)
print(user3 in users)
print(user5 in users)