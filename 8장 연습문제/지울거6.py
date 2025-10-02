import tkinter as tk

class Lists:
    def __init__(self, root):
        self.root = root

        self.lb = tk.Listbox(root, height=4)
        self.lb.pack() #지금은 또 변수에 할당해서 두 줄짜리로 pack()

        self.lb.insert(tk.END, "나는")#반드시 위치 인덱스가 들어가야 한다
        self.lb.insert(tk.END, "네 곁에") #0 또는 tk.END
        self.lb.insert(tk.END, "있을지도")
        self.lb.insert(tk.END, "몰라")

root  = tk.Tk()
app = Lists(root)
root.mainloop()

