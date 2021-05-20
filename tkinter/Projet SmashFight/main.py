from tkinter import *
import time
from random import *



#######################################################    Principal #########################################################


#On cree une fenêtre et un canevas générale:

tk = Tk()
tk.geometry('1920x1080')
canvas = Canvas(tk,width = 1920, height = 1080 ) # Fenetre principale
canvas.pack(padx=10,pady=10)

# Banques d'iamges

fond = PhotoImage(file="background.png")
canvas.create_image(960, 540, image=fond)

# On crée les plateformes

canvas.create_rectangle(1200,750,1500,725, fill="green")
canvas.create_rectangle(250,750,550,725, fill="green")
canvas.create_rectangle(725,550,1025,525, fill="green")
canvas.create_rectangle(-10,1000,1920,950, fill="blue")

plateformetop = PhotoImage(file="form.png")
canvas.create_image(780,535, image=plateformetop)
canvas.create_image(900,535, image=plateformetop)
canvas.create_image(975,535, image=plateformetop)

canvas.create_image(305,735, image=plateformetop)
canvas.create_image(400,735, image=plateformetop)
canvas.create_image(500,735, image=plateformetop)

canvas.create_image(1255,735, image=plateformetop)
canvas.create_image(1355,735, image=plateformetop)
canvas.create_image(1450,735, image=plateformetop)

sol = PhotoImage(file="floor.png")
canvas.create_image(1575,975, image=sol)
canvas.create_image(925,975, image=sol)
canvas.create_image(275,975, image=sol)

tk.mainloop()