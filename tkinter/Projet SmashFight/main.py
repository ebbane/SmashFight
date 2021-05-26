from tkinter import *
import time
import os
from random import *
import keyboard
from highScores import *
from constants import *
import numpy as np


stop = 1
timer = 0
begin = time.time()
fin = time.time()


mydb=mysql.connector.connect(
    host="localhost",
    user="projetLogiciel",
    password="hfX5MfGPNO6Q3mD9",
    database="SmashFight"
)
cursor=mydb.cursor()

def PlayGame():
    global begin
    begin = time.time()
    # Réinitialisation  
    canvas.delete(ALL)

    # Mise en place du fond d'écran pendant la partie
    canvas.create_image(960, 540, image=background)
    canvas.create_rectangle(1200,750,1500,725, fill="brown")
    canvas.create_rectangle(250,750,550,725, fill="brown")
    canvas.create_rectangle(725,550,1025,525, fill="brown")
    canvas.create_rectangle(-10,1000,1920,950, fill="blue")


    canvas.create_image(780,535, image=plateformetop)
    canvas.create_image(900,535, image=plateformetop)
    canvas.create_image(975,535, image=plateformetop)

    canvas.create_image(305,735, image=plateformetop)
    canvas.create_image(400,735, image=plateformetop)
    canvas.create_image(500,735, image=plateformetop)

    canvas.create_image(1255,735, image=plateformetop)
    canvas.create_image(1355,735, image=plateformetop)
    canvas.create_image(1450,735, image=plateformetop)

    # Floor 
    canvas.create_image(1575,975, image=sol)
    canvas.create_image(925,975, image=sol)

    ## Bouton Pause ##
    pauseBtn = Button(tk, image = pauseButton, command = PauseScreen)
    canvas.create_window(1850, 35, window=pauseBtn)

    # jeu
    main()


#########################################  Page d'accueil #########################################

def HomePage():
    player1.life = 3
    player2.life = 3
    player1.hit = 0
    player2.hit = 0
    player1.x = 25
    player2.x = 1875
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=homeBackground)

    ButtonJouer  = Button( tk, bg='green', image =play, command = PlayGame)
    canvas.create_window(500, 500, window = ButtonJouer)

    ButtonQuitter = Button(tk, bg='#BB0D0D', image = quit, command = tk.destroy)
    canvas.create_window(500, 650, window=ButtonQuitter)

    ButtonStuff = Button(tk, bg='#406F4E',  image = equipments, command=EquipmentsScreen)
    canvas.create_window(1500, 400, window=ButtonStuff)

    ButtonInstruction = Button(tk, bg='#406F4E', image = instructions, command = InstructionsScreen)
    canvas.create_window(1500, 550, window=ButtonInstruction)

    ButtonInstruction = Button(tk, bg='#07079A', image = highScores, command = Showall)
    canvas.create_window(1500, 700, window=ButtonInstruction)
       


#########################################  Page de Pause  #########################################

def PauseScreen():
    global stop
    stop *= -1

   
# #######################################################     Instructions    ##############################################

def InstructionsScreen():
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    canvas.create_image(960, 200, image=instructions)  

    HomeButton = Button(tk, image = home , command = HomePage)
    canvas.create_window(150, 60, window=HomeButton )

# #######################################################     Equipments    ##############################################

def EquipmentsScreen():

    canvas.delete(ALL)
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    canvas.create_image(900, 200, image=equipments)
    canvas.create_image(730, 500, image=player4)
    canvas.create_image(1115, 500, image=player5)

    canvas.create_image(700, 700, image=playerName)
    canvas.create_image(1150, 700, image=playerName2)


    ## BUTTON ##
    HomeButton = Button(tk, image = home , command = HomePage)
    canvas.create_window(150, 60, window=HomeButton )


def sigmoid(x):
    return(1/(1+np.exp(-0.1*x)))

# #######################################################     Page de fin   ##############################################


def GameOver (winner):
    global begin, fin
    canvas.delete(ALL)

    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    canvas.create_text(960, 250, fill="white", font="Times 100 bold", text="Winner is : " + winner)
    canvas.create_text(960, 400, fill="white", font="Times 50 bold", text="Score : " + str(((player1.life-1)*5+5-player1.hit+(player2.life-1)*5+5-player2.hit)*2*int(10*sigmoid(fin-begin))/10))
    
    ButtonQuitter = Button(tk, bg='#BB0D0D', image = quit, command = tk.destroy)
    canvas.create_window(500, 650, window=ButtonQuitter)

    ButtonRegister = Button(tk, bg='#07079A', image = records, command = Records)
    canvas.create_window(1350, 650, window=ButtonRegister)

    tk.button()


def Records():

    canvas.delete(ALL)
    name = StringVar()
    HomeButton = Button(tk, image = home , command = HomePage)
    canvas.create_window(150, 60, window=HomeButton )

    score = ((player1.life-1)*5+5-player1.hit+(player2.life-1)*5+5-player2.hit)*2*int(10*sigmoid(time.time()-begin))/10
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)

    canvas.create_image(900, 200, image=sentence)

    winnerName = Entry(tk, font="Times 50", textvariable=name)
    canvas.create_window(900, 400, window=winnerName)

    ButtonSave = Button(tk, bg='#07079A', image = save, command=lambda : Register(winnerName.get(), score))
    canvas.create_window(900, 550, window=ButtonSave)

    ButtonQuit = Button(tk, bg='#BB0D0D', image = littleQuit, command=tk.destroy)
    canvas.create_window(900, 850, window=ButtonQuit)

    ButtonScores = Button(tk, bg='green', image = highScores, command = Showall)
    canvas.create_window(900, 700, window=ButtonScores)



def Register(winnerName, scorePlayer):
    name=winnerName
    print(name)
    score = scorePlayer
    print(score)
    dbname=""
    Select="select name from users where name='%s'" %(name)
    print(Select)
    cursor.execute(Select)
    result=cursor.fetchall()
    for i in result:
        dbname=i[0]
    if(name == dbname):
        messagebox.askokcancel("Information","Record Already exists. We will do an update")
        Update(name)
    else:    
        Insert="Insert into users(name,score) values('%s','%s')" %(name,score)
        cursor.execute(Insert)
        mydb.commit()
        messagebox.showinfo("Information","Saved ! ")
        
      

def Update(name):

    scorePlayer = ((player1.life-1)*5+5-player1.hit+(player2.life-1)*5+5-player2.hit)*2*int(10*sigmoid(time.time()-begin))/10
    score= "select score from users where name='%s'" %(name)
    cursor.execute(score)
    scoreBefore = cursor.fetchone()

    scoreFinal = int(scoreBefore[0]) + int(scorePlayer) 
   
    Update="Update users set score='%s' where name='%s'" %(scoreFinal,name)
    cursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Information","Score Update")

    

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


def gravity():
    player1.vy += player1.ay
    player1.y += player1.vy
    player2.vy += player2.ay
    player2.y += player2.vy

def animate():
    global greenbullet, redbullet
    for i in range(5):
        player1.bullet[i].x += player1.bullet[i].vx
        player2.bullet[i].x -= player2.bullet[i].vx

        canvas.delete(player1.bullet[i].draw)
        player1.bullet[i].draw = canvas.create_image(player1.bullet[i].x, player1.bullet[i].y,image=redbullet)

        canvas.delete(player2.bullet[i].draw)
        player2.bullet[i].draw = canvas.create_image(player2.bullet[i].x, player2.bullet[i].y,image=greenbullet)


def collide():
    if player1.y >= 880:
        player1.vy = 0
        player1.y = 880
        player1.etat = 1
    
    if(player1.x <= 20):
        player1.x = 20

    if(player1.x >= 1880):
        player1.x = 1880
        
    if player2.y >= 880:
        player2.vy = 0
        player2.y = 880
        player2.etat = 1
    
    if(player2.x <= 20):
        player2.x = 20

    if(player2.x >= 1880):
        player2.x = 1880

    for i in range(len(plateform)):
        if (player1.y + 65>= plateform[i].y and player1.y + 65  <= plateform[i].cy and player1.x + 10 >= plateform[i].x and player1.x - 10 <= plateform[i].cx):
            player1.vy = 0
            player1.y = plateform[i].y-65
            player1.etat = 1

        if (player2.y + 65>= plateform[i].y and player2.y + 65 <= plateform[i].cy and player2.x + 10 >= plateform[i].x and player2.x - 10 <= plateform[i].cx):
            player2.vy = 0
            player2.y = plateform[i].y-65
            player2.etat = 1

    for i in range(5):
        if(player1.bullet[i].x-8 <= player2.x+45 and player1.bullet[i].x+8 >= player2.x-45 and player1.bullet[i].y-8 <= player2.y+67 and player1.bullet[i].y+8 >= player2.y-67):
            player2.hit += 1
            if(player2.hit == 5):
                player2.hit = 0
                player2.life -= 1
                if(player2.life == 0):
                    pass
            player1.bullet[i].x = 0
            player1.bullet[i].y = -10
        if(player2.bullet[i].x-8 <= player1.x+45 and player2.bullet[i].x+8 >= player1.x-45 and player2.bullet[i].y-8 <= player1.y+67 and player2.bullet[i].y+8 >= player1.y-67):
            player1.hit += 1
            if(player1.hit == 5):
                player1.hit = 0
                player1.life -= 1
                if(player1.life == 0):
                    pass
            player2.bullet[i].x = 0
            player2.bullet[i].y = -10       

def control():

    if(player1.etat == 1):
        if (keyboard.is_pressed("z")):
            player1.vy = -15
            player1.etat = 0
    if keyboard.is_pressed("d"):
        player1.x += 5
    if keyboard.is_pressed("q"):
        player1.x -= 5
    if keyboard.is_pressed("s"):
        player1.y += 25
    if (keyboard.is_pressed("space")) and (time.time()-player1.timer >= 0.35):
        player1.bullet[player1.nb].y = player1.y
        player1.bullet[player1.nb].x = player1.x
        player1.nb += 1
        player1.timer = time.time()
        if(player1.nb == 5):
            player1.nb = 0


    if(player2.etat == 1):
        if keyboard.is_pressed("up"):
            player2.vy = -15
            player2.etat = 0
    if keyboard.is_pressed("right"):
        player2.x += 5
    if keyboard.is_pressed("left"):
        player2.x -= 5
    if keyboard.is_pressed("down"):
        player2.y += 25
    if (keyboard.is_pressed("enter")) and (time.time()-player2.timer >= 0.35):
        player2.bullet[player2.nb].y = player2.y
        player2.bullet[player2.nb].x = player2.x
        player2.nb += 1
        player2.timer = time.time()
        if(player2.nb == 5):
            player2.nb = 0
     

def draw():
    global skin1, skin2, score1, score2, hp_player1, hp_player2, life_player1, life_player2, head_player1, head_player2, timer, fin
    canvas.delete(player1.draw)
    player1.draw = canvas.create_image(player1.x, player1.y, image=skin1)

    canvas.delete(player2.draw)
    player2.draw = canvas.create_image(player2.x, player2.y, image=skin2)

    for i in range(3):
        canvas.delete(life_player1[i])
        canvas.delete(life_player2[i])

    for i in range(player1.life):
        life_player1[i] = canvas.create_image(45+25*i, 150, image=head_player1)
    for i in range(player2.life):
        life_player2[i] = canvas.create_image(1855-25*i, 150, image=head_player2)

    canvas.delete(hp_player1)
    hp_player1 = canvas.create_image(150, 100, image=player1.hp[player1.hit])

    canvas.delete(hp_player2)
    hp_player2 = canvas.create_image(1750, 100, image=player2.hp[player2.hit])

    canvas.delete(timer)
    timer = canvas.create_text(960, 100, font="Times, 50", text=str(int(time.time()-begin)), fill="white")
    fin = time.time()

def main():
    global blackVeil, stop
    if(player1.life == 0):
        GameOver("player2")
    elif(player2.life == 0):
        GameOver("player1")
    else:
        if(stop == 1):
            animate()
            gravity()
            collide()
            control()
            draw()
    tk.after(10, main)

HomePage()
tk.mainloop()