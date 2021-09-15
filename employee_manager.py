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

def add_employee():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' INSERT INTO employee (id,name,password,contact_num,address)
                    VALUES(?,?,?,?,?)'''
    cur.execute(sql_command, (str(new_ID.get()), str(new_name.get()), str(new_password.get()), str(new_contact.get()), str(new_address.get())))
    db.commit()
    table_display()
    new_ID.set('')
    new_password.set('')
    new_name.set('')
    new_contact.set('')
    new_address.set('')

def edit_employee():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' UPDATE employee SET name =?, password = ?, contact_num = ?, address = ?  WHERE id = ?'''
    cur.execute(sql_command, (str(new_name.get()), str(new_password.get()), str(new_contact.get()), str(new_address.get()), str(new_ID.get())))
    db.commit()
    table_display()
    new_ID.set('')
    new_password.set('')
    new_name.set('')
    new_contact.set('')
    new_address.set('')


def remove_employee():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' DELETE FROM employee  WHERE id = ?'''
    cur.execute(sql_command, [str(new_ID.get())])
    db.commit()
    table_display()
    new_ID.set('')
    new_password.set('')
    new_name.set('')
    new_contact.set('')
    new_address.set('')


def search():
    my_tree.delete(*my_tree.get_children())
    sql_command = ''' SELECT * FROM employee  WHERE id = ? OR name = ? OR password = ? OR contact_num =? OR address =?'''
    cur.execute(sql_command, (str(new_ID.get()),str(new_name.get()), str(new_password.get()), str(new_contact.get()), str(new_address.get()) ))
    db.commit()
    data = cur.fetchall()
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],record[2], record[3], record[4]))
        count += 1
    new_ID.set('')
    new_password('')
    new_name.set('')
    new_contact.set('')
    new_address.set('')



def table_display():
    with sqlite3.connect("./Database/grocery_store.db") as db:
        cur = db.cursor()
    sql_command = "SELECT * FROM employee"
    cur.execute(sql_command)
    data = cur.fetchall()
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],record[2], record[3], record[4]))
        count += 1



# Creat window
root = Tk()
root.title("Employee List")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))
root.config(background='#8daeb5')

# ===================variables============================

new_ID = StringVar()
new_name = StringVar()
new_password = StringVar()
new_contact = StringVar()
new_address = StringVar()

# =========================================================================
with sqlite3.connect("./Database/grocery_store.db") as db:
    cur = db.cursor()


Label(root, text = 'Employee List', font="-family {Poppins} -size 40",background='#8daeb5').place(relx=0.4, rely=0.05, anchor=W)

product = LabelFrame(root, text='Employee', font="-family {Poppins} -size 20")
product.place(relx= 0.05, rely=0.15, relwidth=0.45, relheight=0.7)

search_btn = TkinterCustomButton(master=product, corner_radius=20,text="Search", command=search)
search_btn.place(relx=0.01, rely=0.9)

add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add", command=add_employee)
add_btn.place(relx=0.21, rely=0.9)

remove_btn = TkinterCustomButton(master=product, corner_radius=20,text="Remove", command=remove_employee)
remove_btn.place(relx=0.41, rely=0.9)


edit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Edit", command=edit_employee)
edit_btn.place(relx=0.61, rely=0.9)


exit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Exit", command=exit)
exit_btn.place(relx=0.81, rely=0.9)
# ==========================================================================




# ID
Label(product, text='ID',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.05)
entry1 = Entry(product)
entry1.place(relx=0.25, rely=0.05, relwidth=0.7, relheight=0.05)
entry1.configure(font="-family {Poppins} -size 15")
entry1.configure(relief="flat")
entry1.configure(textvariable=new_ID)

# Name
Label(product, text='Name',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.2)
entry2 = Entry(product)
entry2.place(relx=0.25, rely=0.2, relwidth=0.7, relheight=0.05)
entry2.configure(font="-family {Poppins} -size 15")
entry2.configure(relief="flat")
entry2.configure(textvariable=new_name)

# password
Label(product, text='Password',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.35)
entry3 = Entry(product)
entry3.place(relx=0.25, rely=0.35, relwidth=0.7, relheight=0.05)
entry3.configure(font="-family {Poppins} -size 15")
entry3.configure(relief="flat")
entry3.configure(textvariable=new_password)

# contact no
Label(product, text='Contact No:',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.5)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_contact)

# address
Label(product, text='Address:',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.65)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.65, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_address)

# =========================================================================

# Items
item_aera=Frame(root)
item_aera.place(relx=0.52,rely=0.12,relwidth=0.5,relheight=0.78)

my_tree = ttk.Treeview(item_aera, height=10)
my_tree.place(relx=0,rely=0, relwidth=0.9, relheight=1)
style = ttk.Style()
style.configure("Treeview", font="-family {Poppins} -size 12", rowheight=30)
style.configure("Treeview.Heading", font="-family {Poppins} -size 14")

vsb = ttk.Scrollbar(item_aera, orient="vertical",command=my_tree.yview)
vsb.place(relx=0.9,rely=0, relheight=1)
my_tree.configure(yscrollcommand=vsb.set)



my_tree['columns'] = ('ID', 'Name', 'Password', 'Contact No', 'Address')

my_tree.column('#0', width=0, minwidth=0, stretch=NO )
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Name', anchor=CENTER, width=120)
my_tree.column('Password', anchor=CENTER, width=80)
my_tree.column('Contact No', anchor=CENTER, width=100)
my_tree.column('Address', anchor=CENTER, width=200)


table_display()


# Create Headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('ID', text = 'ID', anchor=CENTER)
my_tree.heading('Name', text = 'Name', anchor=CENTER)
my_tree.heading('Password', text = 'Password', anchor=CENTER)
my_tree.heading('Contact No', text = 'Phone', anchor=CENTER)
my_tree.heading('Address', text = 'Address', anchor=CENTER)





# Execute Tkinter
root.mainloop()
