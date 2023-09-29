import tkinter as tk

# 버튼 클릭 시 숫자와 연산자를 업데이트하는 함수
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "오류")

# GUI 창 생성
window = tk.Tk()
window.title("계산기")

# 입력 필드 생성
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# 버튼 생성
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# GUI 실행
window.mainloop()
