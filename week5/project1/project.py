import tkinter as tk
from tkinter import messagebox
import csv

def entryMessage(f_name, l_name):
    # Create a new Tkinter window to show employees in the same department
    dept = dept_entry.get()
    window = tk.Toplevel(root)
    window.title("Employee List")
    window.geometry("800x600")
    
    label1 = tk.Label(window, text=f"Welcome, {l_name} {f_name}!\n")
    label1.pack()
    label2 = tk.Label(window, text="These employees are your fellows in the same department:")
    label2.pack()
    
    for val in details.values():
        if val[2] == dept.title() and val[0] != l_name.upper():
            tk.Label(window, text=f"{val[0]} {val[1]}").pack()
        else:
            continue
    
    root.mainloop()
        
def submit():
    first_name = f_name_entry.get()
    last_name = l_name_entry.get()
    dept = dept_entry.get()
    
    check = []
    
    for val in details.values():
        if val[0] == last_name.upper() and val[1] == first_name.title() and val[2] == dept.title():
            check = val
        else:
            continue
    if check in details.values():
        entryMessage(check[1],check[0])
    else:
        messagebox.showerror("Login", "Invalid credentials!")

details = {}

with open('GIG-logistics.csv') as file:
    c_read = list(csv.reader(file))
    
    for i in range(len(c_read)):
        if i == 0:
            continue
        else:
            details[c_read[i][0]] = c_read[i][1:]
    file.close()
    
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

f_name_label = tk.Label(root, text="First Name:")
f_name_label.pack()
f_name_entry = tk.Entry(root)
f_name_entry.pack()

l_name_label = tk.Label(root, text="Last Name:")
l_name_label.pack()
l_name_entry = tk.Entry(root)
l_name_entry.pack()

dept_label = tk.Label(root, text="Department:")
dept_label.pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()