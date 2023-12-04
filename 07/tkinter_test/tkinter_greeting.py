import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + name_entry.get() + "!")

root = tk.Tk()
root.title("Greeting App")
root.geometry("300x150")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=on_button_click)
button.pack(pady=10)

root.mainloop()
