import tkinter as tk  
root=tk.Tk() 
root.title("My calculator") 
root.geometry("300x400")
entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0,column=0,columnspan=4,pady=10)  
def click_button(item):
    entry.insert(tk.END, item)   

def clear_entry():
    entry.delete(0, tk.END)     

def calculate():
    try:
        result = str(eval(entry.get()))   
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error") 
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        b = tk.Button(root, text=button, width=10, height=3, command=calculate)
    else:
        b = tk.Button(root, text=button, width=10, height=3,
                      command=lambda b=button: click_button(b))
    b.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1 
clear_btn = tk.Button(root, text="C", width=10, height=3, command=clear_entry)
clear_btn.grid(row=row_val, column=col_val) 
root.mainloop()