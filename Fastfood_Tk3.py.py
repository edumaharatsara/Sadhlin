import subprocess
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from random import *
from module import *
import os

fooddic={}
foodlist=[]

fn="food.txt"
def Get_Data_From_File():
    fp=open(fn,"r") #x  w  a  r
    global fooddic,foodlist
    fooddic={}
    foodlist=[]
    while True:
        x=fp.readline()    # x="pizza,750000,10,"
        if x=="":
            break
        y=x.split(",")   # y[0]="Pizza"  y[1]="750000" y[2]="10"
        foodname=y[0]
        price=float(y[1])
        off=float(y[2])
        fooddic[foodname]=[price,off]
        foodlist.append(foodname)
    fp.close()
Get_Data_From_File()




def fast_food_page():
    def mohasebe():
        foodname=e1.get()
        if foodname=="":
            e1.focus()
            return
        price=float(e2.get())
        if price<1000 or price>5000000:
            e2.focus()
            return
        off=float(e3.get())
        if off <0 or off>100:
            e3.focus()
            return
        num=int(e4.get())
        if num<0 or num>20:
            e4.focus
            return
        h1=price * num
        h2=h1 * off /100
        h3=h1 - h2
        factor="{0:20s}{1:10.2f}{2:10.2f}{3:10.1f}{4:10.1f}{5:10.1f}{6:10.1f}".format(foodname,price,off,num,h1,h2,h3)+"\n"
        q=messagebox.askyesno("ثبت سفارش","ایا از سفارش خود مطمین هستید؟")
        if q==True:
            t1.insert(END,factor)
            e4.delete(0,END)
            e4.delete(0,END)
            e4.delete(0,END)
            e4.delete(0,END)

    def load(*args):
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

    def Add_Food():
        foodname=e1.get()
        if foodname=="" or foodname in foodlist:
            e1.delete(0,END)
            e1.focus()
            return
        price=e2.get()
        price=Set_Float(price,10000,3000000)
        if price==-1:
            e2.focus()
            return
        
        off=e3.get()
        off=Set_Float(off,0,100)
        if off==-1:
            e3.focus()
            return
        fp=open(fn,"a")
        data=foodname+","+str(price)+","+str(off)+","+"\n"
        fp.write(data)
        fp.close()
        Get_Data_From_File()

        c1["values"]=foodlist
        messagebox.showinfo("Ok","Every things are OK... ")
        
    p1=Tk()
    p1.title("game_page")
    p1.geometry("900x600")
    p1.config(bg="#507081")

    l1=Label(p1,text="foodname")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="food price")
    l2.place(x=10,y=50)
    e2=Entry(p1)
    e2.place(x=100,y=50)

    l3=Label(p1,text="off")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

    l4=Label(p1,text="num")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)

    b1=Button(p1,text="calculate",width=17,command=mohasebe)
    b1.place(x=250,y=10)

    t1=Text(p1,width=100,height=30)
    t1.place(x=10,y=170)

    var1=StringVar()
    c1=ttk.Combobox(p1,textvariable=var1)
    c1.place(x=550,y=10)
    c1["values"]=foodlist
    c1.set("food name")
    c1.bind("<<ComboboxSelected>>",load)

    b2=Button(p1,text="Add Food",width=17,command=Add_Food)
    b2.place(x=550,y=50)


    p1.mainloop()

fast_food_page()


