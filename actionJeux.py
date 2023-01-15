import logging
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import affichage
import navigation

blockCheck = False
nb = 0
formerX = -1
formerY = -1
game = []
gameInProgress = True
endedGame = False
res = ''
solvedLevels = []
lvl = 1
labelSolved = Label(navigation.frlabel, fg='#9c6b00', bg='DarkOliveGreen1', font=affichage.fonte, width=13, bd=2, relief=RIDGE)
labelSolved.grid(row=0, column=1, padx=2)

def reload():
    logging.warning("Le niveau est remis à zéro")
    global posX, posY, formerX, formerY, game, gameInProgress, endedGame
    ## On remet les anciennes positions à -1
    formerX = -1
    formerY = -1
    posX = -1
    posY = -1
    gameInProgress = True
    endedGame = False
    loadGame()
    affichage.display()

def loadGame():
    logging.debug("Lecture du fichier de configuration du niveau")
    global lvl, game
    t = "levels/lvl_" + str(lvl) + ".txt"
    file = open(t, 'r')
    game[:] = []
    for ligne in file:
        a = ligne.rstrip('\n\r')
        game.append(list(a))
    file.close()



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
        rep = messagebox.showinfo("VICTOIRE !", "Vous avez fini ce plateau")
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

    if blockCheck == False:
        gameInProgress = False
        endedGame = True
        logging.warning("La partie est perdue, plus aucun mouvement possible")
        repv = messagebox.showinfo('Plus de possibilité',
                                   "Retenter le niveau ou bien essayer en un autre")


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