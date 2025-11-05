class Course: #문자열 반환을 어떻게 하는 거지????
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, s):
        self.scores.append(s)
    
    def avg(self):
        sum = 0
        for score in self.scores:
            sum += score
        result = sum / len(self.scores)
        return result
    
    def info(self):
        #return "과목: ", str(self.name), "평균: ", str(Course.result) #print 뺀 f string을 하면 된다
        average = self.avg()
        return f"과목: {self.name}, 평균: {average}" #그리고 아래 메인에서 평균함수를 실행 안했으므로 여기서 평균도 계산해야 한다

c = Course("파이썬")
c.add_score(80)
c.add_score(90)
#print(c.info) 함수 형태는 올바르게 적어줘
print(c.info())