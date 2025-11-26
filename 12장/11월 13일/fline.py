import os #상대경로는 오류가 많으니 이렇게 절대경로를 쓰는 연습을 하자
base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, "proverbs.txt")
outfilename = os.path.join(base_dir, "output.txt")

#텍스트 파일을 읽기 모드로 열고 변수에 할당
infile = open(infilename)

#텍스트 파일을 쓰기 모드로 열고 변수에 할당
outfile = open(outfilename, "w")

#라인 번호 저장할 변수
i = 1

#텍스트 파일의 각 라인에 대해 반복
for line in infile:
    outfile.write(str(i) + ": " + line) #숫자는 str()로 변환 필수

    i += 1 #다음 라인으로 이동하기 위해 숫자 증가

#파일닫기
infile.close()
outfile.close()