from objets import joueur
from objets import bcolors
import allumettes
import morpion
import devinette

def Transition():
    """
    procédure permettant de créer une transition
    Elle ne possède rien en entrée ni en sortie
    """
    print((bcolors.OKRED+"►"+bcolors.ENDC+bcolors.OKBLUE+"►"+bcolors.ENDC+bcolors.OKRED+"►"+bcolors.ENDC+" "+bcolors.OKBLUE+"►"+bcolors.ENDC+bcolors.OKRED+"►"+bcolors.ENDC+bcolors.OKBLUE+"►"+bcolors.ENDC+" ")*4+bcolors.OKGREEN)
    
def AfficherJoueurs(listJ:list[joueur]):
    """
    Procédure permettant d'afficher la liste des joueurs
    Entrée : liste des joueurs
    """
    i : int
    
    Transition()
    print("Liste des joueurs :")
    
    if len(listJ) > 0:
    
        for i in range(0,len(listJ)):
            if listJ[i].typo == "Robot":
                print(listJ[i].nom," - ",listJ[i].typo," - ",listJ[i].mode)
            else:
                print(listJ[i].nom," - ",listJ[i].typo)
    else:
        print("Aucun joueur d'enregistré.")
    
def AjoutJoueur(listJ:list[joueur]):
    """
    Procédure permettant d'ajouter un joueur
    Entrée : la liste des joueurs
    """
    
    le_joueur : joueur
    choix : int
    
    le_joueur = joueur()
    choix = 0
    
    Transition()
    print()
        
    listJ.append(le_joueur)
    listJ[-1].nom = str(input("Saisir nom du joueur : "+bcolors.OKYELLOW))
    
    listJ[-1].score = 0
    
    while choix != 1 and choix != 2:
        print()
        print(bcolors.LightMagenta+"1 - ",bcolors.OKGREEN,"Le joueur est un Humain")
        print(bcolors.LightMagenta+"2 - ",bcolors.OKGREEN,"Le joueur est un Robot")
        
        choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
        
        if choix == 1:
            listJ[-1].typo = "Humain"
        elif choix == 2:
            listJ[-1].typo = "Robot"
        else:
            print(bcolors.OKRED,"Erreur.")
    
    if listJ[-1].typo == "Humain":
        listJ[-1].mode = "Normal"
    else:
        choix = 0
        while choix != 1 and choix != 2:
            print(bcolors.LightMagenta,"1 - ",bcolors.OKGREEN,"Le Robot est basique")
            print(bcolors.LightMagenta,"2 - ",bcolors.OKGREEN,"Le Robot est intelligent")
            
            choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
            
            if choix == 1:
                listJ[-1].mode = "Normal"
            elif choix == 2:
                listJ[-1].mode = "Intelligent"
            else:
                print(bcolors.OKRED+"Erreur.")
    print()
    print(bcolors.OKGREEN+"Le joueur ",listJ[-1].nom," de type ",listJ[-1].typo," a bien été rajouté !")
    
    if listJ[-1].typo == "Robot" and listJ[-1].mode == "Intelligent":
        print("Le robot est particulièrement intelligent.")
    elif listJ[-1].typo == "Robot" and listJ[-1].mode == "Normal":
        print("Le robot est assez basique.")
        
def Recherche(nom:str,listJ:list[joueur]) -> int:
    """
    Fonction permettant de rechercher un joueur
    Entrée : la liste des joueurs
    Sortie:le numéro du joueur
    """
    pos : int
    i : int
    
    pos = -1

    for i in range (0,len(listJ)):
        if listJ[i].nom == nom:
            pos = i
          
    return(pos)
        
def SuppJoueur(listJ:list[joueur]):
    """
    Procédure permettant de supprimer un joueur
    Entrée : la liste des joueurs
    """
    
    Transition()

    nom = str(input("Saisir le nom du joueur à supprimer : "+bcolors.OKYELLOW))
    
    pos = Recherche(nom,listJ)
    
    if pos < 0 :
        print("Joueur introuvable !")
    else:
        print(listJ[pos].nom," est supprimé !")
        listJ.remove(listJ[pos])

def MenuProfil(listJ:list[joueur]):
    """
    Procédure  permettant d'afficher le menu de profil
    Entrée : la liste des joueurs
    """
    choix : int
    choix = 0
    
    while choix != 4:
        
        Transition()
        print()
        print("Paramètre Profil :")
        print()
        print(bcolors.LightMagenta,"1 - ",bcolors.OKGREEN,"Liste Joueur")
        print(bcolors.LightMagenta,"2 - ",bcolors.OKGREEN,"Retirer Joueur")
        print(bcolors.LightMagenta,"3 - ",bcolors.OKGREEN,"Ajouter Joueur")
        print(bcolors.LightMagenta,"4 - ",bcolors.OKGREEN,"Retour")
        print()
        
        choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
        
        print()
        
        if choix == 1:
            AfficherJoueurs(listJ)
            
        elif choix == 2:
            SuppJoueur(listJ)
            
        elif choix == 3:
            print()
            AjoutJoueur(listJ)
            
        elif choix == 4:
            print("Retour au menu principal !")
            
        else:
            print(bcolors.OKRED+"Erreur.")

def ChoixJoueur(listJ:list[joueur],choix:int):
    """
    Procédure permettant de choisir les joueurs qui vont jouer
    Entrée : La liste des joueurs et le choix du jeu
    """
    choix1 : int
    choix2 : int
    i : int
    choix1 = 0
    choix2 = 0
        
    while choix1 != len(listJ)+1  and choix2 != len(listJ)+1:
        Transition()
        print()
        print("Joueurs :")
        print()
        for i in range(0,len(listJ)):
            print(bcolors.LightMagenta,i+1,bcolors.OKGREEN," - ",listJ[i].nom)
        print(bcolors.LightMagenta,len(listJ)+1,bcolors.OKGREEN," -  Retour")
        print()
        
        choix1 = int(input("Choisissez J1 : "+bcolors.OKYELLOW))
        
        if choix1 != len(listJ)+1:
            choix2 = int(input(bcolors.OKGREEN+"Choisissez J2 : "+bcolors.OKYELLOW))
            
            if choix2 != len(listJ)+1:
                if choix1 == choix2:
                    print(bcolors.OKRED+"Erreur.")
                else:
                    if choix == 1:
                        allumettes.Allumettes(listJ[choix1-1],listJ[choix2-1])
                    elif choix == 2:
                        morpion.Morpion(listJ[choix1-1],listJ[choix2-1])
                    elif choix == 3:
                        devinette.Devinette(listJ[choix1-1],listJ[choix2-1])
                print()

def MenuJeux(listJ:list[joueur]):
    """
    Procédure  permettant d'afficher le menu de jeux
    Entrée : la liste des joueurs
    """
    choix : int
    choix = 0
    
    while choix != 4:
        
        Transition()
        
        print()
        print("Mini-jeux :")
        print()
        print(bcolors.LightMagenta,"1 - ",bcolors.OKGREEN,"Allumettes")
        print(bcolors.LightMagenta,"2 - ",bcolors.OKGREEN,"Morpion")
        print(bcolors.LightMagenta,"3 - ",bcolors.OKGREEN,"Devinette")
        print(bcolors.LightMagenta,"4 - ",bcolors.OKGREEN,"Retour")
        print()
        
        choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
        
        print()
        
        if choix == 1:
            ChoixJoueur(listJ,choix)
            
        elif choix == 2:
            ChoixJoueur(listJ,choix)
            
        elif choix == 3:
            ChoixJoueur(listJ,choix)
            
        elif choix == 4:
            print("Retour au menu principal !")
            
        else:
            print(bcolors.OKRED+"Erreur.")
    
def AfficherScore(listJ:list[joueur]):
    """
    Procédure permettant d'afficher le score
    Entrée : La liste des joueurs
    """
    i : int
    
    Transition()
    
    if len(listJ) == 0:
        print()
        print("Veuillez ajouter des joueurs.")
        print()
    else:
        print("Liste des joueurs :")
        
        for i in range(0,len(listJ)):
            if listJ[i].typo == "Robot":
                print(listJ[i].score," - ",listJ[i].nom," - ",listJ[i].typo," - ",listJ[i].mode)
            else:
                print(listJ[i].score," - ",listJ[i].nom," - ",listJ[i].typo)
            
def ModifScore(listJ:list[joueur]):
    """
    Procédure permettant de modifier le score d'un joueur
    Entrée: la liste des joueurs
    """
    choix1 : int
    choix2 : int
    i : int
    
    choix1 = 0
    choix2 = 0
        
    while choix1 != len(listJ)+1  :
        
        Transition()
        print()
        print("Joueurs :")
        print()
        for i in range(0,len(listJ)):
            print(i+1," - ",listJ[i].nom)
        print(len(listJ)+1," -  Retour")
        print()
        
        choix1 = int(input("Saisissez un joueur à qui modifier son score : "+bcolors.OKYELLOW))
        
        if choix1 != len(listJ)+1 and choix1 <= len(listJ) and choix1 > 0:
            choix2 = 0
            
            while choix2 != 3 :
                Transition()
                print()
                print(bcolors.LightMagenta,"1 - ",bcolors.OKGREEN,"Augmenter")
                print(bcolors.LightMagenta,"2 - ",bcolors.OKGREEN,"Réduire")
                print(bcolors.LightMagenta,"3 - ",bcolors.OKGREEN,"Retour")
                print()
                
                choix2 = int(input("Voulez-vous augmenter ou réduire son score ? : "+bcolors.OKYELLOW))
                if choix2 == 1:
                    listJ[choix1-1].score = listJ[choix1-1].score+int(input(bcolors.OKGREEN+"Saisissez une valeur : "+bcolors.OKYELLOW))
                elif choix2 == 2:
                    listJ[choix1-1].score = listJ[choix1-1].score-int(input(bcolors.OKGREEN+"Saisissez une valeur : "+bcolors.OKYELLOW))
                elif choix == 3:
                    print(bcolors.OKGREEN+"Retour au menu principal !")
                else:
                    print(bcolors.OKRED+"Erreur.")
            
def MenuScore(listJ:list[joueur]):
    """
    Procédure  permettant d'afficher le menu de score
    Entrée : la liste des joueurs
    """
    choix : int
    choix = 0
    
    while choix != 3:
        
        Transition()
        print()
        print("Score :")
        print()
        print(bcolors.LightMagenta,"1 - ",bcolors.OKGREEN,"Afficher Score")
        print(bcolors.LightMagenta,"2 - ",bcolors.OKGREEN,"Score Option")
        print(bcolors.LightMagenta,"3 - ",bcolors.OKGREEN,"Retour")
        print()
        
        choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
        
        print()
        
        if choix == 1:
            AfficherScore(listJ)
            
        elif choix == 2:
            ModifScore(listJ)

        elif choix == 3:
            print("Retour au menu principal !")
            
        else:
            print(bcolors.OKRED+"Erreur.")
            
def ChargementJoueurs(listJ:list[joueur]):
    """
    Procédure permettant de charger les joueurs
    Entrée : la liste des joueurs
    """

    choix : int
    mot1 : str
    mot2 : int
    mot3 : str
    mot4 : str

    profiles = open("profiles.txt", "r")

    info = profiles.read()

    mot = ""
    mot1 = ""
    mot2 = 0
    mot3 = ""
    mot4 = ""

    for i in range(0,len(info)):
        if info[-i] == ";":
            choix = 0
            for j in range(len(info)-i+1):
                if info[len(info)-i-j] == ",":

                    choix = choix+1

                    if choix == 1:
                        mot = mot[0:-1]
                        mot1 = mot

                    if choix == 2:
                        mot2 = int(mot)

                    if choix == 3:
                        mot3 = mot

                    if choix == 4:
                        mot4 = mot

                    mot = ""
                else:
                    mot = info[len(info)-i-j]+mot

            AjoutJoueurChargement(listJ,mot1,mot2,mot3,mot4)

    profiles.close()

def AjoutJoueurChargement(listJ:list[joueur],mot1:str,mot2:int,mot3:str,mot4:str):
    """
    Procédure permettant d'ajouter un joueur à la liste
    Entrée : la liste des joueurs et tous ses arguments sous formes de mot
    """
    le_joueur : joueur
    le_joueur = joueur()

    listJ.append(le_joueur)

    listJ[-1].nom = mot1
    listJ[-1].score = mot2
    listJ[-1].typo = mot3
    listJ[-1].mode = mot4

def SauvegardeJoueurs(listJ:list[joueur]):
    """
    Procédure permettant de sauvegarder les joueurs
    Entrée : Liste des joueurs
    """

    profiles = open("profiles.txt", "w")

    for i in range(len(listJ)):
        profiles.write(",")
        profiles.write(listJ[-i].mode)
        profiles.write(",")
        profiles.write(listJ[-i].typo)
        profiles.write(",")
        profiles.write(str(listJ[-i].score))
        profiles.write(",")
        profiles.write(listJ[-i].nom)
        profiles.write(";\n")

    profiles.close()

if __name__ == "__main__" :

    choix : int
    listJ : list[joueur]
    
    choix = 0
    listJ = []

    ChargementJoueurs(listJ)
    
    Transition()
    print()
    print("Bienvenue !")
    print()
    
    while choix != 4:
        Transition()
        print()
        print(bcolors.LightMagenta,"1 -",bcolors.OKGREEN,"Paramètre profil")
        print(bcolors.LightMagenta,"2 -",bcolors.OKGREEN,"Mini-jeux")
        print(bcolors.LightMagenta,"3 -",bcolors.OKGREEN,"Score")
        print(bcolors.LightMagenta,"4 -",bcolors.OKGREEN,"Quitter")
        print()
        
        choix = int(input("Choisissez une option : "+bcolors.OKYELLOW))
        
        if choix == 1:
            MenuProfil(listJ)
            
        elif choix == 2:
            MenuJeux(listJ)
            
        elif choix == 3:
            MenuScore(listJ)
            
        elif choix == 4:
            Transition()
            print()
            print("Au revoir !")
            print()
            Transition()
            
            SauvegardeJoueurs(listJ)

        else:
            print(bcolors.OKRED+"Erreur.")