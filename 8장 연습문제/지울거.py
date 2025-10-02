import tkinter as tk

class Student:
    def __init__(self, root):
        self.root = root

        self.label1 = tk.Label(root, text="이름").pack()
        self.entryValue1 = tk.Entry(root)
        self.entryValue1.pack()

        self.label2 = tk.Label(root, text="나이").pack()
        self.entryValue2 = tk.Entry()
        self.entryValue2.pack()

        self.button = tk.Button(root, text="제출", command=self.getValue)
        self.button.pack()
    
    def getValue(self):
        self.getValue1 = self.entryValue1.get()
        self.getValue2 = self.entryValue2.get()
        print(f"이름: {self.getValue1}")
        print(f"나이: {self.getValue2}")

root = tk.Tk()
root.geometry("500x300")
result = Student(root)
root.mainloop()