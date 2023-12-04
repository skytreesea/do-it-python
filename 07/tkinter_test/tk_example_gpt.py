import tkinter as tk

def calculate():
    try:
        number = float(entry.get())
        result = number * 3.3
        output.config(text=f"{number} * 3.3 = {result}")
    except ValueError:
        output.config(text="Invalid input")

# Create a GUI window
window = tk.Tk()
window.title("Small Box")
window.geometry("300x150")

# Create a label and an entry box
label = tk.Label(window, text="Enter a number:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to calculate the result
button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

# Create a label to show the result
output = tk.Label(window, text="")
output.pack()

# Start the GUI loop
window.mainloop() 



