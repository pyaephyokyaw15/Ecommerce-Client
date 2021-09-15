#==================imports===================
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
import sys
from custom_button import TkinterCustomButton

def add_item():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' INSERT INTO inventory (id,item,quantity,price)
                    VALUES(?,?,?,?)'''
    cur.execute(sql_command, (str(new_ID.get()), str(new_item.get()), str(new_quantity.get()), str(new_price.get())))
    db.commit()
    table_display()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    

def edit_item():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' UPDATE inventory SET item =?, quantity = ?, price = ?  WHERE id = ?'''
    cur.execute(sql_command, (str(new_item.get()), str(new_quantity.get()), str(new_price.get()), str(new_ID.get())))
    db.commit()
    table_display()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')


def remove_item():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' DELETE FROM inventory  WHERE id = ?'''
    cur.execute(sql_command, [str(new_ID.get())])
    db.commit()
    table_display()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')


def search():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' SELECT * FROM inventory  WHERE id = ? OR item = ? OR quantity = ? OR price =?'''
    cur.execute(sql_command, (str(new_ID.get()),str(new_item.get()), str(new_quantity.get()), str(new_price.get())))
    db.commit()
    data = cur.fetchall()
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],record[2], record[3]))
        count += 1
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')



def table_display():
    with sqlite3.connect("./Database/grocery_store.db") as db:
        cur = db.cursor()
    sql_command = "SELECT * FROM inventory ORDER BY quantity ASC"
    cur.execute(sql_command)
    data = cur.fetchall()
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],record[2], record[3]))
        count += 1



# Creat window
root = Tk()
root.title("Inventory")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))
root.config(background='#73695f')

# ===================variables============================

new_ID = StringVar()
new_item = StringVar()
new_quantity = StringVar()
new_price = StringVar()

# =========================================================================
with sqlite3.connect("./Database/grocery_store.db") as db:
    cur = db.cursor()


Label(root, text = 'Inventory', font="-family {Poppins} -size 40", background='#73695f').place(relx=0.4, rely=0.05, anchor=W)

product = LabelFrame(root, text='Items', font="-family {Poppins} -size 20")
product.place(relx= 0.05, rely=0.15, relwidth=0.45, relheight=0.7)

search_btn = TkinterCustomButton(master=product, corner_radius=20,text="Search", command=search)
search_btn.place(relx=0.01, rely=0.9)

add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add Item", command=add_item)
add_btn.place(relx=0.21, rely=0.9)

remove_btn = TkinterCustomButton(master=product, corner_radius=20,text="Remove Item", command=remove_item)
remove_btn.place(relx=0.41, rely=0.9)


edit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Edit Item", command=edit_item)
edit_btn.place(relx=0.61, rely=0.9)


exit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Exit", command=exit)
exit_btn.place(relx=0.81, rely=0.9)
# ==========================================================================




# ID
Label(product, text='ID',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.1)
entry1 = Entry(product)
entry1.place(relx=0.25, rely=0.1, relwidth=0.7, relheight=0.05)
entry1.configure(font="-family {Poppins} -size 15")
entry1.configure(relief="flat")
entry1.configure(textvariable=new_ID)

# Item
Label(product, text='Item',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.3)
entry2 = Entry(product)
entry2.place(relx=0.25, rely=0.3, relwidth=0.7, relheight=0.05)
entry2.configure(font="-family {Poppins} -size 15")
entry2.configure(relief="flat")
entry2.configure(textvariable=new_item)

# quantity
Label(product, text='In Stock',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.5)
entry3 = Entry(product)
entry3.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.05)
entry3.configure(font="-family {Poppins} -size 15")
entry3.configure(relief="flat")
entry3.configure(textvariable=new_quantity)

# price
Label(product, text='Price',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.7)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.7, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_price)



# =========================================================================

# Items
item_aera=Frame(root)
item_aera.place(relx=0.52,rely=0.12,relwidth=0.5,relheight=0.78)

my_tree = ttk.Treeview(item_aera, height=10)
my_tree.place(relx=0,rely=0, relwidth=0.9, relheight=1)
style = ttk.Style()
style.configure("Treeview", font="-family {Poppins} -size 12", rowheight=30)
style.configure("Treeview.Heading", font="-family {Poppins} -size 15")

vsb = ttk.Scrollbar(item_aera, orient="vertical",command=my_tree.yview)
vsb.place(relx=0.9,rely=0, relheight=1)
my_tree.configure(yscrollcommand=vsb.set)



my_tree['columns'] = ('Item-ID', 'Item', 'Quantity', 'Price')

my_tree.column('#0', width=0, minwidth=0, stretch=NO )
my_tree.column('Item-ID', anchor=W, width=100)
my_tree.column('Item', anchor=W, width=200)
my_tree.column('Quantity', anchor=E, width=50)
my_tree.column('Price', anchor=E, width=50)


table_display()


# Create Headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Item-ID', text = 'Item ID', anchor=CENTER)
my_tree.heading('Item', text = 'Item', anchor=CENTER)
my_tree.heading('Quantity', text = 'In Stock', anchor=CENTER)
my_tree.heading('Price', text = 'Price', anchor=CENTER)




# Execute Tkinter
root.mainloop()
