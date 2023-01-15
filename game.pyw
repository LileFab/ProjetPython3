
## Importation des bibliothèques
import logging
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import actionJeux
import affichage
import navigation

## Fin d'importation des bibliothèques

## Configuration du log
logging.basicConfig(filename='application.log', format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG)
logging.debug("La configuration du logger est terminée")

# Création fenêtre
logging.debug("La fenetre principale a bien été crée")


## Fonctions et procédures

canv = affichage.canv
mur = affichage.mur
vide = affichage.vide
boule_noire = affichage.boule_noire
boule_select = affichage.boule_select
win = affichage.win
fonte = affichage.fonte
posX = affichage.posX
posY = affichage.posY

def cancelLastMove():  ## Possible que si partie non finie
  logging.warning("Annulation du dernier coup")
  global posX, posY, formerX, formerY, game, gameInProgress, endedGame
  if actionJeux.gameInProgress == True and actionJeux.endedGame == False:
      ## On change que si il y a eu un coup joué
      if formerX != -1 and formerY != -1:
          if posY == formerY - 2:  # Dernier coup correspond à une montée
              actionJeux.game[posY][posX] = 'V'  # Position actuelle vide
              actionJeux.game[posY + 1][posX] = 'B'  # remise de la boule prise une case en bas
              actionJeux.game[posY + 2][posX] = 'J'  # remise de la boule preneuse 2 cases en bas
          elif posY == formerY + 2:  # Dernier coup correspond à une descente
              actionJeux.game[posY][posX] = 'V'  # Position actuelle vide
              actionJeux.game[posY - 1][posX] = 'B'  # remise de la boule prise une case en haut
              actionJeux.game[posY - 2][posX] = 'J'  # remise de la boule preneuse 2 cases en haut
          elif posX == formerX + 2:  # Dernier coup correspond à déplacement à droite
              actionJeux.game[posY][posX] = 'V'  # Position actuelle vide
              actionJeux.game[posY][posX - 1] = 'B'  # remise de la boule prise une case à gauche
              actionJeux.game[posY][posX - 2] = 'J'  # remise de la boule preneuse 2 cases à gauche
          elif posX == formerX - 2:  # Dernier coup correspond à déplacement à gauche
              actionJeux.game[posY][posX] = 'V'  # Position actuelle vide
              actionJeux.game[posY][posX + 1] = 'B'  # remise de la boule prise une case à droite
              actionJeux.game[posY][posX + 2] = 'J'  # remise de la boule preneuse 2 cases à droite
      logging.debug("Remise en place des ancienne coordonnées de la dernière boule jouée")
      posY = formerY
      posX = formerX
      ## On annule les anciennes coordonées
      formerX = -1
      formerY = -1
      ## On affiche
      affichage.display()

def main(event):
    ## Fonction principale du jeu
    global game, posX, posY, formerX, formerY, gameInProgress, endedGame
    ## On ne vérifie que si partie en cours
    if actionJeux.gameInProgress == True and actionJeux.endedGame == False:
        ## On récupère les coordonnées de la case cliquée
        x = event.x // 50
        y = event.y // 50
        ## On ne vérifie que les actions possibles
        ## Le joueur appuie sur une boule noire
        if actionJeux.game[y][x] == 'B':
            ## On la change en boule rouge (sélectionnée)
            actionJeux.game[y][x] = 'J'
            ## On change l'ancienne boule rouge en noire (si existe)
            if posX != -1 and posY != -1:
                actionJeux.game[posY][posX] = 'B'
            ## On affiche le tout
            affichage.display()
            ## On change les coordonées de la boule sélectionnée
            posX = x
            posY = y
        ## Le joueur appuie sur une case vide
        elif actionJeux.game[y][x] == 'V':
            ## On vérifie si nous sommes 2 cases à droite de la boule sélectionnée
            if actionJeux.game[y][x - 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if actionJeux.game[y][x - 1] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    actionJeux.game[posY][posX] = 'V'  # Case vide sur ancienne position
                    actionJeux.game[posY][posX + 1] = 'V'  # Et sur boule sautée
                    actionJeux.game[posY][posX + 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posX = posX + 2
                    ## On affiche le tout
                    affichage.display()
            ## On vérifie si nous sommes 2 cases à gauche
            if actionJeux.game[y][x + 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if actionJeux.game[y][x + 1] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    actionJeux.game[posY][posX] = 'V'  # Case vide sur ancienne position
                    actionJeux.game[posY][posX - 1] = 'V'  # Et sur boule sautée
                    actionJeux.game[posY][posX - 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posX = posX - 2
                    ## On affiche le tout
                    affichage.display()
            ## On vérifie si nous sommes 2 cases en haut
            if actionJeux.game[y + 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if actionJeux.game[y + 1][x] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    actionJeux.game[posY][posX] = 'V'  # Case vide sur ancienne position
                    actionJeux.game[posY - 1][posX] = 'V'  # Et sur boule sautée
                    actionJeux.game[posY - 2][posX] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posY = posY - 2
                    ## On affiche le tout
                    affichage.display()
            ## On vérifie si nous sommes 2 cases en bas
            if actionJeux.game[y - 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if actionJeux.game[y - 1][x] == 'B':
                    ## On garde la position précédente
                    formerX = posX
                    formerY = posY
                    ## On procède au déplacement
                    actionJeux.game[posY][posX] = 'V'  # Case vide sur ancienne position
                    actionJeux.game[posY + 1][posX] = 'V'  # Et sur boule sautée
                    actionJeux.game[posY + 2][posX] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posY = posY + 2
                    ## On affiche le tout
                    affichage.display()


## Fin fonctions et procédures

## Variables et Images


## Fin variables et images

## Intérieur Fenêtre
win.title('SOLITAIRE')
win.resizable(height=False, width=False)
if sys.platform.startswith('linux'):
    win.iconphoto(True, PhotoImage(file='image/solitaire.xbm'))
elif sys.platform.startswith('win32'):
    win.iconphoto(True, PhotoImage(file='image/solitaire.png'))


frbutton = Frame(win)
frbutton.grid(row=1, column=1, pady=5)
firstLevelButton = Button(frbutton, text='<<', width=4, font=fonte, command=navigation.moveFirstLevel)
firstLevelButton.grid(row=0, column=0)
previousLevelButton = Button(frbutton, text='<', width=4, font=fonte, command=navigation.movePreviousLevel)
previousLevelButton.grid(row=0, column=1)
nextLevelButton = Button(frbutton, text='>', width=4, font=fonte, command=navigation.moveNextLevel)
nextLevelButton.grid(row=0, column=2)
lastLevelButton = Button(frbutton, text='>>', width=4, font=fonte, command=navigation.moveLastLevel)
lastLevelButton.grid(row=0, column=3)
cancelMoveButton = Button(frbutton, text='R', width=4, font=fonte, command=cancelLastMove)
cancelMoveButton.grid(row=0, column=4)
restartButton = Button(frbutton, text='D', width=4, font=fonte, command=actionJeux.reload)
restartButton.grid(row=0, column=5)
helpButton = Button(frbutton, text='?', width=4, font=fonte, command=affichage.HelpWindow)
helpButton.grid(row=0, column=6)
## Fin Intérieur Fenêtre

## On lit le fichier 'progression.txt' et on affiche le résultat dans le Label
actionJeux.readSolvedFile()
actionJeux.SolvedLabel()
## Fin lecture et écriture de la résolution du niveau

## On lit le fichier du niveau en cours et on l'affiche
actionJeux.loadGame()
affichage.display()
## Fin de lecture et affichage du niveau

## Placement de la fenêtre

## Fin placement de la fenêtre

## Liens d'action
canv.bind('<Button-1>', main)
## Fin liens d'action

win.mainloop()
win.destroy()
