import tkinter as tk

class Display:
    def __init__(self, root):
        self.root = root

        self.textWidget = tk.Text(root, width=60, height=10)
        self.textWidget.pack()

        self.button = tk.Button(root, text="제출", command=self.displayText)
        self.button.pack()

    def displayText(self):
        self.text = self.textWidget.get("1.0", tk.END)
        print(self.text)

root = tk.Tk()
app = Display(root)
