#SIMPLE CALCULATOR APPLICATION...
import tkinter as tk
def on_click(e):

    text = e.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "DEL":
        entry.delete(len(entry.get())-1,tk.END)
    elif text == "exp":
        entry.insert(tk.END, "**")
    elif text == "sq":
        entry.insert(tk.END,"**2")
    else:
        entry.insert(tk.END, text)

window = tk.Tk()
window.title("CALCULATOR")

entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10)

buttons = [
    'C','DEL','exp','sq',
    '7', '8', '9','/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()

