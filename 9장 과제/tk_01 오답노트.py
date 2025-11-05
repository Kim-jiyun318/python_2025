#import tkinter as tk 이거 쓰는 경우의 차이점을 모르겠다
from tkinter import *
#여기서 모르는 거:버튼에서 객체 생성하기(?), 마지막 결과 출력하기

class Book:
    def __init__(self, title, author): # root 안써도 됨
        #self.root = root
        self.title = title
        self.author = author
        self.borrowed = False #self.borrowed 상태인가? 아닌가?
                              #not 연산자도 사용 가능
    def borrow(self):
        if self.borrowed == False:
            self.borrowed = True
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출 중입니다."
    
    def return_book(self):
        if self.borrowed == False:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."
        self.borrowed = False
        return f"{self.title}이(가) 반납되었습니다."
    
root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("380x220")

Label(root , text = "도서 대출 관리 시스템", font=(30)).pack()

#입력칸은 grid로 생각하기
'''
#대출 입력칸
title_frame = Frame(root)
title_frame.pack()

Label(title_frame, text="제목: ").pack()
title_entry = Entry(title_frame, width=30)
title_entry.pack()  

#작가 입력칸
author_frame = Frame(root)
author_frame.pack()

Label(author_frame, text="저자: ").pack()
author_entry = Entry(author_frame, width=30)
author_entry.pack()
'''

#대출, 반납 버튼
book_frame = Frame(root)
book_frame.pack()

borrow_button = Button(book_frame, text = "대출", width = 30, command = Book.borrow())
borrow_button.pack()

return_button = Button(book_frame, text = "반납", width = 30, command = Book.return_book())
return_button.pack()

#결과 출력
Label(root, )

root.mainloop()