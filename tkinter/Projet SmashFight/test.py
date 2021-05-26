from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb=mysql.connector.connect(
    host="localhost",
    user="projetLogiciel",
    password="hfX5MfGPNO6Q3mD9",
    database="SmashFight"
)
mycursor=mydb.cursor()

# label1=Label(root,text="name",width=20,height=2,).grid(row=0,column=0)
# label2=Label(root,text="score",width=20,height=2).grid(row=1,column=0)

# e1=Entry(root,width=30,borderwidth=8)
# e1.grid(row=0,column=1)
# e2=Entry(root,width=30,borderwidth=8)
# e2.grid(row=1,column=1)

# def Register():
#     name=e1.get()
#     dbname=""
#     Select="select name from users where name='%s'" %(name)
#     mycursor.execute(Select)
#     result=mycursor.fetchall()
#     for i in result:
#         dbname=i[0]
#     if(name == dbname):
#         messagebox.askokcancel("Information","Record Already exists")
#         Update()
#     else:
#         Insert="Insert into users(name,score,) values(%s,%s)"
#         score=e2.get()
        
#         if(score !=""):
#             Value=(name,score)
#             mycursor.execute(Insert,Value)
#             mydb.commit()
#             messagebox.askokcancel("Information","Record inserted")
#             e1.delete(0, END)
#             e2.delete(0, END)
#         else:
#             if (score == ""):
#              messagebox.askokcancel("Information","New Entery Fill All Details")
#             else:
#              messagebox.askokcancel("Information", "Some fields left blank")


# def Update():
#     name=e1.get()
#     score=e2.get()
#     Update="Update users set score='%s' where name='%s'" %(score,name)
#     mycursor.execute(Update)
#     mydb.commit()
#     messagebox.showinfo("Info","Record Update")



# root.mainloop()