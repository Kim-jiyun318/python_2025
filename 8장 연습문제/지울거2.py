import tkinter as tk
from tkinter.messagebox import showinfo

class Check:
    def __init__(self, root):
        self.root = root

        #초기상태는 '비동의'로 설정(set)하고 새롭게 저장받는다.
        agree = tk.StringVar()
        agree.set("비동의")

        tk.Checkbutton(root, text = "동의합니다",
                       variable=agree,
                       onvalue = "동의",
                       offvlaue = "비동의",
                       command=self.popup).pack()#pack은 필수
    
    def popup(self):
        showinfo(title="결과", message = self.agree.get())#출력하려면 값을 '가져'와야지

root = tk.Tk()
window = Check(root)
root.mainloop()
