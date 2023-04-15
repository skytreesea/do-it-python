import tkinter as tk

def calculate_value():
    initial_value = float(initial_entry.get())
    rate = float(rate_entry.get())
    num_years = int(years_variable.get())

    for i in range(num_years):
        new_value = initial_value * (1 + rate/100)**(i+1)
        result_label.config(text=f"Year {i+1}: {new_value:.2f}")

root = tk.Tk()
root.title("Yearly Growth Calculator")

# Create input widgets
initial_label = tk.Label(root, text="Initial Value")
initial_entry = tk.Entry(root)
rate_label = tk.Label(root, text="Rate of Increase (%)")
rate_entry = tk.Entry(root)
years_label = tk.Label(root, text="Number of Years")
years_variable = tk.StringVar(root)
years_dropdown = tk.OptionMenu(root, years_variable, "1", "2", "3", "4", "5")

# Create button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate_value)

# Create label to display the result
result_label = tk.Label(root, text="Result", font=("Arial", 12), fg="blue")

# Add widgets to the grid
initial_label.grid(row=0, column=0, padx=5, pady=5)
initial_entry.grid(row=0, column=1, padx=5, pady=5)
rate_label.grid(row=1, column=0, padx=5, pady=5)
rate_entry.grid(row=1, column=1, padx=5, pady=5)
years_label.grid(row=2, column=0, padx=5, pady=5)
years_dropdown.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
