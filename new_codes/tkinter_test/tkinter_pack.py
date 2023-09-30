import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()  # 부모 위젯에 적절하게 배치합니다.

button1 = tk.Button(frame, text="버튼 1")
button2 = tk.Button(frame, text="버튼 2")

button1.pack()  # 버튼 1을 부모 프레임에 배치합니다.
button2.pack()  # 버튼 2를 부모 프레임에 배치합니다.

root.mainloop()

import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="라벨 1")
label2 = tk.Label(root, text="라벨 2")

label1.grid(row=0, column=0)  # 라벨 1을 격자의 (0, 0) 위치에 배치합니다.
label2.grid(row=1, column=0)  # 라벨 2를 격자의 (1, 0) 위치에 배치합니다.

root.mainloop()

