from objets import joueur
from objets import bcolors
import random

def PrintMorpion(tab:list[list[str]]):
    """
    Procédure permettant d'afficher le morpion
    Entrée : le morpion (sous forme de matrice)
    """

    tabtemp : list[list[str]]
    tabtemp = [["-","-","-"],["-","-","-"],["-","-","-"]]

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "X":
                tabtemp[i][j] = bcolors.OKRED+bcolors.BOLD+tab[i][j]+bcolors.ENDC
            elif tab[i][j] == "O":
                tabtemp[i][j] = bcolors.OKBLUE+bcolors.BOLD+tab[i][j]+bcolors.ENDC

    print(bcolors.ENDC)
    print(" ",tabtemp[0][0]," ║ ",tabtemp[0][1]," ║ ",tabtemp[0][2])
    print("═════╬═════╬═════")
    print(" ",tabtemp[1][0]," ║ ",tabtemp[1][1]," ║ ",tabtemp[1][2])
    print("═════╬═════╬═════")
    print(" ",tabtemp[2][0]," ║ ",tabtemp[2][1]," ║ ",tabtemp[2][2])
    print()

def TourHumain(tab:list[list[str]],Jnb:str) :
    """
    Procédure permettant de savoir quel pion a choisit l'humain
    Entrée : Le morpion
    """

    choixX : int
    choixY : int
    tabtemp : list[list[str]]
    
    choixX = 0
    choixY = 0
    tabtemp = [["-","-","-"],["-","-","-"],["-","-","-"]]

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabtemp[i][j] = tab[i][j]

    #Saisie Position X du symbole.
    while choixX != 1 and choixX != 2 and choixX !=3:
        print()
        choixX = int(input("Indiquez la position de la case sur l'axe X : "))
        if choixX != 1 and choixX != 2 and choixX !=3:
            print("Erreur.")

    #Saisie Position Y du symbole.
    while choixY != 1 and choixY != 2 and choixY !=3:
        print()
        choixY = int(input("Indiquez la position de la case sur l'axe Y : "))
        if choixY != 1 and choixY != 2 and choixY !=3:
            print("Erreur.")

    print("La position de la case est de X : ",choixX,", Y : ",choixY)

    #Marquage du symbole dans le tableau.
    if tab[choixY-1][choixX-1] == "X" or tab[choixY-1][choixX-1] == "O":
        print("Erreur. La case est déjà marqué par un symbole !")
        tabtemp = TourHumain(tab,Jnb)
    else:
        if Jnb == "J1" :
            tabtemp[choixY-1][choixX-1] = "X"
        elif Jnb == "J2" :
            tabtemp[choixY-1][choixX-1] = "O"
        
    return(tabtemp)

def TourRobot(tab:list[list[str]],Jnb:str,player:joueur,tour:int):
    """
    Procédure permettant de savoir quel pion a choisit le robot
    Entrée : Le morpion, le joueur, le tour
    """

    choixX : int
    choixY : int
    tabtemp : list[list[str]]
    
    choixX = 0
    choixY = 0
    tabtemp = [["-","-","-"],["-","-","-"],["-","-","-"]]

    #Affecte les valeurs du morpion à celle du morpion temporaire
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabtemp[i][j] = tab[i][j]

    if player.mode == "Intelligent":

        if tour == 1 and tab[1][1] == "-":
            choixX = 2
            choixY = 2

        elif tour == 2 and tab[1][1] != "-":
            choixX = random.choice([1,3])
            choixY = random.choice([1,3])
        else:
            for i in range(0,len(tab)):
                #Vérifie les lignes
                if tab[i][0] == tab[i][1] and tab[i][2] == "-":
                    choixX = 3
                    choixY = i+1
                elif tab[i][2] == tab[i][1] and tab[i][0] == "-":
                    choixX = 1
                    choixY = i+1
                elif tab[i][2] == tab[i][0] and tab[i][1] == "-":
                    choixX = 2
                    choixY = i+1
                #Vérifie les colonnes
                elif tab[0][i] == tab[1][i] and tab[2][i] == "-":
                    choixX = i+1
                    choixY = 3
                elif tab[2][i] == tab[1][i] and tab[0][i] == "-":
                    choixX = i+1
                    choixY = 1
                elif tab[2][i] == tab[0][i] and tab[1][i] == "-":
                    choixX = i+1
                    choixY = 2

            if choixX == 0 and choixY == 0:
                #Diagonale d'en haut à gauche de en bas à droite
                if tab[0][0] == tab[1][1] and tab[2][2] == "-":
                    choixX = 2
                    choixY = 2
                elif tab[2][2] == tab[1][1] and tab[0][0] == "-":
                    choixX = 0
                    choixY = 0
                elif tab[2][2] == tab[0][0] and tab[1][1] == "-":
                    choixX = 1
                    choixY = 1
                #Diagonale d'en haut à droite de en bas à gauche
                elif tab[0][2] == tab[1][1] and tab[2][0] == "-":
                    choixX = 0
                    choixY = 2
                elif tab[2][0] == tab[1][1] and tab[0][2] == "-":
                    choixX = 2
                    choixY = 0
                elif tab[2][0] == tab[0][2] and tab[1][1] == "-":
                    choixX = 1
                    choixY = 1
                else:
                    choixX = random.randint(1,3)
                    choixY = random.randint(1,3)

    elif player.mode == "Normal":
        #Saisie Position X du symbole.
        choixX = random.randint(1,3)

        #Saisie Position Y du symbole.
        choixY = random.randint(1,3)

    #Marquage du symbole dans le tableau.
    if tab[choixY-1][choixX-1] == "X" or tab[choixY-1][choixX-1] == "O":
        tabtemp = TourRobot(tab,Jnb,player,tour)
    else:
        if Jnb == "J1" :
            tabtemp[choixY-1][choixX-1] = "X"
        elif Jnb == "J2" :
            tabtemp[choixY-1][choixX-1] = "O"

    return(tabtemp)

def VerifWin(tab:list[list[str]]):
    """
    Procédure permettant de savoir si la partie est gagnée ou pas
    Entrée : le morpion
    """

    #Vérifie les lignes
    for i in range(0,len(tab)):
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] == "X" and tab[i][1] == "X" and tab[i][2] == "X":
            return(1)
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] == "O" and tab[i][1] == "O" and tab[i][2] == "O":
            return(2)

    #Vérifie les colonnes
    for i in range(0,len(tab)):
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] == "X" and tab[1][i] == "X" and tab[2][i] == "X":
            return(1)
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] == "O" and tab[1][i] == "O" and tab[2][i] == "O":
            return(2)

    #Vérifie les diagonales
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] == "X" and tab[1][1] == "X" and tab[2][2] == "X":
        return(1)
    if tab[2][0] == tab[1][1] == tab[0][2] and tab[2][0] == "X" and tab[1][1] == "X" and tab[0][2] == "X":
        return(1)
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] == "O" and tab[1][1] == "O" and tab[2][2] == "O":
        return(2)
    if tab[2][0] == tab[1][1] == tab[0][2] and tab[2][0] == "O" and tab[1][1] == "O" and tab[0][2] == "O":
        return(2)

    if tab[0][0] != "-" and tab[0][1] != "-"  and tab[0][2] != "-"  and tab[1][0] != "-"  and tab[1][1] != "-"  and tab[1][2] != "-"  and tab[2][0] != "-"  and tab[2][1] != "-"  and tab[2][2] != "-" :
        return(3)

    return(0)

def Morpion(J1:joueur,J2:joueur):
    """
    Procédure principale du morpion
    Entrée : les deux joueurs
    """

    tab : list[list[str]]
    win : int
    tour : int

    tab = [["-","-","-"],["-","-","-"],["-","-","-"]]
    win = 0
    tour = 0

    PrintMorpion(tab)

    while win != 1 and win != 2 and win != 3:
        print()
        print("Tour de ",J1.nom," !")

        tour = tour + 1
        print("tour : ",tour)
        
        if J1.typo == "Humain":
            tab = TourHumain(tab,"J1")
        else:
            tab = TourRobot(tab,"J1",J1,tour)

        PrintMorpion(tab)

        win = VerifWin(tab)

        if win == 0:

            print()
            print("Tour de ",J2.nom," !")

            tour = tour + 1
            print("tour : ",tour)

            if J2.typo == "Humain":
                tab = TourHumain(tab,"J2")
            else:
                tab = TourRobot(tab,"J2",J2,tour)

            PrintMorpion(tab)

            win = VerifWin(tab)

    if win == 1:
        print()
        print(J1.nom," gagne ! ",J1.nom," gagne 1 point !")
        J1.score = J1.score+1
    elif win == 2:
        print()
        print(J1.nom," gagne ! ",J1.nom," gagne 1 point !")
        J1.score = J1.score+1
    elif win == 3:
        print()
        print("Egalité ! Personne ne gagne de points.")
