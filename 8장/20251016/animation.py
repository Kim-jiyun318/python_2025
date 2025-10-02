from tkinter import*

def move_oval(): 
    canvas.move(id, 3, 0) # x축:3 y축:0
    if canvas.coords(id)[2] < 400: 
        root.after(50, move_oval) # 50ms 후에 move_oval 함수 호출


root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill="green")
move_oval() ##함수 호출

root.mainloop()