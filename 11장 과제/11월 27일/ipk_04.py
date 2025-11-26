from tkinter import *
class Person:
    def __init__(self, name): self.name = name
    
class Student(Person):
    def __init__(self, name): 
        super().__init__(name) #상속이니까 속성도 상속...
        self.classes = []

    def enrollCourse(self, subject: str): #반드시 문자열?
        if subject not in self.classes: #조건문을 추가해 줬다.(리스트에 없을 때만!)
            self.classes.append(subject)
    
    def clearCourses(self):
        self.classes.clear()

root = Tk()
root.title("문제 4")
root.geometry("380x280")

stu = Student("홍길동") #Q.사실상 Person은 추상메소드인 걸까? 상속받아서 객체 만들었으니

#Label(root, text="학생: 홍길동").pack() 놉놉. 객체를 넣어야지
Label(root, text=f"학생: {stu.name}", font=("맑은 고딕", 11, "bold")).pack()
         #외부에서 인스턴스 변수에 접근하려니까 객체를 붙여서! 아까 나왔던 거다
#s = Person("홍길동")

frame1 = Frame(root)
frame1.pack(pady=6)

'''
P = IntVar()
Checkbutton(frame1, text="Python", variable=P).pack(side="left")
A = IntVar()
Checkbutton(frame1, text="AI", variable=A).pack(side="left")
D = IntVar()
Checkbutton(frame1, text="DataScience", variable=D).pack(side="left")
'''
#한꺼번에 적어도 ok. 근데 value=0 1 이렇게 해도 되는겨?
P = IntVar(value=0)
A = IntVar(value=0)
D = IntVar(value=0) #모두 해제되어 있는 상태라는데..

cb1 = Checkbutton(frame1, text="Python", variable=P)
cb2 = Checkbutton(frame1, text="AI", variable=A)
cb3 = Checkbutton(frame1, text="DataScience", variable=D)

#체크박스는 grid 쓰는 게 낫나 보다.
cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

#결과 표시 라벨
info = StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
result = Label(root, textvariable=info, wraplength=340, justify="left") #Q.오른쪽 두개는 뭐지?
result.pack()


def enroll():
    #c = Student() 앞에서 객체 생성 했으니 됐다
    stu.clearCourses() #할때마다 초기화작업
    if P.get(): #ok 형식은 동일했어 좋았스!!
        stu.enrollCourse("Python")
    elif A.get():
        stu.enrollCourse("AI")
    elif D.get():
        stu.enrollCourse("DataScience")
    #Q. 어떻게 반영된 것만 레이블로 나타내지? (검색해보기)
    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def clear():
    '''
    P.get() = False #True/False가 아니라 0과 1인가... 검색해보자
    A.get() = False
    D.get() = False
    '''
    P.set(0); A.set(0); D.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

frame2 = Frame(root)
frame2.pack(pady=6)

Button(frame2, text="등록하기" , command=enroll).pack()
Button(frame2, text="초기화" , command=clear).pack()

root.mainloop()