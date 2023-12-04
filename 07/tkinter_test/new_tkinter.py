import tkinter as tk

root = tk.Tk()  # 기본 창을 생성합니다.
root.title("My First tkinter App")  # 창의 제목을 설정합니다.
root.geometry("300x200")  # 창의 크기를 설정합니다.

label = tk.Label(root, text="안녕 나는 팅커야!")
label.pack()
a = 0 
def on_button_click():
    global a
    print(f'{a}번 클릭되었습니다')
    a +=1
 
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

root.mainloop()  # 이벤트 루프를 시작합니다.