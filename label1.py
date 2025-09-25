from tkinter import* # * 기호를 꼭 붙여줘야 한다.

root = Tk() #윈도우 생성
root.geometry("300x200") #창의 크기 설정

label = Label(root, text="Hello, World!") #레이블 위젯 생성
label.pack() #레이블 배치

root.mainloop() #이벤트 루프 시작