import os
base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, input("텍스트 파일 이름을 입력하세요: "))
findWord = input("검색 문자열을 입력하세요: ")

word = []
count = 0
with open(infilename, "r", encoding="utf-8") as file: #close를 쓰지 않아도 자동으로 파일을 닫을 수 있고, 
    for line in file:
        if findWord in line:
            count += 1

print(f"'{findWord}'(은)는 파일 내에서 {count}번 나타납니다.")
    