import tkinter as tk

root = tk.Tk()
root.title("Entry 예시")
root.geometry("300x100")

# Entry 위젯 생성
name_entry = tk.Entry(root)
name_entry.pack(pady=20)  # Entry 위젯을 부모 윈도우에 배치하고 여백을 추가

root.mainloop()
