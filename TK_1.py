import subprocess 
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
def Login_Page():
    def Sign_In():
        messagebox.showinfo("Ok","You Can Go Away...")
        p1.destroy()

        Maharat()
    p1=Tk()
    p1.title("Login Page")
    p1.geometry("400x300")
    p1.resizable(False,False)
    p1.config(bg="#099CB9")

    l1=Label(p1,text="User name:")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="Password:")
    l2.place(x=10,y=50)
    e2=Entry(p1,show="•")
    e2.place(x=100,y=50)
    b2=Button(p1,text="Show",command=Showpassword)
    b2.place(x=240,y=50)

    l3=Label(p1,text="My Captcha:")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

    l4=Label(p1,text="Sys Captcha")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)
    b4=Button(p1,text="New")
    b4.place(x=240,y=130)

    b1=Button(p1,text="Sign_In",width=17,command=Sign_In)
    b1.place(x=100,y=170)

    p1.mainloop()


def Maharat():

    def Sign_Out():
        q=messagebox.askyesno("Sign_Out","Are You Sure ?")
        if q==True:
            p1.destroy()
            Login_Page()
    p1=Tk()
    p1.title("Login Page")
    p1.geometry("700x600")
    p1.resizable(False,False)
    p1.config(bg="#D5F439")

    b1=Button(p1,text="Sign_Out",command=Sign_Out)
    b1.place(x=320,y=280)

    p1.mainloop()

Login_Page()

