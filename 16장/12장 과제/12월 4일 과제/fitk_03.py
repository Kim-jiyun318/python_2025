import os
base_dir = os.path.dirname(__file__)

infilename1 = os.path.join(base_dir, input("입력 파일 이름1: "))
infilename2 = os.path.join(base_dir, input("입력 파일 이름2: "))
outfilename = os.path.join(base_dir, input("출력 파일 이름: "))

with open(infilename1, "r", encoding="utf-8") as file1, open(infilename2, "r", encoding="utf-8") as file2, open(outfilename, "w", encoding="utf-8") as outFile:
    inText1 = file1.read()
    outFile.write(inText1)

    outFile.write('\n')
                  
    inText2 = file2.read()
    outFile.write(inText2)

