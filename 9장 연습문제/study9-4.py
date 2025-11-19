class Employee:
    def __init__(self, name, salary):
        self.name = name #직원의 이름과 연봉을 저장하고!
        self.salary = salary
    
    def usual_salary(self):
        print(f"{self.name}의 연봉은 {self.salary}입니다.")

    def raise_salary(self):
        self.salary += 2000
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")
    
employee1 = Employee("Kim", 5000)
employee2 = Employee("Lee", 6000)

employee1.usual_salary()
employee2.usual_salary() #무조건 안에다가 만들 필요는 없구나
                        #조건에 없었으니까 다음에는 usual_salary를 여기에 출력하자.
employee1.raise_salary()
employee2.raise_salary()
class Employee:
    def __init__(self, name, salary):
        self.name = name #직원의 이름과 연봉을 저장하고!
        self.salary = salary
    
    def usual_salary(self):
        print(f"{self.name}의 연봉은 {self.salary}입니다.")

    def raise_salary(self):
        self.salary += 2000
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")
    
employee1 = Employee("Kim", 5000)
employee2 = Employee("Lee", 6000)

employee1.usual_salary()
employee2.usual_salary() #무조건 안에다가 만들 필요는 없구나
                        #조건에 없었으니까 다음에는 usual_salary를 여기에 출력하자.
employee1.raise_salary()
employee2.raise_salary()
