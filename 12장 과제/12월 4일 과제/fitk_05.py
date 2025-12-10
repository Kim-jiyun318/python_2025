from tkinter import filedialog
from tkinter import *
import os
base_dir = os.path.dirname(__file__)


def count_stats(filename):
    space_count = 0
    up_count = 0
    low_count = 0
    with open(filename, "r", encoding="utf-8") as file:
        
        for line in file:
            for ch in line:
                if ch == ' ':
                    space_count+=1
                elif ch.isupper():
                    up_count+=1
                elif ch.islower():
                    low_count+=1
        return space_count, up_count, low_count


def select_file():
    path = filedialog.askopenfilename(title = "파일을 선택해 주세요.", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
    if not path: #경로가 없으면
        return #바로 종료
    try:
        counts = count_stats(path)
        select_label.config(text = f"선택된 파일:{path}")
        result_label.config(text = f"스페이스:{counts[0]}, 대문자:{counts[1]}, 소문자:{counts[2]}")
    except IOError:
        print('파일 처리 과정에서 문제가 생겼습니다.') #에러를 메시지박스로 전달하면 좋겠지?
                                                    #요구사항도 에러메시지를 '팝업창'에 표시하라는 것이었다.
#tkiner
root = Tk()
root.title("문제 5")
root.geometry("520x220")

Label(root, text = "텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.").pack(pady=10)

Button(root, text = "파일 선택", command = select_file).pack(pady=6)

select_label = Label(root, text = "선택된 파일: (없음)")
select_label.pack(pady=11)

result_label = Label(root, text = "스페이스: 0, 대문자: 0, 소문자: 0")
result_label.pack()

root.mainloop()