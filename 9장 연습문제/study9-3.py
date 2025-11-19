class Student:
    def __init__(self, name):
        self.name = name #이런 건 외부에서 전달받아 저장하는 거!
        self.score = [] #학생의 이름과 성적을 저장한다 했으니 객체 두 개 생성!


    def add_score(self, test):
        self.score.append(test)
        print(f"{self.name}의 성적 {test}점이 추가되었습니다.")

    def cal_avg(self):
        sum = 0
        count = 0
        for i in self.score:
            sum += i
            count += 1
        avg = sum/count
        print(f"{self.name}의 평균 성적: {avg:.2f}")

student = Student("Kim")

student.add_score(90)
student.add_score(85)
student.add_score(78)
student.cal_avg()
class Student:
    def __init__(self, name):
        self.name = name #이런 건 외부에서 전달받아 저장하는 거!
        self.score = [] #학생의 이름과 성적을 저장한다 했으니 객체 두 개 생성!


    def add_score(self, test):
        self.score.append(test)
        print(f"{self.name}의 성적 {test}점이 추가되었습니다.")

    def cal_avg(self):
        sum = 0
        count = 0
        for i in self.score:
            sum += i
            count += 1
        avg = sum/count
        print(f"{self.name}의 평균 성적: {avg:.2f}")

student = Student("Kim")

student.add_score(90)
student.add_score(85)
student.add_score(78)
student.cal_avg()
#답안이랑 살짝 달라지긴 했는데 그래도 에러가 없다!