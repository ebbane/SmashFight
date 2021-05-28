from tkinter import *


tk = Tk()
tk.title('Smash Fight')
tk.geometry('1920x1080')
canvas = Canvas(tk,width = 1920, height = 1080 ) # Fenetre principale
canvas.pack(padx=10,pady=10)

####################################################### Pictures referencies #########################################################


background = PhotoImage(file="images/background.png") 

# Game
plateformetop = PhotoImage(file="images/form.png")
sol = PhotoImage(file="images/floor.png")
pauseButton = PhotoImage(file="images/pauseBtn.png")

# Page d'acceuil
homeBackground = PhotoImage(file="images/back.png")
play = PhotoImage(file="images/play.png")
instructions = PhotoImage(file="images/instructions.png")
quit = PhotoImage(file="images/quit.png")
equipments = PhotoImage(file="images/equipments.png")
highScores = PhotoImage(file="images/High Scores.png")

# Page d'instruction
blackVeil = PhotoImage(file="images/fondunoir.png")
home = PhotoImage(file="images/Home.png")
backgroundIstruction = PhotoImage(file="images/instructionBackground.png")

# Page d'equipements
soon = PhotoImage(file="images/soon.png")
back = PhotoImage(file="images/reserve.png")
player4 = PhotoImage(file="images/player4.png")
player5 = PhotoImage(file="images/player5.png")
playerName = PhotoImage(file="images/John.png")
playerName2 = PhotoImage(file="images/Maurice.png")
more = PhotoImage(file="images/more.png")
less = PhotoImage(file="images/less.png")
playerOne = PhotoImage(file="images/playerOne.png")
playerTWo = PhotoImage(file="images/playerTWo.png")
movementSpeed = PhotoImage(file="images/movementSpeed.png")
jumpSpeed = PhotoImage(file="images/jumpSpeed.png")
shootSpeed = PhotoImage(file="images/shootSpeed.png")

# Game over Screen
records = PhotoImage(file="images/Record.png")
winner = PhotoImage(file="images/winner.png")
sentence = PhotoImage(file="images/order.png")
save = PhotoImage(file="images/save.png")
littleQuit = PhotoImage(file="images/littleQuit.png")

# Player 1
skin1 = PhotoImage(file="images/player1.png")
head_player1 = PhotoImage(file="images/head1.png")
head_player2 = PhotoImage(file="images/head2.png")

# Player 2
skin2 = PhotoImage(file="images/player2.png")
redbullet = PhotoImage(file="images/redbullet.png")
greenbullet = PhotoImage(file="images/greenbullet.png")

#####################################################################################################################################