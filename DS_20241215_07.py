from tkinter import*

def draw_rectangle():
    canvas.delete("all")
    canvas.create_rectangle(200, 200, 100, 100, fill="red")

def draw_oval():
    canvas.delete("all")
    canvas.create_oval(200, 200, 100, 100, fill="blue")

def draw_image():
    global img
    canvas.delete("all")
    img = PhotoImage(file="logo.png")
    canvas.create_image(20, 20, anchor=NW, image=img)

def delete():
    canvas.delete("all")

root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

frame = Frame(root)
frame.pack()

Button(frame, text= "사각형", command=draw_rectangle, padx=10).pack(side="left")
Button(frame, text= "원", command=draw_oval, padx=10).pack(side="left")
Button(frame, text= "그림", command=draw_image, padx=10).pack(side="left")
Button(frame, text= "지우기", command=delete, padx=10).pack(side="left")

Label(root, text="버튼을 눌러 도형을 선택하세요.", pady=10).pack()

root.mainloop()