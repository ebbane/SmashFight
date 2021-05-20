from tkinter import *
import time
from random import *
import keyboard



#######################################################    Principal #########################################################


#On cree une fenêtre et un canevas générale:

tk = Tk()
tk.geometry('1920x1080')
canvas = Canvas(tk,width = 1920, height = 1080 ) # Fenetre principale
canvas.pack(padx=10,pady=10)

# Banques d'iamges

fond = PhotoImage(file="background.png")
canvas.create_image(960, 540, image=fond)

## Gravity ##

class point:
    def __init__(self, name):
        self.name = name
        self.x = 25
        self.y = 775
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 1
        self.draw = 0
        self.etat = 1


player1 = point(0)
#player1=point()
player2 = point(1)

class box:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.cx = 0
        self.cy = 0
        self.length = 0

plateform = []
plateform.append(box(0))
plateform[0].x = 1200
plateform[0].y = 725
plateform[0].cx = 1500
plateform[0].cy = 750


plateform.append(box(1))
plateform[1].x = 250
plateform[1].y = 725
plateform[1].cx = 550
plateform[1].cy = 750

plateform.append(box(2))
plateform[2].x = 725
plateform[2].y = 525
plateform[2].cx = 1025
plateform[2].cy = 550

# On crée les plateformes
canvas.create_rectangle(1200,750,1500,725, fill="brown")
canvas.create_rectangle(250,750,550,725, fill="brown")
canvas.create_rectangle(725,550,1025,525, fill="brown")
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

def gravity():
    player1.vy += player1.ay
    player1.y += player1.vy

def collide():
    if player1.y >= 935:
        player1.vy = 0
        player1.y = 935
        player1.etat = 1
    
    if(player1.x <= 20):
        player1.x = 20

    if(player1.x >= 1880):
        player1.x = 1880
        
    if player2.y >= 935:
        player2.vy = 0
        player2.y = 935
        player2.etat = 1
    
    if(player2.x <= 20):
        player2.x = 20

    if(player2.x >= 1880):
        player2.x = 1880

    for i in range(len(plateform)):
        if (player1.y + 10>= plateform[i].y and player1.y - 10 <= plateform[i].cy and player1.x + 10 >= plateform[i].x and player1.x - 10 <= plateform[i].cx):
            player1.vy = 0
            player1.y = plateform[i].y-10
            player1.etat = 1

        if (player2.y + 10>= plateform[i].y and player2.y - 10 <= plateform[i].cy and player2.x + 10 >= plateform[i].x and player2.x - 10 <= plateform[i].cx):
            player2.vy = 0
            player2.y = plateform[i].y-10
            player2.etat = 1
        

def control():
    if(player1.etat == 1):
        if (keyboard.is_pressed("space") or keyboard.is_pressed("up")):
            player1.vy = -23
            player1.etat = 0
    if keyboard.is_pressed("right"):
        player1.x += 5
    if keyboard.is_pressed("left"):
        player1.x -= 5

    if(player2.etat == 1):
        if (keyboard.is_pressed("z")):
            player2.vy = -23
            player2.etat = 0
    if keyboard.is_pressed("d"):
        player2.x += 5
    if keyboard.is_pressed("q"):
        player2.x -= 5

def draw():
    canvas.delete(player1.draw)
    player1.draw = canvas.create_rectangle(player1.x-10, player1.y-10, player1.x+10, player1.y+10 ,fill = "red")

    canvas.delete(player2.draw)
    player2.draw = canvas.create_rectangle(player2.x-10, player2.y-10, player2.x+10, player2.y+10 ,fill = "blue")

def main():
    collide()
    control()
    gravity()
    draw()
    tk.after(5, main)

main()
tk.mainloop()