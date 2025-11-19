#텍스트 파일을 읽기 모드로 열고 변수에 할당
infile = open("proverbs.txt")

#텍스트 파일을 쓰기 모드로 열고 변수에 할당
outfile = open("output.txt", "w")

#라인 번호 저장할 변수
i = 1

#텍스트 파일의 각 라인에 대해 반복
for line in infile:
    outfile.write(str(i) + ": " + line)

    i += 1

#파일닫기
infile.close()
outfile.close()