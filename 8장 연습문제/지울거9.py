from tkinter import*

root = Tk()
root.geometry("300x300")

button1 = Button(root, bg="skyblue")
button2 = Button(root, bg="red")
button3 = Button(root, bg="yellow")
button1.grid(row=1, column=3) #상하여백
button2.grid(row=0, column=1) #좌우여백
button3.grid(row=1, column=2)

root.mainloop(  )