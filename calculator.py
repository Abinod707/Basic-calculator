import tkinter as tk

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button click
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        
        if btn_text == "=":
            btn.config(command=calculate)
        elif btn_text == "C":
            btn.config(command=clear)
        else:
            btn.config(command=lambda txt=btn_text: button_click(txt))

# Run the application
root.mainloop()
