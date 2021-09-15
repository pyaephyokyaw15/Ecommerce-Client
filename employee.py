#==================imports===================
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import datetime 
from tkinter import scrolledtext as tkst
import sys
from custom_button import TkinterCustomButton

#============================================

raw_name = sys.argv[1:]
print(raw_name)
name =' '.join(raw_name)
print(name)

# ==========================================

# Creat window
root = Tk()
root.title("Billing")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))
root.configure(background='#698c7b')
# ===========================================================================

# variables
total_amount = 0
id = StringVar()
quan= IntVar()

# =========================================================================

# Functions
def add():
    global total_amount
    item_id = id.get()
    print(item_id)
    sql_command = "SELECT item,price FROM inventory WHERE id = ?"
    cur.execute(sql_command, (item_id,))
    result = cur.fetchone()
    print(result)
    name = result[0]
    price = int(result[1])

    quantity = int(quan.get())
    amount = price*quantity
    total_amount += amount
    textarea.insert(END,'\n{}\t\t {}\t\t {}\t\t {}\n'.format(name, str(quantity).rjust(5), str(price).rjust(5), str(amount).rjust(10)))
    sql_command = "SELECT quantity FROM inventory WHERE id = ?"
    cur.execute(sql_command, (item_id,))
    remain_quan = int(cur.fetchone()[0])
    remain_quan -= quantity

    sql_command = ''' UPDATE inventory SET quantity = ?  WHERE id = ?'''
    cur.execute(sql_command, (remain_quan, item_id))

    db.commit()



def total():
    textarea.insert(END,'------------------------------------------------------------------------------------------------')
    textarea.insert(END,'\nTotal\t\t\t\t\t\t{}'.format(str(total_amount).rjust(10)))

def generate_bill():
    with open('bill.txt', 'w') as f:
        f.write(textarea.get("1.0",END))
    textarea.delete("2.0",END)
    
    

# =========================================================================
with sqlite3.connect("./Database/grocery_store.db") as db:
    cur = db.cursor()


Label(root, text = 'Billing Page', font="-family {Poppins} -size 40",background='#698c7b').place(relx=0.4, rely=0.05, anchor=W)

product = LabelFrame(root, text='Produts', font="-family {Poppins} -size 20")
product.place(relx= 0.02, rely=0.15, relwidth=0.45, relheight=0.5)

Label(product, text='Item-ID', font="-family {Poppins} -size 15").place(relx=0.02, rely=0.1)   #pack()
item_id = Entry(product, font="-family {Poppins} -size 15", textvariable= id)
# item_name.pack()
item_id.place(relx=0.1, rely=0.2, relwidth= 0.8, relheight=0.05)



Label(product, text='Quantity', font="-family {Poppins} -size 15").place(relx=0.02, rely=0.5)   #pack()
quantity = Entry(product, font="-family {Poppins} -size 15", textvariable=quan)
# item_name.pack()
quantity.place(relx=0.1, rely=0.6, relwidth= 0.8, relheight=0.05)


add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add To Cart", command=add)
# add_btn.pack()
add_btn.place(relx=0.4, rely=0.8)




# ==========================================================================

options = LabelFrame(root, text='Options', font="-family {Poppins} -size 20")
options.place(relx= 0.02, rely=0.7, relwidth=0.45, relheight=0.15)


total_btn = TkinterCustomButton(master=options, corner_radius=20,text="Total", command=total)
# add_btn.pack()
total_btn.place(relx=0.1, rely=0.3)


bill_btn = TkinterCustomButton(master=options, corner_radius=20,text="Bill", command=generate_bill)
# clear_btn.pack()
bill_btn.place(relx=0.4, rely=0.3)

exit_btn = TkinterCustomButton(master=options, corner_radius=20,text="Exit", command=exit)
# clear_btn.pack()
exit_btn.place(relx=0.7, rely=0.3)


# =========================================================================

# Bill Aera
bill_aera=Frame(root)
bill_aera.place(relx=0.5,rely=0.12,relwidth=0.45,relheight=0.78)
scrol_y=Scrollbar(bill_aera,orient=VERTICAL)
scrol_y.place(relx=0.98,rely=0, relheight=1, relwidth=0.02)
textarea=Text(bill_aera,font='arial 15',yscrollcommand=scrol_y.set)
textarea.place(relx=0, rely=0, relwidth=0.98, relheight=1)
textarea.insert(END,"\t\t\tMg Chat's Grocery Store\n\n")
textarea.insert(END,"\t\t          Open Daily : 7:30 AM to 9:0 PM\n\n")
textarea.insert(END,"\t\t**********************************************\n\n\n")
now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
hour = '{:02d}'.format(now.hour)
minute = '{:02d}'.format(now.minute)
day_month_year = '{}-{}-{}'.format(day, month, year)

textarea.insert(END,'    {}\t\t\t\t\t\t{}\n\n'.format(day_month_year,datetime.datetime.today().strftime("%I:%M %p")))
textarea.insert(END,'    {}\t\t\t\t\t\t{}\n\n'.format(''.join(random.choices(string.ascii_letters+string.digits,k=10)),name))
textarea.insert(END,"========================================================\n\n\n")
textarea.insert(END,'    Description\t\t  Qty\t\t  Price\t\t  Amount\n')

scrol_y.config(command=textarea.yview)


# Execute Tkinter
root.mainloop()
