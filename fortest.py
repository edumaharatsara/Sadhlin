import subprocess 
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

fooddic={
    "Pizza"          :[750000,10],
    "Burger"         :[650000,20],
    "Sandwich"       :[450000,10],
    "Special Pizza"  :[950000,10]
}
foodlist=[]
for key in fooddic:
    foodlist.append(key)

def Fast_Food_Page():
    def Mohasebeh():
        foodname=e1.get()
        if foodname=="":
            e1.focus()
            return

        price=float(e2.get())
        if price<10000 or price>5000000:
            e2.focus()
            return

        off=float(e3.get())
        if off<0 or off>100:
            e3.focus()
            return
        
        num=int(e4.get())
        if num<0 or num>20:
            e4.focus()
            return
        h1=price * num 
        h2=h1 * off /100
        h3=h1 -h2

        factor="{0:20s}{1:10.2f}{2:10d}{3:10.1f}{4:10.1f}{5:10.1f}".format(foodname,price,num,h1,h2,h3)+"\n"
        q=messagebox.askyesno("ثبت سفارش","آیا از سفارش این غذا مطمئن هستید ?")
        if q==True:
            t1.insert(END,factor)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            
    def Load(*args):
        key=c1.get()
        values=fooddic[key]

        e1.delete(0,END)
        e1.insert(0,key)

        e2.delete(0,END)
        e2.insert(0,values[0])
        
        e3.delete(0,END)
        e3.insert(0,values[1])

        e4.delete(0,END)
        e4.insert(0,1)
    p1=Tk()
    p1.geometry("900x600")
    p1.title("Fast Food ")
    p1.config(bg="#F4481D")

    l1=Label(p1,text="Foodname")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="Food Price")
    l2.place(x=10,y=50)
    e2=Entry(p1)
    e2.place(x=100,y=50)

    l3=Label(p1,text="Off %")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

    l4=Label(p1,text="Num #")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)

    b1=Button(p1,text="محاسبه فاکتور",command=Mohasebeh)
    b1.place(x=250,y=10)

    t1=Text(p1,width=100,height=30)
    t1.place(x=10,y=170)

    var1=StringVar()
    c1=ttk.Combobox(p1,textvariable=var1)
    c1.place(x=550,y=10)
    c1["values"]=foodlist
    c1.set("Food Name")
    c1.bind("<<ComboboxSelected>>",Load)

    p1.mainloop()
Fast_Food_Page()