from tkinter import *
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title}이(가) 대출되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출 중입니다."
    
    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."

#tkinter 구현
root = Tk()
root.title("도서 대출 관리 프로그램")

l_title = Label(root, text = "제목: ")
l_author = Label(root, text = "저자: ")
e_title = Entry(root, width = 30)
e_author = Entry(root, width = 30)

l_title.grid(row=0, column=0)
e_title.grid(row=0, column=1)
l_author.grid(row=1, column=0)
e_author.grid(row=1, column=1)

#버튼
frame = Frame(root)
frame.pack()

Button(frame, text = "대출")
Button(frame, text = "반납")

root.mainloop()
