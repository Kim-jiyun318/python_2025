class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def getSalary(self):
        self.salary = super().getSalary()
        return self.salary + self.bonus
    
    def __repr__(self):                                         #이 슬래시는 무슨 역할?
        return "이름:" + self.name + "; 월급:" + str(self.salary) + \
            "; 보너스:" +str(self.bonus)

kim = Manager("김철수", 2000000, 1000000)
print(kim)