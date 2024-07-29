import tkinter as tk
import operator

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operator = operator_entry.get()

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        else:
            result = "Invalid operator"
    except ValueError:
        result = "Invalid input"

    result_label.config(text=f"Result: {result}")


root = tk.Tk()
root.title('Simple calculator')
root.geometry('500x400')
root.configure(bg='darkblue')

tk.Label(root, text="enter your first number: ", bg='darkblue', fg='white').pack()
entry1 = tk.Entry(root)
entry1.pack(fill='x')

tk.Label(root, text='enter your operater: ', bg='darkblue', fg='white').pack()
operator_entry = tk.Entry(root)
operator_entry.pack(fill='x')

tk.Label(root, text=' enter your second number: ', bg='darkblue', fg='white').pack()
entry2 = tk.Entry(root)
entry2.pack(fill='x')


tk.Button(root, text="Calculate", command=calculate, bg='green', fg='white').pack()

result_label = tk.Label(root, text='Result: ', bg='darkblue', fg='white')
result_label.pack()

root.mainloop()
