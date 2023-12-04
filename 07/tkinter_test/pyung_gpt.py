import tkinter as tk

def convert():
    # '평' 값을 가져옵니다.
    pyeong = float(entry.get())
    # 3.3을 곱하여 제곱미터로 변환합니다.
    square_meter = pyeong * 3.3
    # 제곱미터 값을 라벨에 표시합니다.
    result_label.config(text=f"{square_meter} ㎡")

# tkinter 윈도우 생성
window = tk.Tk()
window.title("평방미터 변환기")


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
