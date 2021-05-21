from tkinter import *
from main import *
from random import *




#########################################  Fenetre principal #########################################

def lancerjeu():

    # Réinitialisation  
    canvas.delete(ALL)

    # Mise en place du fond d'écran pendant la partie
    canvas.create_image(960, 540, image=fond)
    
    ## Bouton Pause ##
    ButtonPause = Button(tk, image = boutonpause, command = PauseEcran)
    Pause = canvas.create_image(1850, 35, image = boutonpause)
    canvas.create_window(1850, 35, window=ButtonPause)

    # jeu
    collide()
    control()
    gravity()
    draw() 


#########################################  Page d'accueil #########################################

def AcceuilPage():   
    canvas.delete(ALL)
    score = 0
    canvas.create_image(960, 540, image=fond)
    canvas.create_image(500, 850, image=jouer)
    canvas.create_image(1650, 700, image=stuff)
    canvas.create_image(1650, 800, image=instruction)
    canvas.create_image(1650, 900, image=quitter)

    ButtonInstruction = Button(tk, image = instruction, command = Pageinstruction)
    canvas.create_window(1650, 800, window=ButtonInstruction)

    ButtonStuff = Button(tk, image = stuff, command=PageEquipement)
    canvas.create_window(1650, 700, window=ButtonStuff)

    ButtonQuitter = Button(tk, image = quitter, command = tk.destroy)
    canvas.create_window(1650, 900, window=ButtonQuitter)

    ButtonJouer  = Button( tk, image = jouer, command = lancerjeu)
    canvas.create_window(500, 850, window = ButtonJouer)


#########################################  Page de Pause  #########################################

def PauseEcran():
    global gamepause, FondPause,  FondNoir, FondPauseScreen, Quitter, FondContinuerButton, FondPetitQuitter, ButtonPetitQuitter, WindowQuitter, ButtonContinuer, WindowContinuer, ButtonRejouer, WindowRejouer
    gamepause = 1
    FondPause = canvas.create_image(960, 540, image=fond)
    FondNoir = canvas.create_image(960, 540, image=voilenoir)
    FondPauseScreen = canvas.create_image(900, 450, image=pausescreen)
    FondContinuerButton = canvas.create_image(500, 850, image=continuebutton)
    FondPetitQuitter = canvas.create_image(125, 40, image=accueil)
    FondQuitter = canvas.create_image(125, 40, image=accueil)

    ButtonPetitQuitter = Button(tk, image = accueil, command = AcceuilPage)
    WindowQuitter =canvas.create_window(125, 40, window=ButtonPetitQuitter)

    ButtonContinuer = Button(tk, image = continuebutton, command = continuerjeu)
    WindowContinuer =canvas.create_window(500, 850, window=ButtonContinuer)

    ButtonQuitter = Button(tk, image = quitter, command = tk.destroy)
    canvas.create_window(1200, 850, window=ButtonQuitter)


def continuerjeu():
    global FondPause, FondNoir, FondPauseScreen, FondRejouer, FondContinuerButton, FondPetitQuitter, WindowQuitter, ButtonContinuer, WindowContinuer, ButtonRejouer, WindowRejouer
    canvas.delete(FondPause, FondNoir, FondPauseScreen, FondRejouer, FondContinuerButton, FondPetitQuitter, WindowQuitter, WindowContinuer, WindowRejouer)
   
# #######################################################     Instructions    ##############################################

def Pageinstruction():
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=fond)
    canvas.create_image(960, 540, image=voilenoir)
    canvas.create_image(125, 40, image=accueil)
    canvas.create_image(960, 200, image=titreinstruction)  


    ButtonPetitQuitter = Button(tk, image = accueil , command = AcceuilPage)
    canvas.create_window(125, 40, window=ButtonPetitQuitter )

def PageEquipement():
    canvas.delete(ALL)
    canvas.create_image(960, 540, image=fond)
    canvas.create_image(960, 540, image=voilenoir)
    canvas.create_image(125, 40, image=accueil)
    canvas.create_image(900, 200, image=titrestuff)
    canvas.create_image(400, 500, image=cat)
    canvas.create_image(750, 500, image=player2)
    canvas.create_image(1100, 500, image=player3)
    canvas.create_image(1450, 500, image=player6)


    canvas.create_image(400, 700, image=playerName)
    canvas.create_image(750, 700, image=playerName)
    canvas.create_image(1115, 700, image=playerName)
    canvas.create_image(1465, 700, image=playerName)

    


    ## BUTTON ##
    ButtonPetitQuitter = Button(tk, image = accueil,  command = AcceuilPage)
    canvas.create_window(125, 40, window=ButtonPetitQuitter)

