from tkinter import * 
import tkinter.messagebox


def try_signIn():
    email = email_entry.get()
    password = password_entry.get()

    if email_entry.get() == "dimas@gmail.com" and password_entry.get() == 123:
        tkinter.messagebox.showinfo("Succes!")
    else:
        tkinter.messagebox.showwarning("Email atau Password Salah!")
        

def SignIn_Page():
    login_screen = Tk()
    login_screen.title("Sign In")
    login_screen.geometry("300x200")
    
    Label(login_screen, text=" ").pack()
    Label(login_screen, text="Email Adress:").pack()
    email_entry = Entry(login_screen, textvariable="Email Address:",width=30, ANCHOR=W)
    email_entry.pack()
    
    Label(login_screen, text=" ").pack()
    Label(login_screen, text="Password:").pack()
    password_entry = Entry(login_screen, textvariable="Password:", show="*")
    password_entry.pack()
    
    Label(login_screen, text=" ").pack()
    Button(login_screen, text="Sign In", width=10, height=1).pack()
    login_screen.mainloop()
SignIn_Page()
