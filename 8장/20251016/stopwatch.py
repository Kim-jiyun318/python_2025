import tkinter as tk
#작성중

#먼저 객체들을 생성하기
root = tk.Tk()

timer = 0

timeText = tk.Label(root, text="0", font=("Helvetica", 80)) #레이블 생성
timeText.pack()

startButton = tk.Button(root, text='시작', bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(root, text='중지', bg="yellow", command=stop)
stopButton.pack(fill=tk.BOTH)

#그 다음 함수를 정의하자
def startTimer():
    #10ms 후에 호출되어 타이머를 업데이트하는 함수
    if running: #변수다. True = 1, False = 0인거 기억하기
        global timer


startTimer()
root.mainloop()