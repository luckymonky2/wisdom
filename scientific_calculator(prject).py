import tkinter as tk
import math

# Evaluate the expression
def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('^', '**')  # Handle exponentiation
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Add character to input
def add_to_entry(char):
    entry.insert(tk.END, char)

# Clear the input
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Entry field
entry = tk.Entry(window, width=30, font=("Arial", 18), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin(', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan(', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3), ('+', 4, 4),
    ('log(', 5, 0), ('sqrt(', 5, 1), ('^', 5, 2), ('Clear', 5, 3), ('=', 5, 4)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'Clear':
        action = clear_entry
    else:
        action = lambda char=text: add_to_entry(char)

    tk.Button(window, text=text, width=5, height=2, command=action).grid(row=row, column=col)

# Start the app
window.mainloop()


calculate()