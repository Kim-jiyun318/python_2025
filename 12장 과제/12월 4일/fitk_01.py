import os
base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, input("텍스트 파일 이름을 입력하세요: "))

#infile = open("example01.txt", "r", encoding="utf-8")
infile = open(infilename, "r", encoding="utf-8")
s = infile.read() 
print(s)
infile.close()