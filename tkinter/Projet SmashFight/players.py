from tkinter import * 
from constants import *
import time


# shoot #

class shoot:
    def __init__(self, name):
        self.name = name
        self.x = -10
        self.y = -10
        self.vx = 5

## Gravity ##

class point:
    def __init__(self, name):
        self.name = name
        self.x = 25
        self.y = 775
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0.5
        self.draw = 0
        self.etat = 1
        self.bullet = [shoot(0), shoot(1), shoot(2), shoot(3), shoot(4)]
        self.nb = 0
        self.timer = 0
        self.score = 0
        self.hit = 0
        self.hp = [PhotoImage(file="images/hp1.png"), PhotoImage(file="images/hp2.png"), PhotoImage(file="images/hp3.png"), PhotoImage(file="images/hp4.png"), PhotoImage(file="images/hp5.png"), PhotoImage(file="images/hp6.png")]
        self.life = 3

player1 = point(0)
player1.x = 50

player2 = point(1)
player2.x = 1850


hp_player1 = canvas.create_rectangle(0, 0, 0, 0)
hp_player2 = canvas.create_rectangle(0, 0, 0, 0)
life_player1 = [canvas.create_rectangle(0, 0, 0, 0), canvas.create_rectangle(0, 0, 0, 0), canvas.create_rectangle(0, 0, 0, 0)]
life_player2 = [canvas.create_rectangle(0, 0, 0, 0), canvas.create_rectangle(0, 0, 0, 0), canvas.create_rectangle(0, 0, 0, 0)]


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

# On crée l'espaces tir

class shoot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.vx = 5
        self.draw = canvas.create_oval(0, 0, 0, 0, fill = "white")

player1.bullet[0].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player1.bullet[1].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player1.bullet[2].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player1.bullet[3].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player1.bullet[4].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player2.bullet[0].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player2.bullet[1].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player2.bullet[2].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player2.bullet[3].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")
player2.bullet[4].draw = canvas.create_oval(0, 0, 0, 0, fill = "white")

player1.timer = time.time()

# Score
score1 = canvas.create_text(100, 725, text="0")
score2 = canvas.create_text(1820, 725, text="0")