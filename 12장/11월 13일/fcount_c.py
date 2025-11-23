import os
base_dir = os.path.dirname(__file__)
filename = input("파일명을 입력하세요: ").strip()
filepath = os.path.join(base_dir, filename)

infile = open(filepath, "r", encoding="utf-8")

freqs = {} #딕셔너리 생성

#========이중for문은 늘 헷갈리지=======
for line in infile:
    for char in line.strip(): #양쪽 끝의 공백문자or 줄바꿈기호 제거
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
        
print(freqs)
infile.close()