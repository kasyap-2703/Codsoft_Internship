import tkinter as tk

def calculator():
    a = float(Entry_a.get())
    b = float(Entry_b.get())
    operation = operator.get()
    
    if operation == "+":
        ans = a + b
    elif operation == "-":
        ans = a - b
    elif operation == "*":
        ans = a * b
    elif operation == "/":
        if b != 0:
            ans = a / b
        else:
            ans = "Error: Division by zero"
    else:
        ans = "Invalid operation"
    
    ans_label.config(text="ans: " + str(ans))

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")

# Number inputs
Entry_a = tk.Entry(root)
Entry_a.pack()

Entry_b = tk.Entry(root)
Entry_b.pack()

# Operator selection
operator = tk.StringVar()
operator.set("+")  # Default operator

operator_menu = tk.OptionMenu(root, operator, "+", "-", "*", "/")
operator_menu.pack()

# calculator button
calculator_button = tk.Button(root, text="calculate", command=calculator)
calculator_button.pack()

# answer label
ans_label = tk.Label(root, text="answer:")
ans_label.pack()

root.mainloop()
