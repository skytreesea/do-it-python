import tkinter as tk

def calculate_value():  # 먼저 창을 띄우기 전에 계산할 방법을 함수로 정의합니다. 
    initial_value = int(initial_entry.get()) # 첫번째 값을 initial_value라고 입력 받습니다. 
    rate = int(rate_entry.get()) #상승률을 rate라고 입력 받습니다.
    num_years = int(years_variable.get()) # 증가시킬 연도 수를 입력 받습니다.

    for i in range(num_years):
        new_value = initial_value * (1 + rate/100)**(i+1) # 계산법을 알려줍니다.
        result_label.config(text=f"Year {i+1}: {new_value:.2f}") # 소수점 두 자리 수까지 출력합니다. 
        
root = tk.Tk()
root.title("Yearly Growth Calculator")

# Create input widgets
initial_label = tk.Label(root, text="Initial Value") # 따옴표 안에 들아갈 값이 출력될 값이므로 여러분의 취향에 맞게 바꿔도 됩니다. 
initial_entry = tk.Entry(root) # 사의 Entry클래스를 이용하여 ‘최초 값’은 입력 받습니다. 
rate_label = tk.Label(root, text="Rate of Increase (%)")
rate_entry = tk.Entry(root)
years_label = tk.Label(root, text="Number of Years")
years_variable = tk.StringVar(root)
years_dropdown = tk.OptionMenu(root, years_variable, "1", "2", "3", "4", "5") # 드랍다운을 생성하는 방법도 이 문법을 통해서 알 수 있습니다. 

# Create button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate_value) # 실행시키면 calculate_value라는 명령어를 수행시키도록 되어 있네요. 처음에 입력했던 함수입니다. 

# Create label to display the result
result_label = tk.Label(root, text="Result", font=("Arial", 12), fg="blue") #출력할 폰트와 색상을 지정합니다. 

# Add widgets to the grid
initial_label.grid(row=0, column=0, padx=5, pady=5) # 입력받을 값이 어디에 위치할 지 지정해줍니다. 
initial_entry.grid(row=0, column=1, padx=5, pady=5)
rate_label.grid(row=1, column=0, padx=5, pady=5)
rate_entry.grid(row=1, column=1, padx=5, pady=5)
years_label.grid(row=2, column=0, padx=5, pady=5)
years_dropdown.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop() #전체 함수를 실행합니다. Loop는 반복이란 뜻으로 윈도우 창이 닫힐 때까지 실행한다는 뜻입니다. 
