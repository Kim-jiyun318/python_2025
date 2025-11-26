import os
base_dir = os.path.dirname(__file__)

#입력 파일 이름과 출력 파일 이름을 받는다.
infilename = os.path.join(base_dir, input("입력 파일 이름: "))
outfilename = os.path.join(base_dir, input("출력 파일 이름: "))

#합계와 횟수를 위한 변수를 정의한다.
sum = 0
count = 0

#입력과 출력을 위한 파일을 열고 작업을 수행한다.
# 읽기, 쓰기 둘다 할 것이므로 각각 써준다.
with open(infilename, "r", encoding="utf-8") as infile, open(outfilename, "w", encoding="utf-8") as outfile:
    #입력 파일에서 한 줄을 읽어서 합계를 계산한다.
    for line in infile:
        dailySale = int(line)
        sum += dailySale
        count += 1
    
    #총매출과 일평균 매출을 출력 파일에 기록한다.
    #with 블럭이 종료되면 자동으로 파일을 닫으므로 작성(w)까지도(!) with 블럭 내에서 해야 한다.
    outfile.write("총매출 = " + str(sum) + "\n")
    outfile.write("평균 일매출 = " + str(sum // count))