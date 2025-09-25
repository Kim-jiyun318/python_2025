from tkinter import*

root = Tk()
photo = PhotoImage(file="cat.jpeg")
label = Label(root, image=photo)
label.pack()
root.mainloop()