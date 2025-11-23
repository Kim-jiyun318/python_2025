import os

def parse_file(path):
    infile = open(path) #파일을 전달받아 연다는 걸 힌트로 받으면 캐치

    spaces = 0
    tabs = 0

    for line in infile:
        spaces += line.count(' ')
        tabs += line.count('\t')
    
    infile.close()

    return spaces, tabs #반환값이 있다는 건... 메서드가 있다는 뜻

base_dir = os.path.dirname(__file__) #현재경로

#===========여기부터 공부해야 하는 부분==========
filename = input("파일 이름을 입력하시오: ")

#base_dir(기본 폴더 위치)와 파일명 결합하여 전체 경로 생성
filepath = os.path.join(base_dir, filename) 

spaces, tabs = parse_file(filepath) #함수를 호출했으면 반환값을 받아야 한다.
print(f"스페이스 수 = {spaces}, 탭의 수 = {tabs}")