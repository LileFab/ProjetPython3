#!/usr/bin/python3
# -*- coding: utf-8 -*-
#########################################
#                                       #
# Nom du programme : SOLITAIRE A BILLE  #
#                                       #
# Auteurs : ......... GARBAY / FLEISCH  #
#                                       #
# Création : ........ 12/2022 - 01/2023 #
#                                       #
# Programmé en : ... Python             #
#                                       #
#########################################

## Importation des bibliothèques
import logging
import sys
import tkinter
from tkinter import *
from tkinter import ttk, messagebox

## Fin d'importation des bibliothèques

## Configuration du log
logging.basicConfig(filename='application.log', format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG)
logging.debug("La configuration du logger est terminée")

# Création fenêtre
win = Tk()
logging.debug("La fenetre principale a bien été crée")


## Fonctions et procédures
def endGame():
    ## Quitter le jeu
    reponse = tkinter.messagebox.askyesno("Terminer le jeu",
                                          "Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
    if reponse:
        ## On enregistre les éventuelles modifications
        ## du fichier 'progresion.txt'
        saveFile()
        ## On quitte le programme
        logging.info('Fin du jeu')
        win.quit()


def aboutWindow():
    logging.debug("Création et affichage de la fenêtre d'information")
    global ws, hs
    aboutWin = newWindow(284, 466, "À propos de ...")
    labelAbout = Label(aboutWin, background='white', foreground='black', font=fonte, justify='left')
    txtAbout = 'SOLITAIRE A BILLE\n\n'
    txtAbout = txtAbout + 'Fabien FLEISCH & Pierre GARBAY 12/2022 - 01/2023\n\n'
    txtAbout = txtAbout + 'Jeu programmé en Python\n\n'
    txtAbout = txtAbout + 'Illustrations par Pierre GARBAY.\n\n'
    labelAbout.configure(text=txtAbout)
    labelAbout.grid(row=0, column=0, padx=5, pady=10)
    aboutButtonQuit = ttk.Button(aboutWin, style='BW.TButton', text='Quitter', command=aboutWin.destroy)
    aboutButtonQuit.grid(row=1, column=0, pady=10)
    logging.debug("Fermeture de la fenêtre d'info et remise en place du top level sur la fenetre de jeu")


def HelpWindow():
    logging.debug("Création et affichage de la fenêtre d'aide")
    global ws, hs
    helpWin = newWindow(660, 540, "Aide")
    labelHelp = Label(helpWin, background='white', foreground='black', font=fonte, justify='left')
    txtHelp = 'SOLITAIRE\n\n'
    txtHelp = txtHelp + "BUT DU JEU :\n\n"
    txtHelp = txtHelp + "Débarasser le plateau des billes jusqu'à ce qu'il n'en reste qu'une.\n\n"
    txtHelp = txtHelp + 'COMMENT ? :\n\n'
    txtHelp = txtHelp + "1. Choisir une bille et la faire se déplacer par dessus une autre.\n"
    txtHelp = txtHelp + "2. Le déplacement de bille se fait horizontalement ou verticalement.\n"
    txtHelp = txtHelp + "3. La prise de bille ne peut se faire que sur une case vide se\n"
    txtHelp = txtHelp + "situe immédiatement après la bille par dessus laquelle\n"
    txtHelp = txtHelp + " la bille selectionnée passe.\n"
    txtHelp = txtHelp + '4. La bille à prendre doit être adjacente à la bille preneuse.\n'
    txtHelp = txtHelp + '5. Le joueur peut changer de bille preneuse en cours de partie.\n\n'
    txtHelp = txtHelp + "COMMENT JOUER :\n\n"
    txtHelp = txtHelp + "Le joueur clique avec la souris sur une bille qui devient preneuse.\n"
    txtHelp = txtHelp + "Le joueur clique avec la souris sur une case vide pour prendre une boule.\n"
    txtHelp = txtHelp + "Le clic se fait avec le bouton gauche de la souris.\n\n"
    txtHelp = txtHelp + "LES BOUTONS DE COMMANDES :\n\n"
    txtHelp = txtHelp + "<< : Aller au 1er niveau.\n"
    txtHelp = txtHelp + "< : Aller au niveau précédent.\n"
    txtHelp = txtHelp + "> : Aller au niveau suivant.\n"
    txtHelp = txtHelp + ">> : Aller au dernier niveau.\n"
    txtHelp = txtHelp + "R : Annuler le dernier coup.\n"
    txtHelp = txtHelp + "D : Recharger le niveau actuel.\n"
    txtHelp = txtHelp + "? : Aider.\n"
    txtHelp = txtHelp + "... : À propos de ...\n"
    txtHelp = txtHelp + "X : Quitter."
    labelHelp.configure(text=txtHelp)
    labelHelp.grid(row=0, column=0, padx=5, pady=10)
    helpButtonQuit = ttk.Button(helpWin, style='BW.TButton', text='Quitter', command=helpWin.destroy)
    helpButtonQuit.grid(row=1, column=0, pady=10)
    helpWin.grab_set()
    logging.debug("Fermeture de la fenêtre d'aide et remise en place du top level sur la fenetre de jeu")


def newWindow(height, width, title):
    global ws, hs
    aNew = (ws - width) // 2
    bNew = (hs - height) // 2
    newWin = Toplevel(win)
    newWin.geometry("%dx%d+%d+%d" % (width, height, aNew, bNew))
    newWin.resizable(height=False, width=False)
    newWin.focus()
    newWin.title(title)
    newWin.configure(bg='white')
    return newWin

def reload():
    logging.warning("Le niveau est remis à zéro")
    global posX, posY, formerX, formerY, game, gameInProgress, endedGame
    ## On remet les anciennes positions à -1
    formerX = -1
    formerY = -1
    ## On remet les position à -1
    posX = -1
    posY = -1
    ## On met partie à True et part à False
    gameInProgress = True
    endedGame = False
    ## On relit le niveau
    loadGame()
    ## Et on le réaffiche
    display()


def cancelLastMove():  ## Possible que si partie non finie
    logging.warning("Annulation du dernier coup")
    global posX, posY, formerX, formerY, game, gameInProgress, endedGame
    if gameInProgress == True and endedGame == False:
        ## On change que si il y a eu un coup joué
        if formerX != -1 and formerY != -1:
            if posY == formerY - 2:  # Dernier coup correspond à une montée
                game[posY][posX] = 'V'  # Position actuelle vide
                game[posY + 1][posX] = 'B'  # remise de la boule prise une case en bas
                game[posY + 2][posX] = 'J'  # remise de la boule preneuse 2 cases en bas
            elif posY == formerY + 2:  # Dernier coup correspond à une descente
                game[posY][posX] = 'V'  # Position actuelle vide
                game[posY - 1][posX] = 'B'  # remise de la boule prise une case en haut
                game[posY - 2][posX] = 'J'  # remise de la boule preneuse 2 cases en haut
            elif posX == formerX + 2:  # Dernier coup correspond à déplacement à droite
                game[posY][posX] = 'V'  # Position actuelle vide
                game[posY][posX - 1] = 'B'  # remise de la boule prise une case à gauche
                game[posY][posX - 2] = 'J'  # remise de la boule preneuse 2 cases à gauche
            elif posX == formerX - 2:  # Dernier coup correspond à déplacement à gauche
                game[posY][posX] = 'V'  # Position actuelle vide
                game[posY][posX + 1] = 'B'  # remise de la boule prise une case à droite
                game[posY][posX + 2] = 'J'  # remise de la boule preneuse 2 cases à droite
        logging.debug("Remise en place des ancienne coordonnées de la dernière boule jouée")
        posY = formerY
        posX = formerX
        ## On annule les anciennes coordonées
        formerX = -1
        formerY = -1
        ## On affiche
        display()


def moveLastLevel():
    logging.warning("Avancée au dernier niveau")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    ## On va au dernier niveau (si < maxi)
    if lvl < MAX:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        ## On remet les position à -1
        posX = -1
        posY = -1
        ## on met le niveau au max
        lvl = MAX
        ## On lit le niveau
        loadGame()
        ## On l'affiche
        display()
        ## On permet le jeu
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(lvl))
        SolvedLabel()


def moveNextLevel():
    logging.warning("Avancée au niveau suppérieur")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    ## On va au niveau suivant (si niveau actuel < niveau max)
    if lvl < MAX:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        ## On remet les position à -1
        posX = -1
        posY = -1
        ## On augmente le niveau de 1
        lvl = lvl + 1
        ## On lit le niveau
        loadGame()
        ## On l'affiche
        display()
        ## On permet le jeu
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(lvl))
        SolvedLabel()


def movePreviousLevel():
    logging.warning("Descente d'un niveau")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    ## On va au niveau précédent (si niveau actuel > niveau min)
    if lvl > MIN:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        ## On remet les position à -1
        posX = -1
        posY = -1
        ## On diminue le niveau de 1
        lvl = lvl - 1
        ## On lit le niveau
        loadGame()
        ## On l'affiche
        display()
        ## On permet le jeu
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(lvl))
        SolvedLabel()


def moveFirstLevel():
    logging.warning("Retour au niveau 1")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    ## On va au premier niveau (si pas mini)
    if lvl > MIN:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        ## On remet les position à -1
        posX = -1
        posY = -1
        ## On met le niveau au mini
        lvl = MIN
        ## On lit le niveau
        loadGame()
        ## On l'affiche
        display()
        ## On permet le jeu
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(lvl))
        SolvedLabel()


def loadGame():
    logging.debug("Lecture du fichier de configuration du niveau")
    global lvl, game
    t = "lvl_" + str(lvl) + ".txt"
    file = open(t, 'r')
    game[:] = []
    for ligne in file:
        a = ligne.rstrip('\n\r')
        game.append(list(a))
    file.close()


def display():
    logging.debug("Affichage du niveau")
    global game, posX, posY, lvl, nb
    canv.delete(ALL)
    nb = 0
    y = 0
    x = 0
    while y < 14:
        while x < 14:
            if game[y][x] == 'M':
                canv.create_image(x * 50, y * 50, image=mur, anchor='nw')
            elif game[y][x] == 'V':
                canv.create_image(x * 50, y * 50, image=vide, anchor='nw')
            elif game[y][x] == 'B':
                canv.create_image(x * 50, y * 50, image=boule_noire, anchor='nw')
                nb = nb + 1
            elif game[y][x] == 'J':
                canv.create_image(x * 50, y * 50, image=boule_select, anchor='nw')
                nb = nb + 1
                posX = x
                posY = y
            x = x + 1
        x = 0
        y = y + 1
    ## On vérifie le nombre de boules restantes
    gameCheck(nb)


def gameCheck(n):
    logging.debug("Vérification du niveau d'avancement de la partie")
    global solvedLevels, gameInProgress, endedGame
    if n == 1:
        ## On déclare la partie finie
        gameInProgress = False
        endedGame = True
        ## On marque le niveau comme résolu
        if solvedLevels[lvl - 1] == 'Non':
            solvedLevels[lvl - 1] = 'Oui'
            SolvedLabel()
        ## On informe le joueur qu'il a gagné
        rep = messagebox.showinfo("VICTOIRE !!",
                                  "Vous avez réussi à terminer ce niveau avec succès !!\n\nPensez à essayer un autre niveau...")
        logging.info("La partie à été remportée")
    else:
        isGameBlocked()


def isGameBlocked():
    global nb, game, blockCheck, gameInProgress, endedGame
    logging.debug("Vérification des conditions de blocage")
    bx = 0
    by = 0
    blockCheck = False
    while by < 14:
        while bx < 14:
            if (game[by][bx] == 'B' or game[by][bx] == 'J'):
                ## On vérifie à gauche
                if bx > 1:
                    if game[by][bx - 2] == 'V':
                        if (game[by][bx - 1] == 'B' or game[by][bx - 1] == 'J'):
                            blockCheck = True
                ## On vérifie à droite
                if bx < 12:
                    if game[by][bx + 2] == 'V':
                        if (game[by][bx + 1] == 'B' or game[by][bx + 1] == 'J'):
                            blockCheck = True
                ## On vérifie en haut
                if by > 1:
                    if game[by - 2][bx] == 'V':
                        if (game[by - 1][bx] == 'B' or game[by - 1][bx] == 'J'):
                            blockCheck = True
                ## On vérifie en bas
                if by < 12:
                    if game[by + 2][bx] == 'V':
                        if (game[by + 1][bx] == 'B' or game[by + 1][bx] == 'J'):
                            blockCheck = True
            bx = bx + 1
        bx = 0
        by = by + 1
    ## Si la variable bverif est toujours à False
    ## il n'y a plus de possibilités
    if blockCheck == False:
        ## On bloque la partie
        gameInProgress = False
        endedGame = True
        ## On envoie un messagebox
        logging.warning("La partie est perdue, plus aucun mouvement possible")
        repv = messagebox.showinfo('Plus de possibilité',
                                   "Il n'existe plus de possibilité !\n\nMerci de retenter le niveau ou d'en essayer un autre !!")


def saveFile():
    logging.warning("Enregistrement du fichier de résolution")
    global solvedLevels
    t = ''
    max = len(solvedLevels)
    for i in range(0, max):
        if i == max - 1:
            t = t + solvedLevels[i]
        else:
            t = t + solvedLevels[i] + '\n'
    fich = open('progression.txt', 'w')
    fich.write(t)
    fich.close()
    logging.warning("Si un enregistrement était nécéssaire, il a bien eu lieu")


def readSolvedFile():
    logging.debug("Lecture du fichier de résolution")
    global solvedLevels
    file = open('progression.txt', 'r')
    solvedLevels[:] = []
    for ligne in file:
        a = ligne.rstrip('\n\r')
        solvedLevels.append(a)
    file.close()


def SolvedLabel():
    logging.debug("modification du fichier de résolution")
    global res, lvl, solvedLevels
    res = solvedLevels[lvl - 1]
    if res == 'Non':
        labelSolved.configure(text='Non résolu')
    elif res == 'Oui':
        labelSolved.configure(text='Déjà résolu')


def main(event):
    ## Fonction principale du jeu
    global game, posX, posY, formerX, formerY, gameInProgress, endedGame
    ## On ne vérifie que si partie en cours
    if gameInProgress == True and endedGame == False:
        ## On récupère les coordonnées de la case cliquée
        x = event.x // 50
        y = event.y // 50
        ## On ne vérifie que les actions possibles
        ## Le joueur appuie sur une boule noire
        if game[y][x] == 'B':
            ## On la change en boule rouge (sélectionnée)
            game[y][x] = 'J'
            ## On change l'ancienne boule rouge en noire (si existe)
            if posX != -1 and posY != -1:
                game[posY][posX] = 'B'
            ## On affiche le tout
            display()
            ## On change les coordonées de la boule sélectionnée
            posX = x
            posY = y
        ## Le joueur appuie sur une case vide
        elif game[y][x] == 'V':
            ## On vérifie si nous sommes 2 cases à droite de la boule sélectionnée
            if game[y][x - 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if game[y][x - 1] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    game[posY][posX] = 'V'  # Case vide sur ancienne position
                    game[posY][posX + 1] = 'V'  # Et sur boule sautée
                    game[posY][posX + 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posX = posX + 2
                    ## On affiche le tout
                    display()
            ## On vérifie si nous sommes 2 cases à gauche
            if game[y][x + 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if game[y][x + 1] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    game[posY][posX] = 'V'  # Case vide sur ancienne position
                    game[posY][posX - 1] = 'V'  # Et sur boule sautée
                    game[posY][posX - 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posX = posX - 2
                    ## On affiche le tout
                    display()
            ## On vérifie si nous sommes 2 cases en haut
            if game[y + 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if game[y + 1][x] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    game[posY][posX] = 'V'  # Case vide sur ancienne position
                    game[posY - 1][posX] = 'V'  # Et sur boule sautée
                    game[posY - 2][posX] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posY = posY - 2
                    ## On affiche le tout
                    display()
            ## On vérifie si nous sommes 2 cases en bas
            if game[y - 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if game[y - 1][x] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    game[posY][posX] = 'V'  # Case vide sur ancienne position
                    game[posY + 1][posX] = 'V'  # Et sur boule sautée
                    game[posY + 2][posX] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posY = posY + 2
                    ## On affiche le tout
                    display()


## Fin fonctions et procédures

## Variables et Images
mur = PhotoImage(file='Mur.png')
boule_noire = PhotoImage(file='Boule Noire.png')
boule_select = PhotoImage(file='Boule Sélection.png')
vide = PhotoImage(file='Vide.png')
blockCheck = False
nb = 0
fonte = ('Arial', 11, 'bold')
posX = -1
posY = -1
formerX = -1
formerY = -1
game = []
gameInProgress = True
endedGame = False
MAX = 10
MIN = 1
lvl = 1
res = ''
solvedLevels = []
## Fin variables et images

## Intérieur Fenêtre
win.title('SOLITAIRE')
win.resizable(height=False, width=False)
if sys.platform.startswith('linux'):
    win.iconphoto(True, PhotoImage(file='solitaire.xbm'))
elif sys.platform.startswith('win32'):
    win.iconphoto(True, PhotoImage(file='solitaire.png'))
canv = Canvas(win, height=700, width=700, bg='#E1E101', bd=0, highlightthickness=0)
canv.grid(row=0, column=0, columnspan=2)
canv.create_image(50, 50, image=mur, anchor='nw')
frlabel = Frame(win)
frlabel.grid(row=1, column=0, padx=2)
levelLabel = Label(frlabel, bg='DarkOliveGreen1', fg='#9c6b00', font=fonte, text='Niveau 1', width=13, bd=2,
                   relief=RIDGE)
levelLabel.grid(row=0, column=0)
labelSolved = Label(frlabel, fg='#9c6b00', bg='DarkOliveGreen1', font=fonte, width=13, bd=2, relief=RIDGE)
labelSolved.grid(row=0, column=1, padx=2)
frbutton = Frame(win)
frbutton.grid(row=1, column=1, pady=5)
firstLevelButton = Button(frbutton, text='<<', width=4, font=fonte, command=moveFirstLevel)
firstLevelButton.grid(row=0, column=0)
previousLevelButton = Button(frbutton, text='<', width=4, font=fonte, command=movePreviousLevel)
previousLevelButton.grid(row=0, column=1)
nextLevelButton = Button(frbutton, text='>', width=4, font=fonte, command=moveNextLevel)
nextLevelButton.grid(row=0, column=2)
lastLevelButton = Button(frbutton, text='>>', width=4, font=fonte, command=moveLastLevel)
lastLevelButton.grid(row=0, column=3)
cancelMoveButton = Button(frbutton, text='R', width=4, font=fonte, command=cancelLastMove)
cancelMoveButton.grid(row=0, column=4)
restartButton = Button(frbutton, text='D', width=4, font=fonte, command=reload)
restartButton.grid(row=0, column=5)
helpButton = Button(frbutton, text='?', width=4, font=fonte, command=HelpWindow)
helpButton.grid(row=0, column=6)
aboutButton = Button(frbutton, text='...', width=4, font=fonte, command=aboutWindow)
aboutButton.grid(row=0, column=7)
quitButton = Button(frbutton, text='X', width=4, font=fonte, command=endGame)
quitButton.grid(row=0, column=8)
## Fin Intérieur Fenêtre

## On lit le fichier 'progression.txt' et on affiche le résultat dans le Label
readSolvedFile()
SolvedLabel()
## Fin lecture et écriture de la résolution du niveau

## On lit le fichier du niveau en cours et on l'affiche
loadGame()
display()
## Fin de lecture et affichage du niveau

## Placement de la fenêtre
w = 700
h = 800
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
a = (ws - w) // 2
b = (hs - h) // 2
win.geometry("%dx%d+%d+%d" % (w, h, a, b))
## Fin placement de la fenêtre

## Fonction de fermeture de la fenêtre
win.protocol("WM_DELETE_WINDOW", endGame)
## Fin fonction fermeture de fenêtre

## Liens d'action
canv.bind('<Button-1>', main)
## Fin liens d'action

win.mainloop()
win.destroy()
