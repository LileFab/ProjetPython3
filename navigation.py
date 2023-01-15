import logging
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import actionJeux
import affichage

MAX = 10
MIN = 1
frlabel = Frame(affichage.win)
frlabel.grid(row=1, column=0, padx=2)
levelLabel = Label(frlabel, bg='DarkOliveGreen1', fg='#9c6b00', font=affichage.fonte, text='Niveau 1', width=13, bd=2,
                   relief=RIDGE)
levelLabel.grid(row=0, column=0)

def moveLastLevel():
    logging.debug("Avancée au dernier niveau")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    if actionJeux.lvl < MAX:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        posX = -1
        posY = -1
        actionJeux.lvl = MAX
        actionJeux.loadGame()
        affichage.display()
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(actionJeux.lvl))
        actionJeux.SolvedLabel()


def moveNextLevel():
    logging.debug("Avancée au niveau suppérieur")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    if actionJeux.lvl < MAX:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        posX = -1
        posY = -1
        ## On augmente le niveau de 1
        actionJeux.lvl = actionJeux.lvl + 1
        actionJeux.loadGame()
        affichage.display()
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(actionJeux.lvl))
        actionJeux.SolvedLabel()


def movePreviousLevel():
    logging.debug("Descente d'un niveau")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    if actionJeux.lvl > MIN:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        posX = -1
        posY = -1
        ## On diminue le niveau de 1
        actionJeux.lvl = actionJeux.lvl - 1
        actionJeux.loadGame()
        affichage.display()
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(actionJeux.lvl))
        actionJeux.SolvedLabel()


def moveFirstLevel():
    logging.debug("Retour au niveau 1")
    global gameInProgress, endedGame, posX, posY, lvl, formerX, formerY
    if actionJeux.lvl > MIN:
        ## On remet les anciennes positions à -1
        formerX = -1
        formerY = -1
        posX = -1
        posY = -1
        actionJeux.lvl = MIN
        actionJeux.loadGame()
        affichage.display()
        gameInProgress = True
        endedGame = False
        ## on modifie le label niveau et le label résolu
        levelLabel.configure(text='Niveau : ' + str(actionJeux.lvl))
        actionJeux.SolvedLabel()