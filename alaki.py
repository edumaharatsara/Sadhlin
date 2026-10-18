import subprocess 
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from random import * 
game=["sang","kaghaz","gheich"]
user=0; machine=0

def Create_Code():
    code=randint(1,3)
    if code==1:
        return "sang"
    elif code==2:
        return "kaghaz"
    else:
        return "gheichi"


def Game_Page():

    def Run():
        b1.config(text="Mani")
        gameuser=e1.get()
        if gameuser not in ["sang","kaghaz","gheich"]:
            e1.focus()
            return
        gamemachine=Create_Code()
        e2.delete(0,END)
        e2.insert(0,gamemachine)
        global user,machine
        if gameuser=="sang" and gamemachine=="gheichi" or gameuser=="gheichi" and gamemachine=="kaghaz"  or gameuser=="kaghaz" and gamemachine=="sang":
            user+=1
        if gamemachine=="sang" and gameuser=="gheichi"  or gamemachine=="gheichi" and gameuser=="kaghaz"  or gamemachine=="kaghaz" and gameuser=="sang":
            machine+=1
        data="User="+str(user)+"  ,Machine="+str(machine)
        e3.delete(0,END)
        e3.insert(0,data)
        if user==3 or machine==3:
            b1.config(state="disabled")



    def Load(*args):
        data=c1.get()
        e1.delete(0,END)
        e1.insert(0,data)


    p1=Tk()
    p1.title("Game")
    p1.geometry("500x300")

    l1=Label(p1,text="User:")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="Machine:")
    l2.place(x=10,y=60)
    e2=Entry(p1)
    e2.place(x=100,y=60)



    l3=Label(p1,text="Result:")
    l3.place(x=10,y=110)
    e3=Entry(p1)
    e3.place(x=100,y=110)
    e3.insert(0,"User=0 , Machine=0")

    b1=Button(p1,text="Run Game",command=Run)
    b1.place(x=300,y=10)


    v1=StringVar()
    c1=ttk.Combobox(p1,textvariable=v1)
    c1["values"]=game
    c1.place(x=300,y=60)
    c1.set("Game")
    c1.bind("<<ComboboxSelected>>",Load)



    p1.mainloop()

Game_Page()
