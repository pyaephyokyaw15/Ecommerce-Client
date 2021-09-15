import os
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton


option = 0
# Database Connection
with sqlite3.connect('Database/grocery_store.db') as db:
    cur = db.cursor()


# Creat window
root = Tk()
root.title("Grocery Store")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))

# ==============================================================================

# Functions
def inventory():
    root.withdraw()
    os.system("python inventory.py")
    root.deiconify()
        
def employee_manager():
    root.withdraw()
    os.system("python employee_manager.py")
    root.deiconify()
    
#===============================================================================

# Background photo
# Make To be compatible with tkinter and resize photo
bg_photo = Image.open('images/home.jpg')
bg_photo = bg_photo. resize((window_width, window_height), Image. ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_photo)

# Place on the window
Label(root, image=bg_photo).place(relx=0, rely=0)


# Photo for Admin button
admin_logo = ImageTk.PhotoImage(Image.open("images/inventory.png").resize((200, 200)))

# Create Admin button
button1 = Button(root,image=admin_logo, borderwidth=5, bg='#cadbc3', command=inventory, relief=RIDGE )
button1.place(relx=0.25, rely=0.4, width=200, height=200)
Label(root, text = 'Inventory', font=('Arial', 15), bg='#ede5dd').place(relx=0.255, rely=0.6)


# Photo for Employee button
employee_logo = ImageTk.PhotoImage(Image.open("images/team.png").resize((200, 200)))

# Create Employee button
button2 = Button(root,image=employee_logo, borderwidth=5, bg='#cadbc3', command=employee_manager, relief=RIDGE )
button2.place(relx=0.65, rely=0.4, width=200, height=200)
Label(root, text = 'Employees', font=('Arial', 15), bg='#ede5dd').place(relx=0.655, rely=0.6)

# ===============================================================================================





# Execute Tkinter
root.mainloop()

