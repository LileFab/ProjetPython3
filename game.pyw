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
fen = Tk()
logging.debug("La fenetre principale a bien été crée")

## Fonctions et procédures
def quitter_fen():
    ## Quitter le jeu
    reponse = tkinter.messagebox.askyesno("Terminer le jeu",
                                          "Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
    if reponse:
        ## On enregistre les éventuelles modifications
        ## du fichier 'Résolu.txt'
        enregistre_fichier()
        ## On quitte le programme
        logging.info('Fin du jeu')
        fen.quit()


def ap():
    logging.debug("Création et affichage de la fenêtre d'information")
    global ws, hs
    wap = 466
    hap = 284
    aap = (ws - wap) // 2
    bap = (hs - hap) // 2
    fenap = Toplevel(fen)
    fenap.geometry("%dx%d+%d+%d" % (wap, hap, aap, bap))
    fenap.resizable(height=False, width=False)
    fenap.focus()
    fenap.title("À propos de ...")
    fenap.configure(bg='white')
    lbap = Label(fenap, background='white', foreground='black', font=fonte, justify='left')
    txtlbap = 'SOLITAIRE A BILLE\n\n'
    txtlbap = txtlbap + 'Fabien FLEISCH & Pierre GARBAY 12/2022 - 01/2023\n\n'
    txtlbap = txtlbap + 'Jeu programmé en Python\n\n'
    txtlbap = txtlbap + 'Illustrations par Pierre GARBAY.\n\n'
    lbap.configure(text=txtlbap)
    lbap.grid(row=0, column=0, padx=5, pady=10)
    btapquit = ttk.Button(fenap, style='BW.TButton', text='Quitter', command=fenap.destroy)
    btapquit.grid(row=1, column=0, pady=10)
    logging.debug("Fermeture de la fenêtre d'info et remise en place du top level sur la fenetre de jeu")


def aide():
    logging.debug("Création et affichage de la fenêtre d'aide")
    global ws, hs
    waide = 540
    haide = 660
    aaide = (ws - waide) // 2
    baide = (hs - haide) // 2
    fenaide = Toplevel(fen)
    fenaide.geometry("%dx%d+%d+%d" % (waide, haide, aaide, baide))
    fenaide.resizable(height=False, width=False)
    fenaide.focus()
    fenaide.title("Aide")
    fenaide.configure(bg='white')
    lbaide = Label(fenaide, background='white', foreground='black', font=fonte, justify='left')
    txtlbaide = 'SOLITAIRES\n\n'
    txtlbaide = txtlbaide + "BUT DU JEU :\n\n"
    txtlbaide = txtlbaide + "Débarasser le plateau des billes jusqu'à ce qu'il n'en reste qu'une.\n\n"
    txtlbaide = txtlbaide + 'COMMENT ? :\n\n'
    txtlbaide = txtlbaide + "1. Choisir une bille et la faire se déplacer par dessus une autre.\n"
    txtlbaide = txtlbaide + "2. Le déplacement de bille se fait horizontalement ou verticalement.\n"
    txtlbaide = txtlbaide + "3. La prise de bille ne peut se faire que sur une case vide se\n"
    txtlbaide = txtlbaide + "situe immédiatement après la bille par dessus laquelle\n"
    txtlbaide = txtlbaide + " la bille selectionnée passe.\n"
    txtlbaide = txtlbaide + '4. La bille à prendre doit être adjacente à la bille preneuse.\n'
    txtlbaide = txtlbaide + '5. Le joueur peut changer de bille preneuse en cours de partie.\n\n'
    txtlbaide = txtlbaide + "COMMENT JOUER :\n\n"
    txtlbaide = txtlbaide + "Le joueur clique avec la souris sur une bille qui devient preneuse.\n"
    txtlbaide = txtlbaide + "Le joueur clique avec la souris sur une case vide pour prendre une boule.\n"
    txtlbaide = txtlbaide + "Le clic se fait avec le bouton gauche de la souris.\n\n"
    txtlbaide = txtlbaide + "LES BOUTONS DE COMMANDES :\n\n"
    txtlbaide = txtlbaide + "<< : Aller au 1er niveau.\n"
    txtlbaide = txtlbaide + "< : Aller au niveau précédent.\n"
    txtlbaide = txtlbaide + "> : Aller au niveau suivant.\n"
    txtlbaide = txtlbaide + ">> : Aller au dernier niveau.\n"
    txtlbaide = txtlbaide + "R : Annuler le dernier coup.\n"
    txtlbaide = txtlbaide + "D : Recharger le niveau actuel.\n"
    txtlbaide = txtlbaide + "? : Aider.\n"
    txtlbaide = txtlbaide + "... : À propos de ...\n"
    txtlbaide = txtlbaide + "X : Quitter."
    lbaide.configure(text=txtlbaide)
    lbaide.grid(row=0, column=0, padx=5, pady=10)
    btaidequit = ttk.Button(fenaide, style='BW.TButton', text='Quitter', command=fenaide.destroy)
    btaidequit.grid(row=1, column=0, pady=10)
    fenaide.grab_set()
    logging.debug("Fermeture de la fenêtre d'aide et remise en place du top level sur la fenetre de jeu")



def recharge_niveau():
    logging.warning("Le niveau est remis à zéro")
    global posx, posy, ancien_x, ancien_y, jeu, partie, partie_finie
    ## On remet les anciennes positions à -1
    ancien_x = -1
    ancien_y = -1
    ## On remet les position à -1
    posx = -1
    posy = -1
    ## On met partie à True et part à False
    partie = True
    partie_finie = False
    ## On relit le niveau
    lecture_niveau()
    ## Et on le réaffiche
    affichage_niveau()


def retour():## Possible que si partie non finie
    logging.warning("Annulation du dernier coup")
    global posx, posy, ancien_x, ancien_y, jeu, partie, partie_finie
    if partie == True and partie_finie == False:
        ## On change que si il y a eu un coup joué
        if ancien_x != -1 and ancien_y != -1:
            if posy == ancien_y - 2:  # Dernier coup correspond à une montée
                jeu[posy][posx] = 'V'  # Position actuelle vide
                jeu[posy + 1][posx] = 'B'  # remise de la boule prise une case en bas
                jeu[posy + 2][posx] = 'J'  # remise de la boule preneuse 2 cases en bas
            elif posy == ancien_y + 2:  # Dernier coup correspond à une descente
                jeu[posy][posx] = 'V'  # Position actuelle vide
                jeu[posy - 1][posx] = 'B'  # remise de la boule prise une case en haut
                jeu[posy - 2][posx] = 'J'  # remise de la boule preneuse 2 cases en haut
            elif posx == ancien_x + 2:  # Dernier coup correspond à déplacement à droite
                jeu[posy][posx] = 'V'  # Position actuelle vide
                jeu[posy][posx - 1] = 'B'  # remise de la boule prise une case à gauche
                jeu[posy][posx - 2] = 'J'  # remise de la boule preneuse 2 cases à gauche
            elif posx == ancien_x - 2:  # Dernier coup correspond à déplacement à gauche
                jeu[posy][posx] = 'V'  # Position actuelle vide
                jeu[posy][posx + 1] = 'B'  # remise de la boule prise une case à droite
                jeu[posy][posx + 2] = 'J'  # remise de la boule preneuse 2 cases à droite
        logging.debug("Remise en place des ancienne coordonnées de la dernière boule jouée")
        posy = ancien_y
        posx = ancien_x
        ## On annule les anciennes coordonées
        ancien_x = -1
        ancien_y = -1
        ## On affiche
        affichage_niveau()


def dernier_niveau():
    logging.warning("Avancée au dernier niveau")
    global partie, partie_finie, posx, posy, niveau, ancien_x, ancien_y
    ## On va au dernier niveau (si < maxi)
    if niveau < MAX:
        ## On remet les anciennes positions à -1
        ancien_x = -1
        ancien_y = -1
        ## On remet les position à -1
        posx = -1
        posy = -1
        ## on met le niveau au max
        niveau = MAX
        ## On lit le niveau
        lecture_niveau()
        ## On l'affiche
        affichage_niveau()
        ## On permet le jeu
        partie = True
        partie_finie = False
        ## on modifie le label niveau et le label résolu
        lbniveau.configure(text='Niveau : ' + str(niveau))
        change_txt_resolu()


def niveau_plus():
    logging.warning("Avancée au niveau suppérieur")
    global partie, partie_finie, posx, posy, niveau, ancien_x, ancien_y
    ## On va au niveau suivant (si niveau actuel < niveau max)
    if niveau < MAX:
        ## On remet les anciennes positions à -1
        ancien_x = -1
        ancien_y = -1
        ## On remet les position à -1
        posx = -1
        posy = -1
        ## On augmente le niveau de 1
        niveau = niveau + 1
        ## On lit le niveau
        lecture_niveau()
        ## On l'affiche
        affichage_niveau()
        ## On permet le jeu
        partie = True
        partie_finie = False
        ## on modifie le label niveau et le label résolu
        lbniveau.configure(text='Niveau : ' + str(niveau))
        change_txt_resolu()


def niveau_moins():
    logging.warning("Descente d'un niveau")
    global partie, partie_finie, posx, posy, niveau, ancien_x, ancien_y
    ## On va au niveau précédent (si niveau actuel > niveau min)
    if niveau > MIN:
        ## On remet les anciennes positions à -1
        ancien_x = -1
        ancien_y = -1
        ## On remet les position à -1
        posx = -1
        posy = -1
        ## On diminue le niveau de 1
        niveau = niveau - 1
        ## On lit le niveau
        lecture_niveau()
        ## On l'affiche
        affichage_niveau()
        ## On permet le jeu
        partie = True
        partie_finie = False
        ## on modifie le label niveau et le label résolu
        lbniveau.configure(text='Niveau : ' + str(niveau))
        change_txt_resolu()


def premier_niveau():
    logging.warning("Retour au niveau 1")
    global partie, partie_finie, posx, posy, niveau, ancien_x, ancien_y
    ## On va au premier niveau (si pas mini)
    if niveau > MIN:
        ## On remet les anciennes positions à -1
        ancien_x = -1
        ancien_y = -1
        ## On remet les position à -1
        posx = -1
        posy = -1
        ## On met le niveau au mini
        niveau = MIN
        ## On lit le niveau
        lecture_niveau()
        ## On l'affiche
        affichage_niveau()
        ## On permet le jeu
        partie = True
        partie_finie = False
        ## on modifie le label niveau et le label résolu
        lbniveau.configure(text='Niveau : ' + str(niveau))
        change_txt_resolu()


def lecture_niveau():
    logging.debug("Lecture du fichier de configuration du niveau")
    global niveau, jeu
    t = "Niveau " + str(niveau) + ".txt"
    fich = open(t, 'r')
    jeu[:] = []
    for ligne in fich:
        a = ligne.rstrip('\n\r')
        jeu.append(list(a))
    fich.close()


def affichage_niveau():
    logging.debug("Affichage du niveau")
    global jeu, posx, posy, niveau, nbre
    canv.delete(ALL)
    nbre = 0
    y = 0
    x = 0
    while y < 14:
        while x < 14:
            if jeu[y][x] == 'M':
                canv.create_image(x * 50, y * 50, image=mur, anchor='nw')
            elif jeu[y][x] == 'V':
                canv.create_image(x * 50, y * 50, image=vide, anchor='nw')
            elif jeu[y][x] == 'B':
                canv.create_image(x * 50, y * 50, image=boule_noire, anchor='nw')
                nbre = nbre + 1
            elif jeu[y][x] == 'J':
                canv.create_image(x * 50, y * 50, image=boule_select, anchor='nw')
                nbre = nbre + 1
                posx = x
                posy = y
            x = x + 1
        x = 0
        y = y + 1
    ## On vérifie le nombre de boules restantes
    verif_nbre(nbre)


def verif_nbre(n):
    logging.debug("Vérification du niveau d'avancement de la partie")
    global lstresolu, partie, partie_finie
    if n == 1:
        ## On déclare la partie finie
        partie = False
        partie_finie = True
        ## On marque le niveau comme résolu
        if lstresolu[niveau - 1] == 'Non':
            lstresolu[niveau - 1] = 'Oui'
            change_txt_resolu()
        ## On informe le joueur qu'il a gagné
        rep = messagebox.showinfo("VICTOIRE !!",
                                  "Vous avez réussi à terminer ce niveau avec succès !!\n\nPensez à essayer un autre niveau...")
        logging.info("La partie à été remportée")
    else:
        verif_blocage()


def verif_blocage():
    global nbre, jeu, bverif, partie, partie_finie
    logging.debug("Vérification des conditions de blocage")
    bx = 0
    by = 0
    bverif = False
    while by < 14:
        while bx < 14:
            if (jeu[by][bx] == 'B' or jeu[by][bx] == 'J'):
                ## On vérifie à gauche
                if bx > 1:
                    if jeu[by][bx - 2] == 'V':
                        if (jeu[by][bx - 1] == 'B' or jeu[by][bx - 1] == 'J'):
                            bverif = True
                ## On vérifie à droite
                if bx < 12:
                    if jeu[by][bx + 2] == 'V':
                        if (jeu[by][bx + 1] == 'B' or jeu[by][bx + 1] == 'J'):
                            bverif = True
                ## On vérifie en haut
                if by > 1:
                    if jeu[by - 2][bx] == 'V':
                        if (jeu[by - 1][bx] == 'B' or jeu[by - 1][bx] == 'J'):
                            bverif = True
                ## On vérifie en bas
                if by < 12:
                    if jeu[by + 2][bx] == 'V':
                        if (jeu[by + 1][bx] == 'B' or jeu[by + 1][bx] == 'J'):
                            bverif = True
            bx = bx + 1
        bx = 0
        by = by + 1
    ## Si la variable bverif est toujours à False
    ## il n'y a plus de possibilités
    if bverif == False:
        ## On bloque la partie
        partie = False
        partie_finie = True
        ## On envoie un messagebox
        logging.warning("La partie est perdue, plus aucun mouvement possible")
        repv = messagebox.showinfo('Plus de possibilité',
                                   "Il n'existe plus de possibilité !\n\nMerci de retenter le niveau ou d'en essayer un autre !!")


def enregistre_fichier():
    logging.warning("Enregistrement du fichier de résolution")
    global lstresolu
    t = ''
    max = len(lstresolu)
    for i in range(0, max):
        if i == max - 1:
            t = t + lstresolu[i]
        else:
            t = t + lstresolu[i] + '\n'
    fich = open('Résolu.txt', 'w')
    fich.write(t)
    fich.close()
    logging.warning("Si un enregistrement était nécéssaire, il a bien eu lieu")


def lire_fichier_resolu():
    logging.debug("Lecture du fichier de résolution")
    global lstresolu
    fich = open('Résolu.txt', 'r')
    lstresolu[:] = []
    for ligne in fich:
        a = ligne.rstrip('\n\r')
        lstresolu.append(a)
    fich.close()


def change_txt_resolu():
    logging.debug("modification du fichier de résolution")
    global res, niveau, lstresolu
    res = lstresolu[niveau - 1]
    if res == 'Non':
        lbresolu.configure(text='Non résolu')
    elif res == 'Oui':
        lbresolu.configure(text='Déjà résolu')


def fonction_jeu(event):
    ## Fonction principale du jeu
    global jeu, posx, posy, ancien_x, ancien_y, partie, partie_finie
    ## On ne vérifie que si partie en cours
    if partie == True and partie_finie == False:
        ## On récupère les coordonnées de la case cliquée
        x = event.x // 50
        y = event.y // 50
        ## On ne vérifie que les actions possibles
        ## Le joueur appuie sur une boule noire
        if jeu[y][x] == 'B':
            ## On la change en boule rouge (sélectionnée)
            jeu[y][x] = 'J'
            ## On change l'ancienne boule rouge en noire (si existe)
            if posx != -1 and posy != -1:
                jeu[posy][posx] = 'B'
            ## On affiche le tout
            affichage_niveau()
            ## On change les coordonées de la boule sélectionnée
            posx = x
            posy = y
        ## Le joueur appuie sur une case vide
        elif jeu[y][x] == 'V':
            ## On vérifie si nous sommes 2 cases à droite de la boule sélectionnée
            if jeu[y][x - 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if jeu[y][x - 1] == 'B':
                    ## On garde la position précédente
                    ancien_x = posx
                    ancien_y = posy
                    ## On procède au déplacement
                    jeu[posy][posx] = 'V'  # Case vide sur ancienne position
                    jeu[posy][posx + 1] = 'V'  # Et sur boule sautée
                    jeu[posy][posx + 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posx = posx + 2
                    ## On affiche le tout
                    affichage_niveau()
            ## On vérifie si nous sommes 2 cases à gauche
            if jeu[y][x + 2] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if jeu[y][x + 1] == 'B':
                    ## On garde la position précédente
                    ancien_x = posx
                    ancien_y = posy
                    ## On procède au déplacement
                    jeu[posy][posx] = 'V'  # Case vide sur ancienne position
                    jeu[posy][posx - 1] = 'V'  # Et sur boule sautée
                    jeu[posy][posx - 2] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posx = posx - 2
                    ## On affiche le tout
                    affichage_niveau()
            ## On vérifie si nous sommes 2 cases en haut
            if jeu[y + 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if jeu[y + 1][x] == 'B':
                    ## On garde la position précédente
                    ancien_x = posx
                    ancien_y = posy
                    ## On procède au déplacement
                    jeu[posy][posx] = 'V'  # Case vide sur ancienne position
                    jeu[posy - 1][posx] = 'V'  # Et sur boule sautée
                    jeu[posy - 2][posx] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posy = posy - 2
                    ## On affiche le tout
                    affichage_niveau()
            ## On vérifie si nous sommes 2 cases en bas
            if jeu[y - 2][x] == 'J':
                ## On vérifie que la case au milieu est une boule noire
                if jeu[y - 1][x] == 'B':
                    ## On garde la position précédente
                    ancien_x = posx
                    ancien_y = posy
                    ## On procède au déplacement
                    jeu[posy][posx] = 'V'  # Case vide sur ancienne position
                    jeu[posy + 1][posx] = 'V'  # Et sur boule sautée
                    jeu[posy + 2][posx] = 'J'  # Boule sélectionnée
                    ## On modifie les coordonnées de la boule preneuse
                    posy = posy + 2
                    ## On affiche le tout
                    affichage_niveau()


## Fin fonctions et procédures

## Variables et Images
mur = PhotoImage(file='Mur.png')
boule_noire = PhotoImage(file='Boule Noire.png')
boule_select = PhotoImage(file='Boule Sélection.png')
vide = PhotoImage(file='Vide.png')
bverif = False
nbre = 0
fonte = ('Arial', 11, 'bold')
posx = -1
posy = -1
ancien_x = -1
ancien_y = -1
jeu = []
partie = True
partie_finie = False
MAX = 10
MIN = 1
niveau = 1
res = ''
lstresolu = []
## Fin variables et images

## Intérieur Fenêtre
fen.title('SOLITAIRES')
fen.resizable(height=False, width=False)
if sys.platform.startswith('linux'):
    fen.iconphoto(True, PhotoImage(file='solitaire.xbm'))
elif sys.platform.startswith('win32'):
    fen.iconphoto(True, PhotoImage(file='solitaire.png'))
canv = Canvas(fen, height=700, width=700, bg='#E1E101', bd=0, highlightthickness=0)
canv.grid(row=0, column=0, columnspan=2)
canv.create_image(50, 50, image=mur, anchor='nw')
frlabel = Frame(fen)
frlabel.grid(row=1, column=0, padx=2)
lbniveau = Label(frlabel, bg='DarkOliveGreen1', fg='#9c6b00', font=fonte, text='Niveau 1', width=13, bd=2, relief=RIDGE)
lbniveau.grid(row=0, column=0)
lbresolu = Label(frlabel, fg='#9c6b00', bg='DarkOliveGreen1', font=fonte, width=13, bd=2, relief=RIDGE)
lbresolu.grid(row=0, column=1, padx=2)
frbutton = Frame(fen)
frbutton.grid(row=1, column=1, pady=5)
btniv1 = Button(frbutton, text='<<', width=4, font=fonte, command=premier_niveau)
btniv1.grid(row=0, column=0)
btnivprece = Button(frbutton, text='<', width=4, font=fonte, command=niveau_moins)
btnivprece.grid(row=0, column=1)
btnivsuivant = Button(frbutton, text='>', width=4, font=fonte, command=niveau_plus)
btnivsuivant.grid(row=0, column=2)
btnivder = Button(frbutton, text='>>', width=4, font=fonte, command=dernier_niveau)
btnivder.grid(row=0, column=3)
btretour = Button(frbutton, text='R', width=4, font=fonte, command=retour)
btretour.grid(row=0, column=4)
btrecharge = Button(frbutton, text='D', width=4, font=fonte, command=recharge_niveau)
btrecharge.grid(row=0, column=5)
btaide = Button(frbutton, text='?', width=4, font=fonte, command=aide)
btaide.grid(row=0, column=6)
btap = Button(frbutton, text='...', width=4, font=fonte, command=ap)
btap.grid(row=0, column=7)
btquit = Button(frbutton, text='X', width=4, font=fonte, command=quitter_fen)
btquit.grid(row=0, column=8)
## Fin Intérieur Fenêtre

## On lit le fichier 'Résolu.text' et on affiche le résultat dans le Label
lire_fichier_resolu()
change_txt_resolu()
## Fin lecture et écriture de la résolution du niveau

## On lit le fichier du niveau en cours et on l'affiche
lecture_niveau()
affichage_niveau()
## Fin de lecture et affichage du niveau

## Placement de la fenêtre
w = 700
h = 800
ws = fen.winfo_screenwidth()
hs = fen.winfo_screenheight()
a = (ws - w) // 2
b = (hs - h) // 2
fen.geometry("%dx%d+%d+%d" % (w, h, a, b))
## Fin placement de la fenêtre

## Fonction de fermeture de la fenêtre
fen.protocol("WM_DELETE_WINDOW", quitter_fen)
## Fin fonction fermeture de fenêtre

## Liens d'action
canv.bind('<Button-1>', fonction_jeu)
## Fin liens d'action

fen.mainloop()
fen.destroy()
