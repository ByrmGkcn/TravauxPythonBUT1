from objets import joueur
from objets import bcolors
import time
import random

def Transition():
    """
    Procédure permettant de réaliser des transitions
    """
    print((bcolors.OKRED+"►"+bcolors.ENDC+bcolors.OKBLUE+"►"+bcolors.ENDC+bcolors.OKRED+"►"+bcolors.ENDC+" "+bcolors.OKBLUE+"►"+bcolors.ENDC+bcolors.OKRED+"►"+bcolors.ENDC+bcolors.OKBLUE+"►"+bcolors.ENDC+" ")*4+bcolors.OKGREEN)

def constructor(text:str,nbAlumJ1:int,nbAlumJ2:int):
    """
    Procédure permettant de construire les allumettes
    Entrée : Les nombres d'allumettes pour les joueurs 
    """
    niv = ""
    for i in range(0,20):
        if i >= 20-nbAlumJ2:
            niv = niv+bcolors.OKRED+bcolors.BOLD+text+bcolors.OKGREEN
        elif i < nbAlumJ1:
            niv = niv+bcolors.OKRED+bcolors.BOLD+text+bcolors.OKGREEN
        else:
            niv = niv+text
    print(niv)
    
def PrintAllumettes(nbAlumJ1:int,nbAlumJ2:int):
    """
    Procédure permettant d'afficher les allumettes
    Entrée : le nombre d'allumettes
    """
    print()
    constructor("@@@ ",nbAlumJ1,nbAlumJ2)
    constructor("@@@ ",nbAlumJ1,nbAlumJ2)
    constructor("@@@ ",nbAlumJ1,nbAlumJ2)
    constructor("@@@ ",nbAlumJ1,nbAlumJ2)
    constructor("@@@ ",nbAlumJ1,nbAlumJ2)

def TourHumain(nbAlumJ1:int,nbAlumJ2:int) -> int:
    """
    Fonction permettant de donner le choix pour un humain
    Entrée : le nombre d'allumettes
    Sortie : Le choix (un entier)
    """
    choix : int
    
    choix = 0
    
    print()
    Transition()
    print()

    choix = int(input("Combien retirez-vous d'alumettes ? "))
    if choix != 1 and choix != 2 and choix !=3:
        print("Erreur.")
        return(TourHumain(nbAlumJ1,nbAlumJ2))
    else:
        if nbAlumJ1+nbAlumJ2+choix>20:
            choix = 2
            if nbAlumJ1+nbAlumJ2+choix>20:
                choix = 1

    return(choix)

def TourRobot(player:joueur,nbAlumJ1:int,nbAlumJ2:int) -> int:
    """
    Fonction permettant de donner le choix pour un robot
    Entrée : le nombre d'allumettes
    Sortie : Le choix (un entier)
    """
    choix : int

    choix = 0
    
    print()
    Transition()
    
    if player.mode == "Intelligent":
        if 20-(nbAlumJ1+nbAlumJ2) == 3:
            choix = 2
        elif 20-(nbAlumJ1+nbAlumJ2) == 2:
            choix = 1
        elif 20-(nbAlumJ1+nbAlumJ2) == 1:
            choix = 1
        elif 20-(nbAlumJ1+nbAlumJ2) == 4:
            choix = 3
        elif (20-nbAlumJ1+nbAlumJ2-1-3)%4 != 0:
            choix = 3
        elif (20-nbAlumJ1+nbAlumJ2-1-2)%4 != 0:
            choix = 2
        elif (20-nbAlumJ1+nbAlumJ2-1-1)%4 != 0:
            choix = 1
        else:
            choix = random.randint(1,3)
            
    else:
        choix = random.randint(1,3)
    
    print()
    print("Le Robot décide de prendre ",choix," allumette(s) !")
    time.sleep(1.5)
    
    return(choix)

def Allumettes(J1:joueur,J2:joueur):
    """
    Procédure principale
    """
    
    nbAlumJ1 : int
    nbAlumJ2 : int
    
    nbAlumJ1 = 0
    nbAlumJ2 = 0
    
    win = 0

    Transition()
    Transition()

    print()
    print("Bienvenue dans le mini-jeu Allumettes")
    time.sleep(1.0)
    print()
    print("Vous devez dans ce mini-jeu, dans le but de gagner, faire en sorte que votre adversaire récupère la dernière allumette.")
    time.sleep(1.0)
    print()
    print("Vous êtes prêt ?")
    time.sleep(1.0)
    print()
    print("Les deux joueurs qui s'affrontent sont : ",J1.nom," et ",J2.nom)
    time.sleep(1.0)
    print()

    Transition()
    Transition()

    PrintAllumettes(nbAlumJ1,nbAlumJ2)
    
    while nbAlumJ1+nbAlumJ2 < 20:
        
        print()
        print("Tour de ",J1.nom," !")
        
        if J1.typo == "Humain":
            nbAlumJ1 = TourHumain(nbAlumJ1,nbAlumJ2)+nbAlumJ1
        else:
            nbAlumJ1 = TourRobot(J1,nbAlumJ1,nbAlumJ2)+nbAlumJ1
        PrintAllumettes(nbAlumJ1,nbAlumJ2)
        
        if nbAlumJ1+nbAlumJ2 < 20:
            
            print()
            print("Tour de ",J2.nom," !")
            
            if J2.typo == "Humain":
                nbAlumJ2 = TourHumain(nbAlumJ1,nbAlumJ2)+nbAlumJ2
            else:
                nbAlumJ2 = TourRobot(J2,nbAlumJ1,nbAlumJ2)+nbAlumJ2
            PrintAllumettes(nbAlumJ1,nbAlumJ2)
            
            #Verifie la victoire de J2
            if nbAlumJ1+nbAlumJ2 >= 20:
                win = 1
        #Verifie la victoire de J1
        else:
            win = 2
            
    if win == 1:
        print()
        print(J1.nom," gagne ! ",J1.nom," gagne 1 point !")
        J1.score = J1.score+1
        
    elif win == 2:
        print()
        print(J2.nom," gagne ! ",J2.nom," gagne 1 point !")
        J2.score = J2.score+1
    
    Transition()
    Transition()
    Transition()