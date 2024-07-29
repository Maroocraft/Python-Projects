
import tkinter as tk

def bmi():
    try:
        weight = float(entry1.get())
        height = float(entry2.get())
        result = weight / pow(height / 100, 2)
        if result >= 25.0:
            result_label.config(text=f'{result}: You are overweight')
        elif result >= 18.5:
            result_label.config(text=f'{result}: You are normal')
        elif result <= 18.5:
            result_label.config(text=f'{result}: You are underweight')
        else:
           result_label.config(text='invalid input ')
    except ValueError:
         result_label.config(text=f'invalid input')

root = tk.Tk()
root.title('BMI calculator')
root.geometry('400x300')
root.configure(bg = '#3dd9bc')

tk.Label(root, text='Enter you weight (kg) : ', bg = '#3dd9bc').pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text='Enter your height (cm): ', bg = '#3dd9bc').pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text='calculate', command=bmi).pack()

result_label = tk.Label(root, text='Result:', bg = '#3dd9bc')
result_label.pack()

root.mainloop()
