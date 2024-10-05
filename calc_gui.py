import tkinter as tk
import math

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "enter a value")

def calculate_function(func):
    try:
        current = display.get()
        val = float(current)
        result = 0
        if func == 'log':
            result = math.log(val)
        elif func == 'sin':
            result = math.sin(math.radians(val))
        elif func == 'cos':
            result = math.cos(math.radians(val))
        elif func == 'tan':
            result = math.tan(math.radians(val))
        elif func == 'cot':
            result = 1 / math.tan(math.radians(val))
        elif func == 'sec':
            result = 1 / math.cos(math.radians(val))
        elif func == 'cosec':
            result = 1 / math.sin(math.radians(val))
        elif func == 'arcsin':
            result = math.degrees(math.asin(val))
        elif func == 'arccos':
            result = math.degrees(math.acos(val))
        elif func == 'arctan':
            result = math.degrees(math.atan(val))
        elif func == 'arccot':
            result = math.degrees(math.atan(1 / val))
        elif func == 'arcsec':
            result = math.degrees(math.acos(1 / val))
        elif func == 'arccosec':
            result = math.degrees(math.asin(1 / val))

        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
#window creation
window = tk.Tk()
window.title("Advanced Calculator")
#display
display = tk.Entry(window, width=40, justify="right")
display.grid(row=0, column=0, columnspan=30, padx=30, pady=30)
#continous numbers generation
for i in range(1, 10):
    tk.Button(window, text=str(i), command=lambda x=i: button_click(x)).grid(row=(i-1)//3 + 1, column=(i-1)%3)

tk.Button(window, text="0", width=5, command=lambda: button_click(0)).grid(row=4, column=1)
tk.Button(window, text=".", width=5, command=lambda: button_click('.')).grid(row=4, column=0)

tk.Button(window, text="+", width=5, command=lambda: button_click('+')).grid(row=1, column=3)
tk.Button(window, text="-", width=5, command=lambda: button_click('-')).grid(row=2, column=3)
tk.Button(window, text="*", width=5, command=lambda: button_click('*')).grid(row=3, column=3)
tk.Button(window, text="/", width=5, command=lambda: button_click('/')).grid(row=4, column=3)

tk.Button(window, text="=", width=5, command=calculate).grid(row=4, column=2)
tk.Button(window, text="C", width=5, command=clear).grid(row=4, column=4)
tk.Button(window, text="%", width=5, command=lambda: button_click('%')).grid(row=5, column=4)

tk.Button(window, text="log", width=5, command=lambda: calculate_function('log')).grid(row=1, column=4)
tk.Button(window, text="sin", width=5, command=lambda: calculate_function('sin')).grid(row=1, column=5)
tk.Button(window, text="cos", width=5, command=lambda: calculate_function('cos')).grid(row=2, column=5)
tk.Button(window, text="tan", width=5, command=lambda: calculate_function('tan')).grid(row=3, column=5)
tk.Button(window, text="cot", width=5, command=lambda: calculate_function('cot')).grid(row=4, column=5)

tk.Button(window, text="cosec", width=5, command=lambda: calculate_function('cosec')).grid(row=2, column=4)
tk.Button(window, text="sec", width=5, command=lambda: calculate_function('sec')).grid(row=3, column=4)
tk.Button(window, text="arcsin", width=5, command=lambda: calculate_function('arcsin')).grid(row=1, column=6)
tk.Button(window, text="arccos", width=5, command=lambda: calculate_function('arccos')).grid(row=2, column=6)
tk.Button(window, text="arctan", width=5, command=lambda: calculate_function('arctan')).grid(row=3, column=6)
tk.Button(window, text="arccot", width=5, command=lambda: calculate_function('arccot')).grid(row=4, column=6)
tk.Button(window, text="arcsec", width=5, command=lambda: calculate_function('arcsec')).grid(row=5, column=5)
tk.Button(window, text="arccosec", width=5, command=lambda: calculate_function('arccosec')).grid(row=5, column=6)

window.mainloop()
