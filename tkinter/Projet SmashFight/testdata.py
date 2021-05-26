from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
from constants import *


mydb=mysql.connector.connect(
    host="localhost",
    user="projetLogiciel",
    password="hfX5MfGPNO6Q3mD9",
    database="SmashFight"
)
mycursor=mydb.cursor()



def Records(scorePlayer):

    canvas.delete(ALL)

    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)

    canvas.create_image(900, 150, image=winner)

    # p1=Entry(tk,width=100,borderwidth=8)
    # p1.grid(row=0,column=1)



def Register(scorePlayer):
    name=p1.get()
    dbname=""
    Select="select name from users where name='%s'" %(name)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbname=i[0]
    if(name == dbname):
        messagebox.askokcancel("Information","Record Already exists")
        Update(name)
    else:
        Insert="Insert into users(name,score) values('%s','%s')"
        score= "select score from users where name='%s'" %(name) + scorePlayer
        
        if(score !=""):
            Value=(name,score)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Record inserted")
            p1.delete(0, END)
        else:
            if (score == ""):
             messagebox.askokcancel("New Entery Fill All Details")
            else:
             messagebox.askokcancel("Some fields left blank")


def Update(name):
    # name=p1.get()
    score= "select score from users where name='%s'" %(name) + scorePlayer 
    Update="Update users set score='%s' where name='%s'" %(score,name)
    mycursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Score Update")


# tk.mainloop()