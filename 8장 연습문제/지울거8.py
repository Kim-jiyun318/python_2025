from tkinter import*

root = Tk()
root.geometry("300x300")

button1 = Button(root, bg="skyblue")
button2 = Button(root, bg="red")
button3 = Button(root, bg="yellow")
button1.pack(pady=10) #상하여백
button2.pack(padx=10) #좌우여백
button3.grid(pady=20)

root.mainloop(  )