import logging
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import actionJeux

win = Tk()
fonte = ('Arial', 11, 'bold')
mur = PhotoImage(file='image/Mur.png')
boule_noire = PhotoImage(file='image/Boule Noire.png')
boule_select = PhotoImage(file='image/Boule Sélection.png')
vide = PhotoImage(file='image/Vide.png')
canv = Canvas(win, height=700, width=700, bg='#E1E101', bd=0, highlightthickness=0)
canv.grid(row=0, column=0, columnspan=2)
canv.create_image(50, 50, image=mur, anchor='nw')
posX = -1
posY = -1

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
  txtHelp = txtHelp + "D : Recommencer le niveau.\n"
  txtHelp = txtHelp + "? : Aide.\n"
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

def display():
  logging.debug("Affichage du niveau")
  global game, posX, posY, lvl, nb
  canv.delete(ALL)
  nb = 0
  y = 0
  x = 0
  while y < 14:
      while x < 14:
          if actionJeux.game[y][x] == 'M':
              canv.create_image(x * 50, y * 50, image=mur, anchor='nw')
          elif actionJeux.game[y][x] == 'V':
              canv.create_image(x * 50, y * 50, image=vide, anchor='nw')
          elif actionJeux.game[y][x] == 'B':
              canv.create_image(x * 50, y * 50, image=boule_noire, anchor='nw')
              nb = nb + 1
          elif actionJeux.game[y][x] == 'J':
              canv.create_image(x * 50, y * 50, image=boule_select, anchor='nw')
              nb = nb + 1
              posX = x
              posY = y
          x = x + 1
      x = 0
      y = y + 1
  ## On vérifie le nombre de boules restantes
  actionJeux.gameCheck(nb)