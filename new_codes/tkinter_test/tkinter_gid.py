import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="라벨 1")
label2 = tk.Label(root, text="라벨 2")

label1.grid(row=0, column=0)  # 라벨 1을 격자의 (0, 0) 위치에 배치합니다.
label2.grid(row=1, column=0)  # 라벨 2를 격자의 (1, 0) 위치에 배치합니다.

root.mainloop()
