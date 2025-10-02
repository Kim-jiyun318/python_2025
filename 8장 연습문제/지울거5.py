import tkinter as tk
from tkinter.messagebox import showinfo

class Check:
    def __init__(self, root):
        self.root = root

        self.agree = tk.StringVar() #값을받아서 저장
        self.agree.set("비동의") #첫설정은 비동의

        tk.Checkbutton(root, text="동의합니다.",
                       variable = self.agree,
                       onvalue="동의",
                       offvalue="비동의",
                       command = self.agreePop).pack()#변수에 할당하는 방식이 아닐 땐 바로 .pack()해도 문제없음
        #tk.Checkbutton.pack()
    def agreePop(self):
        showinfo(title="결과", message=self.agree.get())#showinfo는 import가 필요하다

root = tk.Tk()
root.geometry("700x400")
app = Check(root)
root.mainloop()
