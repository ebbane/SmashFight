# On importe Tkinter pour l'interface graphique
from tkinter import *
# from menu import *
import time
from random import *
import keyboard



#######################################################    Principal #########################################################


#On cree une fenêtre et un canevas générale:

tk = Tk()
tk.geometry('1920x1080')
canvas = Canvas(tk,width = 1920, height = 1080 ) # Fenetre principale
canvas.pack(padx=10,pady=10)
gameon = 1


####################################################### Pictures referencies #########################################################

background = PhotoImage(file="background.png") 

# Game
plateformetop = PhotoImage(file="form.png")
sol = PhotoImage(file="floor.png")

# Page d'acceuil
homeBackground = PhotoImage(file="back.png")
play = PhotoImage(file="play.png")
instructions = PhotoImage(file="instructions.png")
quit = PhotoImage(file="quit.png")
equipments = PhotoImage(file="equipments.png")

# Page d'instruction
blackVeil = PhotoImage(file="fondunoir.png")
home = PhotoImage(file="Home.png")

#  Page de pause 
pauseButton = PhotoImage(file="pauseBtn.png")
pause = PhotoImage(file="pause.png")
resume = PhotoImage(file="resume.png")

# Page d'equipements

player4 = PhotoImage(file="player4.png")
player5 = PhotoImage(file="player5.png")
playerName = PhotoImage(file="John.png")
playerName2 = PhotoImage(file="Maurice.png")


#####################################################################################################################################

#########################################  Fenetre principal #########################################

def playGame():

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
    ButtonPause = Button(tk, image = pauseButton, command = pauseScreen)
    Pause = canvas.create_image(1850, 35, image = pauseButton)
    canvas.create_window(1850, 35, window=ButtonPause)

    # jeu
    main()


#########################################  Page d'accueil #########################################

def homePage():   
    canvas.delete(ALL)
    score = 0
    canvas.create_image(960, 540, image=homeBackground)

    ButtonJouer  = Button( tk, bg='green', image =play, command = playGame)
    canvas.create_window(500, 500, window = ButtonJouer)

    ButtonQuitter = Button(tk, bg='#BB0D0D', image = quit, command = tk.destroy)
    canvas.create_window(500, 650, window=ButtonQuitter)

    ButtonStuff = Button(tk, bg='#406F4E',  image = equipments, command=equipmentsScreen)
    canvas.create_window(1500, 500, window=ButtonStuff)

    ButtonInstruction = Button(tk, bg='#406F4E', image = instructions, command = instructionsScreen)
    canvas.create_window(1500, 650, window=ButtonInstruction)
       


#########################################  Page de Pause  #########################################

def pauseScreen():
    canvas.delete(ALL)
    # canvas.delete(ALL)
    # gamepause = 1

    # canvas.create_image(960, 540, image=homeBackground) 
    # canvas.create_image(960, 540, image=blackVeil)
    # canvas.create_image(960, 540, image=pause)


    # homePage = Button(tk, image = home, command = homePage)
    # canvas.create_window(125, 40, window=homePage)

    # resumeButton = Button(tk, image = resume, )
    # canvas.create_window(500, 850, window=resumeButton)

    # quitButton = Button(tk, image = quit, command = tk.destroy)
    # canvas.create_window(1200, 850, window=quitButton)


# def continuerjeu():
#     global FondPause, FondNoir, FondPauseScreen, FondRejouer, FondContinuerButton, FondPetitQuitter, WindowQuitter, ButtonContinuer, WindowContinuer, ButtonRejouer, WindowRejouer
#     canvas.delete(FondPause, FondNoir, FondPauseScreen, FondRejouer, FondContinuerButton, FondPetitQuitter, WindowQuitter, WindowContinuer, WindowRejouer)
   
# #######################################################     Instructions    ##############################################

def instructionsScreen():
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    canvas.create_image(960, 200, image=instructions)  


    ButtonPetitQuitter = Button(tk, image = home , command = homePage)
    canvas.create_window(130, 50, window=ButtonPetitQuitter )

def equipmentsScreen():
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    canvas.create_image(900, 200, image=equipments)
    canvas.create_image(730, 500, image=player5)
    canvas.create_image(1115, 500, image=player4)


    canvas.create_image(730, 700, image=playerName)
    canvas.create_image(1100, 700, image=playerName2)


    ## BUTTON ##
    ButtonPetitQuitter = Button(tk, image = home , command = homePage)
    canvas.create_window(125, 40, window=ButtonPetitQuitter )

# #######################################################     PAge de fin   ##############################################


def GameOverScreen(winner):
    canvas.delete(ALL)
    # Fenetre principale
    canvas.create_image(960, 540, image=background)
    canvas.create_image(960, 540, image=blackVeil)
    #canvas.create_image(900, 450, image=gameover)
    canvas.create_text(960, 450, fill="white", font="Times 150 bold", text="Winner is : " + winner)




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
        self.hp = [PhotoImage(file="hp1.png"), PhotoImage(file="hp2.png"), PhotoImage(file="hp3.png"), PhotoImage(file="hp4.png"), PhotoImage(file="hp5.png"), PhotoImage(file="hp6.png")]
        self.life = 3

player1 = point(0)
player1.x = 50
skin1 = PhotoImage(file="player1.png")
head_player1 = PhotoImage(file="head1.png")
head_player2 = PhotoImage(file="head2.png")
player2 = point(1)
player2.x = 1850
skin2 = PhotoImage(file="player2.png")
redbullet = PhotoImage(file="redbullet.png")
greenbullet = PhotoImage(file="greenbullet.png")

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
    global skin1, skin2, score1, score2, hp_player1, hp_player2, life_player1, life_player2, head_player1, head_player2
    canvas.delete(player1.draw)
    player1.draw = canvas.create_image(player1.x, player1.y, image=skin1)

    canvas.delete(player2.draw)
    player2.draw = canvas.create_image(player2.x, player2.y, image=skin2)

    for i in range(3):
        canvas.delete(life_player1[i])
        canvas.delete(life_player2[i])

    for i in range(player1.life):
        life_player1[i] = canvas.create_image(150+25*i, 150, image=head_player1)
    for i in range(player2.life):
        life_player2[i] = canvas.create_image(600-25*i, 150, image=head_player2)

    canvas.delete(hp_player1)
    hp_player1 = canvas.create_image(150, 100, image=player1.hp[player1.hit])

    canvas.delete(hp_player2)
    hp_player2 = canvas.create_image(500, 100, image=player2.hp[player2.hit])

def main():
    global blackVeil
    if(player1.life == 0):
        GameOverScreen("player2")
    elif(player2.life == 0):
        GameOverScreen("player1")
    else:
        animate()
        collide()
        control()
        gravity()
        draw()
    tk.after(10, main)


homePage()
tk.mainloop()