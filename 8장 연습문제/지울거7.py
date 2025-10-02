import tkinter as tk

class frames:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(root, width=600, height=100)
        self.frame.pack()
                               #이렇게 frame을 넣으면 한 프레임 안에 두 개의 버튼을 넣는것을 의미한다.
        self.button1 = tk.Button(self.frame, text="파란휴지")
        self.button1.pack(side="right")

        self.button2 = tk.Button(self.frame, text="빨간휴지")
        self.button2.pack(side="right")


root = tk.Tk()
root.geometry("300x300")
app = frames(root)
root.mainloop()
