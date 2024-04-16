import tkinter as tk
from tkinter import messagebox

def showCharge(location, weight):
    window = tk.Toplevel(root)
    window.title("Simi Services - Charge")
    window.geometry("300x100")
    
    if location == "Ibeju-Lekki" and weight >= 10:
        txt = "That will cost you N5,000 only!"
    elif location == "Ibeju-Lekki" and weight < 10:
        txt = "That will cost you N3,500 only!"
    elif location == "Epe" and weight >= 10:
        txt = "That will cost you N10,000 only!"
    elif location == "Epe" and weight < 10:
        txt = "That will cost you N5,000 only!"
    else:
        txt = "Sorry, we don't deliver to that location!"
        
    label = tk.Label(window, text=txt)
    label.pack()
    
    root.mainloop()

def submit():
    location = location_entry.get()
    weight = int(weight_entry.get())
    
    showCharge(location, weight)
    
root = tk.Tk()
root.title("Simi Services")
root.geometry("500x200")

location_label = tk.Label(root, text="Delivery Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

weight_label = tk.Label(root, text="Weight(in kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

submit_button = tk.Button(root, text="Check", command=submit)
submit_button.pack()

root.mainloop()