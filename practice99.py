import subprocess 
subprocess.call("cls",shell=True)
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from random import * 
turn="human"
gamestate=[]
gamex=[]
gameo=[]
def Game():
    def click(i, b):
        global turn
        if turn=="human":
            gamestate.append(i)
            if i==0:
                b1.config(text="X",state="disabled")
            elif i==1:
                b2.config(text="X",state="disabled")
            elif i==2:
                b3.config(text="X",state="disabled")
            elif i==3:
                b4.config(text="X",state="disabled")
            elif i==4:
                b5.config(text="X",state="disabled")
            elif i==5:
                b6.config(text="X",state="disabled")
            elif i==6:
                b7.config(text="X",state="disabled")
            elif i==7:
                b8.config(text="X",state="disabled")
            else:
                b9.config(text="X",state="disabled")
            turn="machine"


        else:
            while True:
                i=randint(0,8)
                if i not in gamestate:
                    break
            gamestate.append(i)
            if i==0:
                b1.config(text="O",state="disabled")
            elif i==1:
                b2.config(text="O",state="disabled")
            elif i==2:
                b3.config(text="O",state="disabled")
            elif i==3:
                b4.config(text="O",state="disabled")
            elif i==4:
                b5.config(text="O",state="disabled")
            elif i==5:
                b6.config(text="O",state="disabled")
            elif i==6:
                b7.config(text="O",state="disabled")
            elif i==7:
                b8.config(text="O",state="disabled")
            else:
                b9.config(text="O",state="disabled")
            turn="human"
        #Check For Win or lose Game 




    p1 = Tk()
    p1.title("X O Game - vs Machine")
    p1.resizable(False, False)
    p1.config(bg="#01a2ad")
    p1.geometry("500x500")    

    b1=Button(p1,width=5,height=3)
    b1.place(x=120,y=120)

    b2=Button(p1,width=5,height=3)
    b2.place(x=170,y=120)

    b3=Button(p1,width=5,height=3)
    b3.place(x=220,y=120)

    b4=Button(p1,width=5,height=3)
    b4.place(x=120,y=180)

    b5=Button(p1,width=5,height=3)
    b5.place(x=170,y=180)

    b6=Button(p1,width=5,height=3)
    b6.place(x=220,y=180)


    b7=Button(p1,width=5,height=3)
    b7.place(x=120,y=240)

    b8=Button(p1,width=5,height=3)
    b8.place(x=170,y=240)

    b9=Button(p1,width=5,height=3)
    b9.place(x=220,y=240)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    for i, b in enumerate(buttons):
        b.config(command=lambda i=i, b=b: click(i, b))    

    p1.mainloop()
Game()
