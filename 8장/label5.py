from tkinter import*

root = Tk()
photo = PhotoImage(file="\Python 2025\Twitter.png")
w = Label(root, image=photo, justify="left").pack(side="right")
message="""T의 공감법은 사이코패스 같은 게 아니다.
문제가 생겼다면 해결할 수 있도록 돕는 것이
진정한 유대 관계라고 생각한다.
물론 나는 T여서 왜?라며 감정을 이해하려고 하지만
감정을 이해하려 하면 안 된다는 것을 안다.
하지만 그건 어렵다. F들이 부럽구나"""

w2 = Label(root,
           padx = 10,
           text=message).pack(side="left")
root.mainloop()
