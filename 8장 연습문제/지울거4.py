import tkinter as tk

class Radio:
    def __init__(self, root):
        self.root = root

        self.choice = tk.IntVar()

        tk.Radiobutton(root, text="신에이노우젠", padx=50, variable=self.choice, value=1).pack(anchor=tk.W)
        tk.Radiobutton(root, text="블라디레나 밀리제", padx=20, variable=self.choice, value=2).pack(anchor=tk.E)

root = tk.Tk()
go = Radio(root)
root.mainloop()
        
