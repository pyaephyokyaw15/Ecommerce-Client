import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton
import requests


# Creat window
root = Tk()
root.title("E-commerce Client")


# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))

# =============================================================================
# global variable
token =  None
domain = 'http://127.0.0.1:8000/api/v1/'

# Table
item_aera = Frame(root)
item_aera.place(relx=0.52, rely=0.12, relwidth=0.5, relheight=0.78)

my_tree = ttk.Treeview(item_aera, height=10)

# variables
em = StringVar()
passwd = StringVar()
ID = StringVar()
name = StringVar()
price = StringVar()
stock = StringVar()

# =============================================================================


def get_data():
    id = ID.get()
    product_name = name.get()
    product_price = price.get()
    product_stock = stock.get()

    ID.set('')
    name.set('')
    price.set('')
    stock.set('')

    return id, product_name, product_price, product_stock


def add_product():
    id, name, price, stock = get_data()

    url = domain + 'products/'
    body = {
        "name": name,
        "price": price,
        "stock": stock,
        "image": None
    }
    results = requests.post(url, json=body, headers={"Authorization": "Token "+token})
    print(results)
    status_code = results.status_code
    result_json = results.json()
    print(result_json)
    message = result_json['message']

    if status_code != 201:
        messagebox.showerror("Error", message)
    else:
        my_tree.delete(*my_tree.get_children())
        table_display(my_tree)

def delete_product():
    id, name, price, stock = get_data()

    url = f'{domain}products/{id}/'
    results = requests.delete(url, headers={"Authorization": "Token " + token})
    print(results)
    status_code = results.status_code


    if status_code != 204:
        messagebox.showerror("Error", "Not Found")
    else:
        my_tree.delete(*my_tree.get_children())
        table_display(my_tree)

def edit_product():
    id, name, price, stock = get_data()

    url = f'{domain}products/{id}/'
    body = {
        "name": name,
        "price": price,
        "stock": stock,
        "image": None
    }
    results = requests.put(url, json=body, headers={"Authorization": "Token " + token})
    print(results)
    status_code = results.status_code
    result_json = results.json()
    print(result_json)
    message = result_json['message']

    if status_code != 200:
        messagebox.showerror("Error", message)
    else:
        my_tree.delete(*my_tree.get_children())
        table_display(my_tree)


def inventory():
    Label(root, text='Inventory', font="-family {Poppins} -size 40").place(relx=0.4, rely=0.05, anchor=W)

    product = LabelFrame(root, text='Items', font="-family {Poppins} -size 20")
    product.place(relx=0.05, rely=0.15, relwidth=0.45, relheight=0.7)


    add_btn = TkinterCustomButton(master=product, corner_radius=20, text="Add", command=add_product)
    add_btn.place(relx=0.21, rely=0.9)

    remove_btn = TkinterCustomButton(master=product, corner_radius=20, text="Delete", command=delete_product)
    remove_btn.place(relx=0.41, rely=0.9)

    edit_btn = TkinterCustomButton(master=product, corner_radius=20, text="Edit", command=edit_product)
    edit_btn.place(relx=0.61, rely=0.9)


    # ==========================================================================

    # ID
    Label(product, text='ID(only for edit and delete)', font="-family {Poppins} -size 14").place(relx=0.05, rely=0.1)
    entry1 = Entry(product)
    entry1.place(relx=0.05, rely=0.15, relwidth=0.7, relheight=0.05)
    entry1.configure(font="-family {Poppins} -size 14")
    entry1.configure(relief="flat")
    entry1.configure(textvariable=ID)

    # Item
    Label(product, text='Product Name', font="-family {Poppins} -size 14").place(relx=0.05, rely=0.3)
    entry2 = Entry(product)
    entry2.place(relx=0.05, rely=0.35, relwidth=0.7, relheight=0.05)
    entry2.configure(font="-family {Poppins} -size 14")
    entry2.configure(relief="flat")
    entry2.configure(textvariable=name)

    # quantity
    Label(product, text='In Stock', font="-family {Poppins} -size 14").place(relx=0.05, rely=0.5)
    entry3 = Entry(product)
    entry3.place(relx=0.05, rely=0.55, relwidth=0.7, relheight=0.05)
    entry3.configure(font="-family {Poppins} -size 14")
    entry3.configure(relief="flat")
    entry3.configure(textvariable=price)

    # price
    Label(product, text='Price', font="-family {Poppins} -size 14").place(relx=0.05, rely=0.7)
    entry4 = Entry(product)
    entry4.place(relx=0.05, rely=0.75, relwidth=0.7, relheight=0.05)
    entry4.configure(font="-family {Poppins} -size 14")
    entry4.configure(relief="flat")
    entry4.configure(textvariable=stock)



    my_tree.place(relx=0, rely=0, relwidth=0.9, relheight=1)
    style = ttk.Style()
    style.configure("Treeview", font="-family {Poppins} -size 12", rowheight=30)
    style.configure("Treeview.Heading", font="-family {Poppins} -size 15")

    vsb = ttk.Scrollbar(item_aera, orient="vertical", command=my_tree.yview)
    vsb.place(relx=0.9, rely=0, relheight=1)
    my_tree.configure(yscrollcommand=vsb.set)

    my_tree['columns'] = ('ID', 'Name', 'Price', 'Stock', 'Category')

    my_tree.column('#0', width=0, minwidth=0, stretch=NO)
    my_tree.column('ID', anchor=W, width=50)
    my_tree.column('Name', anchor=W, width=200)
    my_tree.column('Price', anchor=E, width=50)
    my_tree.column('Stock', anchor=E, width=50)
    my_tree.column('Category', anchor=CENTER, width=200)


    # Create Headings
    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=CENTER)
    my_tree.heading('Name', text='Name', anchor=CENTER)
    my_tree.heading('Price', text='Stock', anchor=CENTER)
    my_tree.heading('Stock', text='Price', anchor=CENTER)
    my_tree.heading('Category', text='Category', anchor=CENTER)

    table_display(my_tree)



def table_display(my_tree):
    url = domain + 'staff-products/'

    results = requests.get(url, headers={"Authorization": "Token " + token})
    print(results)
    status_code = results.status_code
    result_json = results.json()
    print(result_json)
    message = result_json['message']
    data = result_json["result"]["data"]
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(
            record["id"], record["name"], record["price"], record["stock"], record["category"]["name"]
        ))
        count += 1

def login():
    global token


    email = em.get()
    password = passwd.get()
    print(email)
    print(password)

    em.set('')
    passwd.set('')


    login_url = domain + 'auth/token/'
    body = {
        "email": email,
        "password": password
    }

    results = requests.post(login_url, json=body)
    print(results)
    status_code = results.status_code
    result_json = results.json()
    print(result_json)
    message = result_json['message']


    if status_code == 200:
        # root.withdraw()
        # os.system("python inventory.py")
        # root.deiconify()
        token = result_json['result']['token']
        print(token)
        login_window.destroy()
        inventory()
    else:
        messagebox.showerror("Error", message)

# ==============================================================================
# login Screen
login_window = LabelFrame(root, text='Login', font="-family {Poppins} -size 20")
login_window.place(relx= 0.3, rely=0.3, relwidth=0.4, relheight=0.4)


# email label
Label(login_window,text='Email', font="-family {Poppins} -size 14" ).place(relx=0.1, rely=0.1)

# login entry
entry1 = Entry(master=login_window)
entry1.place(relx=0.1, rely=0.2, relwidth=0.7, relheight=0.1)
entry1.configure(font="-family {Poppins} -size 14")
entry1.configure(relief="flat")
entry1.configure(textvariable=em)


#password label
Label(login_window,text='Password', font="-family {Poppins} -size 14" ).place(relx=0.1, rely=0.4)
# password entry
entry2 = Entry(master=login_window)
entry2.place(relx=0.1, rely=0.5, relwidth=0.7, relheight=0.1)
entry2.configure(font="-family {Poppins} -size 14")
entry2.configure(relief="flat")
entry2.configure(show="*")
entry2.configure(textvariable=passwd)

# login_buttons
button1 = TkinterCustomButton(master=login_window, corner_radius=20,text="LOGIN", command=login)
button1.place(relx=0.5, rely=0.8,  anchor=CENTER)







    

root.mainloop()


