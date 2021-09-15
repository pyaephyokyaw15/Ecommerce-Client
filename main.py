import os
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton

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

# =============================================================================

# variables
user = StringVar()
passwd = StringVar()
option = 0

# =============================================================================
def login():

    username = user.get()
    password = passwd.get()
    print(username)
    print(password)

    user.set('')
    passwd.set('')

    if option==1:
        find_user = "SELECT * FROM admin WHERE id = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchone()
        print(results)
    
        if results:
            
            login_window.withdraw()
            root.withdraw()
            os.system("python admin.py")
            root.deiconify()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            
    
    if option==2:
        find_user = "SELECT name FROM employee WHERE id = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchone()
        print(results)
        
        if results:
            login_window.withdraw()
            root.withdraw()
            os.system("python employee.py {}".format(results[0]))
            root.deiconify()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")

# ==============================================================================
# login Screen
login_window = Toplevel(root)

login_window.title("Login")
login_window.geometry("{}x{}+{}+{}".format(window_width//7, window_height//3,
                        int(window_width/2.3), window_height//3))
login_window.iconbitmap('images\login.ico')

# login logo
login_logo = ImageTk.PhotoImage(Image.open("images/user_name.png").resize((20, 20)))
Label(login_window, image=login_logo).place(relx=0.1, rely=0.2)
Label(login_window,text='Username', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.1)

# login entry
entry1 = Entry(login_window)
entry1.place(relx=0.25, rely=0.2, relwidth=0.7, relheight=0.08)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user)

# password logo
password_logo = ImageTk.PhotoImage(Image.open("images/password.png").resize((20, 20)))
Label(login_window, image=password_logo).place(relx=0.1, rely=0.5)
Label(login_window,text='Password', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.4)

# password entry
entry2 = Entry(login_window)
entry2.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.08)
entry2.configure(font="-family {Poppins} -size 10")
entry2.configure(relief="flat")
entry2.configure(show="*")
entry2.configure(textvariable=passwd)

# login_buttons
button1 = TkinterCustomButton(master=login_window, corner_radius=20,text="LOGIN", command=login)
button1.place(relx=0.5, rely=0.8,  anchor=CENTER)

# hide
login_window.withdraw()
    


# Functions
def admin():
    global option
    option = 1
    # pop-up login page
    
    login_window.deiconify()
    
def employee():
    global option
    option = 2
    login_window.deiconify()
    
    # pop-up login page
    


    





      


#===============================================================================

# Background photo
# Make To be compatible with tkinter and resize photo
bg_photo = Image.open('images/home.jpg')
bg_photo = bg_photo. resize((window_width, window_height), Image. ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_photo)

# Place on the window
Label(root, image=bg_photo).place(relx=0, rely=0)


# Photo for Admin button
admin_logo = ImageTk.PhotoImage(Image.open("images/admin.png").resize((200, 200)))

# Create Admin button
button1 = Button(root,image=admin_logo, borderwidth=5, bg='#cadbc3', command=admin, relief=RIDGE )
button1.place(relx=0.25, rely=0.4, width=200, height=200)
Label(root, text = 'Admin', font=('Arial', 15), bg='#ede5dd').place(relx=0.255, rely=0.6)


# Photo for Employee button
employee_logo = ImageTk.PhotoImage(Image.open("images/employee.png").resize((200, 200)))

# Create Employee button
button2 = Button(root,image=employee_logo, borderwidth=5, bg='#cadbc3', command=employee, relief=RIDGE )
button2.place(relx=0.65, rely=0.4, width=200, height=200)
Label(root, text = 'Employee', font=('Arial', 15), bg='#ede5dd').place(relx=0.655, rely=0.6)





# Execute Tkinter
root.mainloop()


