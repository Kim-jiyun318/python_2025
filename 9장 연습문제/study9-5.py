class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount+=1 #생성될 때마다 클래스값이 바뀌어야 한다.
        #클래스 변수는 앞에 클래스를 붙여줘야 한다.
    def displayEmp(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
        #empCount += 1

Kim = Employee("Kim", 5000)
Lee = Employee("Lee", 6000)

#함수출력하는거 깜빡했다
Kim.displayEmp()
Lee.displayEmp()

#print(f"Total employees: {empCount}")
class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount+=1 #생성될 때마다 클래스값이 바뀌어야 한다.
        #클래스 변수는 앞에 클래스를 붙여줘야 한다.
    def displayEmp(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
        #empCount += 1

Kim = Employee("Kim", 5000)
Lee = Employee("Lee", 6000)

#함수출력하는거 깜빡했다
Kim.displayEmp()
Lee.displayEmp()

#print(f"Total employees: {empCount}")
print("Total emplyees:", Employee.empCount)