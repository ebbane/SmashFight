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
    root.title("Hight Scores")
    A(root)

