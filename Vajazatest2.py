import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry.delete(





root = tk.Tk()
root.title("Kalkulator")


entry = tk.Entry(root, width=20 , font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1 ,1), ("9", 1 ,2), ("/", 1 ,3),
    ("4", 2 ,0), ("5", 2 ,1), ("6", 2 ,2), ("*", 2 ,3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 2, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("C", 4, 3),
]

for (text, row , col ) in buttons:
    button = tk.Button(root, text = text , font=("Arial", 18), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col , padx=5, pady=5, ipadx=10, ipady=10)



root.mainloop()



