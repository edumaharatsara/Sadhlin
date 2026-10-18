import subprocess 
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
show="off"
from random import * 
def Create_Captcha():
    cap=randint(1000,9999)
    return cap

def Login_Page():
    def Sign_In():
        user=e1.get()
        if user!="matin":
            e1.focus()
            return
        password=e2.get()
        if password!="123":
            e2.focus()
            return
        mycap=e3.get()
        syscap=e4.get()
        if mycap!=syscap:
            New_Captcha()
            e3.delete(0,END)
            e3.focus()
            return
        
        p1.destroy()
        Foroshgah()
        
    def Showpassword():
        global show
        if show=="off":
            show="on"
            e2.config(show="")
            b2.config(text="😁")

        else:
            show="off"
            e2.config(show="•")
            b2.config(text="😒")
    def New_Captcha():
        cap=Create_Captcha()
        e4.delete(0,END)
        e4.insert(0,cap)
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
    b2=Button(p1,text="😒",command=Showpassword)
    b2.place(x=240,y=50)

    l3=Label(p1,text="My Captcha:")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

    l4=Label(p1,text="Sys Captcha")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)
    cap=Create_Captcha()
    e4.insert(0,cap)
    b4=Button(p1,text="New",command=New_Captcha)
    b4.place(x=240,y=130)

    b1=Button(p1,text="Sign_In",width=17,command=Sign_In)
    b1.place(x=100,y=170)

    p1.mainloop()


def Foroshgah():

    def Sign_Out():
        q=messagebox.askyesno("Sign_Out","Are You Sure ?")
        if q==True:
            p1.destroy()
            Login_Page()

    def Calculate():
        
        price=float(e1.get())
        tedad=float(e2.get())
        result=price * tedad
        e3.delete(0,END)
        e3.insert(0,result)

    p1=Tk()
    p1.title("Login Page")
    p1.geometry("700x600")
    p1.resizable(False,False)
    p1.config(bg="#D5F439")

    l1=Label(p1,text="Price:")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)


    l2=Label(p1,text="Num Order")
    l2.place(x=300,y=10)
    e2=Entry(p1)
    e2.place(x=400,y=10)

    l3=Label(p1,text="Calculate")
    l3.place(x=10,y=50)
    e3=Entry(p1)
    e3.place(x=100,y=50)

    b2=Button(p1,text="Calculate",command=Calculate)
    b2.place(x=300,y=50)



    b1=Button(p1,text="Sign_Out",command=Sign_Out)
    b1.place(x=320,y=280)

    p1.mainloop()

# Login_Page()
Foroshgah()

