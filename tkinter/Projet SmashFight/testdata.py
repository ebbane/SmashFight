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

label1=Label(root,text="name",width=20,height=2,).grid(row=0,column=0)
label2=Label(root,text="score",width=20,height=2).grid(row=1,column=0)

e1=Entry(root,width=30,borderwidth=8)
e1.grid(row=0,column=1)
e2=Entry(root,width=30,borderwidth=8)
e2.grid(row=1,column=1)

scorePlayer = 200

def Register():
    name=e1.get(scorePlayer)
    dbname=""
    Select="select name from users where name='%s'" %(name)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbname=i[0]
    if(name == dbname):
        messagebox.askokcancel("Information","Record Already exists")
        Update()
    else:
        Insert="Insert into users(name,score,) values(%s,%s)"
        score= "select score from users where name='%s'" %(name) + scorePlayer
        
        if(score !=""):
            Value=(name,score)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
        else:
            if (score == ""):
             messagebox.askokcancel("Information","New Entery Fill All Details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")


def Update():
    name=e1.get()
    score= "select score from users where name='%s'" %(name) + scorePlayer 
    Update="Update users set score='%s' where name='%s'" %(score,name)
    mycursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Info","Record Update")

def Showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)
        def CreateUI(self):
            tv= Treeview(self)
            tv['columns']=('name', 'score')
            tv.heading('#0',text='name',anchor='center')
            tv.column('#0',anchor='center')
            tv.heading('#1', text='score', anchor='center')
            tv.column('#1', anchor='center')
            tv.grid(sticky=(N,S,W,E))
            self.treeview = tv
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
        def LoadTable(self):
            Select="Select * from users order by score DESC"
            mycursor.execute(Select)
            result=mycursor.fetchall()
            name=""
            score=""
            for i in result:
                name=i[0]
                score=i[1]
                
                self.treeview.insert("",'end',text=name,values=(score))
    root=Tk()
    root.title("Tableaux des résultat")
    A(root)

button1=Button(root,text="Register",width=10,height=2,command=Register).grid(row=7,column=0)
button3=Button(root,text="Update",width=10,height=2,command=Update).grid(row=7,column=3)
button5=Button(root,text="Show All",width=10,height=2,command=Showall).grid(row=7,column=7)
root.mainloop()