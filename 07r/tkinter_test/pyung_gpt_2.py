import tkinter as tk

def convert():
# 선택된 변환 단위에 따라 변환 계수를 결정합니다
    if unit.get() == "평으로 바꾸기":
        factor = 1/3.3
        result_unit = "평"
    else:
        factor = 3.3
        result_unit = "제곱미터"
    # 입력된 값에서 계수를 곱하여 변환합니다
    value = float(entry.get())
    # 반복되는 수를 피하기 위해서 round를 설정했습니다. 
    result = round(value * factor,1)
    # 변환 결과를 레이블에 표시합니다
    result_label.config(text=f"{result} {result_unit}")

# tkinter 윈도우 생성
window = tk.Tk()

# 변환 단위를 선택할 드롭다운 위젯 생성
unit_options = ["평으로 바꾸기", "제곱미터로s 바꾸기"]
unit = tk.StringVar(value=unit_options[0]) # 초깃값 설정
unit_dropdown = tk.OptionMenu(window, unit, *unit_options)
unit_dropdown.pack()

# '평' 값을 입력받는 엔트리 위젯 생성
entry = tk.Entry(window, width=10)
entry.pack()

# 변환 버튼 생성
button = tk.Button(window, text="변환", command=convert)
button.pack()

# 변환 결과를 표시할 라벨 생성
result_label = tk.Label(window)
result_label.pack()

# tkinter 이벤트 루프 시작
window.mainloop()
