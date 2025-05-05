import tkinter as tk
from functools import partial
from tkinter import INSERT, messagebox, ttk
from tkinter.simpledialog import askinteger

from PIL import ImageTk


def show_checkout():
    sub = tk.Tk()
    sub.geometry("800x600")
    sub.title("Order")

    global cart, prices

    cart = []
    prices = []

    details_frame = tk.LabelFrame(sub, text="Customer Details")
    details_frame.pack(fill="x", padx=10, pady=10)

    global lname_entry, fname_entry

    lname_label = tk.Label(details_frame, text="Last Name:")
    lname_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    lname_entry = tk.Entry(details_frame, textvariable=tk.StringVar())
    lname_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fname_label = tk.Label(details_frame, text="First Name:")
    fname_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    fname_entry = tk.Entry(details_frame, textvariable=tk.StringVar())
    fname_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    menu_frame = tk.LabelFrame(sub, text="Order Details")
    menu_frame.pack(fill="x", padx=10, pady=10)

    rice_pasta_label = tk.Label(menu_frame, text="Rice/Pasta Dish:")
    rice_pasta_label.grid(row=0, column=0, padx=5, pady=5)
    r_p_combo = ttk.Combobox(menu_frame, values=rp_dishes, state="readonly")
    r_p_combo.set("Pick a rice/pasta dish")
    r_p_combo.grid(row=0, column=1, padx=5, pady=5)
    r_p_qty_label = tk.Label(menu_frame, text="Qty:")
    r_p_qty_label.grid(row=0, column=2, padx=5, pady=5)
    r_p_qty_entry = tk.Entry(menu_frame, textvariable=tk.IntVar(), width=5)
    r_p_qty_entry.grid(row=0, column=3, padx=5, pady=5)
    r_p_submit = tk.Button(
        menu_frame,
        text="Add",
        command=partial(addOrder, r_p_combo, r_p_qty_entry, cart, prices),
    )
    r_p_submit.grid(row=0, column=4, padx=5, pady=5)

    protein_label = tk.Label(menu_frame, text="Protein Dish:")
    protein_label.grid(row=1, column=0, padx=5, pady=5)
    p_combo = ttk.Combobox(menu_frame, values=p_dishes, state="readonly")
    p_combo.set("Pick a protein dish")
    p_combo.grid(row=1, column=1, padx=5, pady=5)
    p_qty_label = tk.Label(menu_frame, text="Qty:")
    p_qty_label.grid(row=1, column=2, padx=5, pady=5)
    p_qty_entry = tk.Entry(menu_frame, textvariable=tk.IntVar(), width=5)
    p_qty_entry.grid(row=1, column=3, padx=5, pady=5)
    p_submit = tk.Button(
        menu_frame,
        text="Add",
        command=partial(addOrder, p_combo, p_qty_entry, cart, prices),
    )
    p_submit.grid(row=1, column=4, padx=5, pady=5)

    beverage_label = tk.Label(menu_frame, text="Beverage:")
    beverage_label.grid(row=2, column=0, padx=5, pady=5)
    b_combo = ttk.Combobox(menu_frame, values=b_dishes, state="readonly")
    b_combo.set("Pick a beverage")
    b_combo.grid(row=2, column=1, padx=5, pady=5)
    b_qty_label = tk.Label(menu_frame, text="Qty:")
    b_qty_label.grid(row=2, column=2, padx=5, pady=5)
    b_qty_entry = tk.Entry(menu_frame, textvariable=tk.IntVar(), width=5)
    b_qty_entry.grid(row=2, column=3, padx=5, pady=5)
    b_submit = tk.Button(
        menu_frame,
        text="Add",
        command=partial(addOrder, b_combo, b_qty_entry, cart, prices),
    )
    b_submit.grid(row=2, column=4, padx=5, pady=5)

    sidedish_label = tk.Label(menu_frame, text="Side Dish:")
    sidedish_label.grid(row=3, column=0, padx=5, pady=5)
    s_combo = ttk.Combobox(menu_frame, values=s_dishes, state="readonly")
    s_combo.set("Pick a side dish")
    s_combo.grid(row=3, column=1, padx=5, pady=5)
    s_qty_label = tk.Label(menu_frame, text="Qty:")
    s_qty_label.grid(row=3, column=2, padx=5, pady=5)
    s_qty_entry = tk.Entry(menu_frame, textvariable=tk.IntVar(), width=5)
    s_qty_entry.grid(row=3, column=3, padx=5, pady=5)
    s_submit = tk.Button(
        menu_frame,
        text="Add",
        command=partial(addOrder, s_combo, s_qty_entry, cart, prices),
    )
    s_submit.grid(row=3, column=4, padx=5, pady=5)

    swallow_label = tk.Label(menu_frame, text="Soup and Swallow Dish:")
    swallow_label.grid(row=4, column=0, padx=5, pady=5)
    ss_combo = ttk.Combobox(menu_frame, values=ss_dishes, state="readonly")
    ss_combo.set("Pick a soup & swallow dish")
    ss_combo.grid(row=4, column=1, padx=5, pady=5)
    ss_qty_label = tk.Label(menu_frame, text="Qty:")
    ss_qty_label.grid(row=4, column=2, padx=5, pady=5)
    ss_qty_entry = tk.Entry(menu_frame, textvariable=tk.IntVar(), width=5)
    ss_qty_entry.grid(row=4, column=3, padx=5, pady=5)
    ss_submit = tk.Button(
        menu_frame,
        text="Add",
        command=partial(addOrder, ss_combo, ss_qty_entry, cart, prices),
    )
    ss_submit.grid(row=4, column=4, padx=5, pady=5)

    button_frame = tk.Frame(sub)
    button_frame.pack(fill="x", padx=10, pady=10)

    bill_button = tk.Button(button_frame, text="Print Bill", command=show_bill)
    bill_button.pack(side="left", padx=5)

    bottom_frame = tk.Frame(sub)
    bottom_frame.pack(fill="x", padx=10, pady=10)

    global text_info
    text_info = tk.Text(bottom_frame)
    text_info.pack()

    root.mainloop()


def addOrder(index_entry, qty_entry, list1, list2):
    global index, qty

    index = index_entry.get()
    qty = int(qty_entry.get())

    for food in foods:
        for key in food.keys():
            if index == key:
                multiple = food[key] * qty
                list1.append(f"{index} x {qty} - {multiple}")
                list2.append(multiple)
                text_info.insert(INSERT, f"{index} x {qty} - {multiple}\n")


def show_bill():
    full_name = f"{lname_entry.get()} {fname_entry.get()}"

    bill = f"Customer Name: {full_name}\n"
    bill += f"\nOrders:\n"
    for item in cart:
        bill += f"{item}\n"
    bill += f"\nTotal Price: N{sum(prices)}\n"

    if sum(prices) > 5000:
        new_total = sum(prices) * 0.75
        bill += f"Order greater than N5000 - 25% discount\n"
        bill += f"\nNew Total: N{new_total}"
    elif sum(prices) > 2500:
        new_total = sum(prices) * 0.85
        bill += f"Order greater than 2500 - 15% discount\n"
        bill += f"\nNew Total: N{new_total}"
    elif sum(prices) < 2500 and sum(prices) >= 1000:
        new_total = sum(prices) * 0.9
        bill += f"Order less than N2500 - 10% discount\n"
        bill += f"\nNew Total: N{new_total}"
    else:
        bill += f"Order less than N1000 - no discount\n"

    messagebox.showinfo("Bill", bill)


rp_dishes = []
p_dishes = []
b_dishes = []
s_dishes = []
ss_dishes = []

root = tk.Tk()
root.title("PAU Cafeteria - Menu")
root.geometry("750x750")
root.resizable(False, False)

bg = ImageTk.PhotoImage(file="tea.png")

canvas = tk.Canvas(root, width=750, height=750)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_image(0, 0, image=bg, anchor="nw")

# Header
canvas.create_text(
    375, 50, font="times 28 bold italic underline", text="MENU", fill="white"
)

# Rice/Pasta
canvas.create_text(
    150,
    90,
    font="times 18 bold underline",
    text="RICE/PASTA",
    fill="black",
    justify="center",
)

rp_dict = {"Jollof Rice": 350, "Coconut Fried Rice": 350, "Jollof Spaghetti": 350}
l_start = 120
for k, v in rp_dict.items():
    canvas.create_text(
        57, l_start, font="times 14 bold", text=f"{k}", fill="black", anchor="w"
    )
    canvas.create_text(
        300, l_start, font="times 14 bold", text=f"{v}", fill="black", anchor="w"
    )
    l_start += 20
    rp_dishes.append(k)

# Proteins
canvas.create_text(
    550,
    90,
    font="times 18 bold underline",
    text="PROTEINS",
    fill="white",
    justify="left",
)

p_dict = {
    "Sweet Chili Chicken": 1100,
    "Grilled Chicken Wings": 400,
    "Fried Beef": 400,
    "Fried Fish": 500,
    "Boiled Egg": 200,
    "Sautered Sausages": 200,
}
r_start = 120
for k, v in p_dict.items():
    canvas.create_text(
        450, r_start, font="times 14 bold", text=f"{k}", fill="white", anchor="w"
    )
    canvas.create_text(
        680, r_start, font="times 14 bold", text=f"{v}", fill="white", anchor="e"
    )
    r_start += 20
    p_dishes.append(k)

# Beverages
canvas.create_text(
    550,
    290,
    font="times 18 bold underline",
    text="BEVERAGES",
    fill="white",
    justify="center",
)
b_dict = {
    "Water": 200,
    "Glass Drink (35cl)": 150,
    "PET Drink (35cl)": 300,
    "PET Drink (50cl)": 350,
    "Glass/Canned Malt": 500,
    "Fresh Yo": 600,
    "Pineapple Juice": 350,
    "Mango Juice": 350,
    "Zobo Drink": 350,
}
r_start = 320
for k, v in b_dict.items():
    canvas.create_text(
        450, r_start, font="times 14 bold", text=f"{k}", fill="white", anchor="w"
    )
    canvas.create_text(
        680, r_start, font="times 14 bold", text=f"{v}", fill="white", anchor="e"
    )
    r_start += 20
    b_dishes.append(k)

# Side dishes
canvas.create_text(
    150,
    230,
    font="times 18 bold underline",
    text="SIDE DISHES",
    fill="black",
    justify="center",
)

s_dict = {
    "Savoury Beans": 350,
    "Roasted Sweet Potatoes": 300,
    "Fried Plantains": 150,
    "Mixed Vegetable Salad": 150,
    "Boiled Yam": 150,
}
l_start = 260
for k, v in s_dict.items():
    canvas.create_text(
        57, l_start, font="times 14 bold", text=f"{k}", fill="black", anchor="w"
    )
    canvas.create_text(
        300, l_start, font="times 14 bold", text=f"{v}", fill="white", anchor="w"
    )
    l_start += 20
    s_dishes.append(k)

# Soups and Swallows
canvas.create_text(
    190,
    400,
    font="times 18 bold underline",
    text="SOUPS & SWALLOWS",
    fill="white",
    justify="center",
)

ss_dict = {
    "Eba": 100,
    "Pounded Yam": 100,
    "Semovita": 100,
    "Atama Soup": 450,
    "Egusi Soup": 400,
}
l_start = 430
for k, v in ss_dict.items():
    canvas.create_text(
        57, l_start, font="times 14 bold", text=f"{k}", fill="white", anchor="w"
    )
    canvas.create_text(
        300, l_start, font="times 14 bold", text=f"{v}", fill="white", anchor="w"
    )
    l_start += 20
    ss_dishes.append(k)

canvas.create_text(383, 550, font="times 22 bold italic", text="ENJOY!", fill="white")

order_button = tk.Button(
    canvas, text="Order Now", padx=6, pady=5, command=show_checkout
)
canvas.create_window(383, 580, window=order_button)

foods = [rp_dict, p_dict, b_dict, s_dict, ss_dict]
root.mainloop()
