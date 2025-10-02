from tkinter import*
from random import randint


def randomPlace():
    x = randint(50, 400)
    y = randint(10, 100)
    width = randint(20, 70)
    height = randint(15, 80)
    button.place(x=x, y=y, width=width, height=height)


root = Tk()
root.geometry("300x300")

buttons = []
colors = ["red", "blue", "yellow", "green"]

for color in colors:
    button = Button(root, text=color, bg=color)
    buttons.append(button) #리스트에 추가해주기

randomPlace() #처음에는 그냥 막 지정해

refresh = Button(root, bg="white", command=randomPlace)
refresh.place(x=150, y=250)

root.mainloop()