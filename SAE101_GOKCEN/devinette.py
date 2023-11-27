from objets import joueur
import random
import time
import getpass

def Devinette(j1:joueur,j2:joueur) :
    """
    Procédure Devinette qui regroupe tout l'algorithme pour le mini-jeu.
    Il prend et modifie les variables j1 et j2 qui sont les deux joueurs.
    La procédure utilise le nom et le mode des joueurs et modifie leur score 
    """

    #variables

    nbre_max:int
    nbre_j1:int
    nbre_j2:int
    limiteh:int
    limiteb:int
    tic:float
    tac:float
    tps1:float
    tps2:float
    nbre_propose:int
    hasard:int
    dif1:float
    dif2:float 

    #présentation
    #règle :
    print("")
    print("Bienvenue dans le mini-jeu Devinette")
    print("")
    time.sleep(1.0)
    print("Vous devez dans ce mini-jeu, dans le but de gagner, deviner le nombre du joueur adverse le plus rapidement.")
    print("")
    time.sleep(2.0)
    print("Le joueur qui aura mis le moins de temps remporte 1 point !")
    print("")
    time.sleep(1.0)
    print("Vous êtes prêt ?")
    print("")
    time.sleep(1.0)
    print("Les deux joueurs qui s'affrontent sont :",j1.nom,"et",j2.nom)
    print("")
    time.sleep(1.0)

    # robot contre robot
    #le temps de réponse en fonction de l'intelligence
    if j1.typo=='Robot' and j2.typo=='Robot' :
        if j1.mode=="Normal":
            dif1=3
        else :
            dif1=1.5
        if j2.mode=="Normal":
            dif2=3
        else :
            dif2=1.5
        # le nombre limite est choisi arbitrairement
        nbre_max=random.randint(100,200) 
        print("Le nombre limite a été choisi :",nbre_max,". Veuillez ne pas dépasser cette limite !")
        print("")
        time.sleep(2.0)
        #choix des nombres
        nbre_j1=random.randint(0,nbre_max)
        nbre_j2=random.randint(0,nbre_max)
        print("Les deux joueur ont choisi leur nombre !")
        print("")
        time.sleep(1.0)
        #joueur 1
        print(j1.nom,"va deviner le nombre de",j2.nom)
        print("")
        time.sleep(2.0)
        nbre_propose=random.randint(0,nbre_max)
        #début chrono
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        #devine le nombre en fonction de l'intelligence
        #si normal :
        if j1.mode=="Normal" :
            while nbre_propose != nbre_j2 :
                print(j1.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j2 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=random.randint(limiteb,limiteh-1) # en effet sinon il risque de se répéter.
                elif nbre_propose<nbre_j2 :
                    print ("Trop petit !")
                    limiteb=nbre_propose
                    nbre_propose=random.randint(limiteb+1,limiteh)  # en effet sinon il risque de se répéter.
                # dépend de l'intelligence du robot
                time.sleep(dif1)
        #si intelligent :
        else :
            while nbre_propose != nbre_j2 :
                print(j1.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j2 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=(limiteb+limiteh)//2 # la moitié de la limite haute et de celle basse.
                elif nbre_propose<nbre_j2 :
                    print ("Trop petit !")
                    #si on choisit le nombre limite comme nombre et donc qu'on obtient de fois de suite le nombre
                    if limiteb==nbre_propose:
                        nbre_propose=nbre_propose+1
                    else :
                    #choi judicieux
                        limiteb=nbre_propose
                        nbre_propose=(limiteb+limiteh)//2  # la moitié de la limite haute et de celle basse.
                # dépend de l'intelligence du robot
                time.sleep(dif1)
        print(j1.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        #fin chrono
        tac=time.time()
        time.sleep(1.0)
        tps1=tac-tic
        print(j1.nom,"a trouvé le nombre en",tps1,"secondes !")
        time.sleep(1.0)
        #joueur 2
        print(j2.nom,"va désormais deviner le nombre de",j1.nom)
        time.sleep(2.0)
        nbre_propose=random.randint(0,nbre_max)
        #début chrono
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        #si normal :
        if j2.mode=="Normal" :
            while nbre_propose != nbre_j1 :
                print(j2.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j1 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=random.randint(limiteb,limiteh-1) # en effet sinon il risque de se répéter.
                elif nbre_propose<nbre_j1 :
                    print ("Trop petit !")
                    limiteb=nbre_propose
                    nbre_propose=random.randint(limiteb+1,limiteh)  # en effet sinon il risque de se répéter.
                # dépend de l'intelligence du robot
                time.sleep(dif2)
        else :
        #si intelligent :
            while nbre_propose != nbre_j1 :
                print(j2.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j1 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=(limiteb+limiteh)//2 # la moitié de la limite haute et de celle basse.
                elif nbre_propose<nbre_j1 :
                    print ("Trop petit !")
                    #si on choisit le nombre limite comme nombre et donc qu'on obtient de fois de suite le nombre
                    if limiteb==nbre_propose:
                        nbre_propose=nbre_propose+1
                    else :
                    #choi judicieux
                        limiteb=nbre_propose
                        nbre_propose=(limiteb+limiteh)//2  # la moitié de la limite haute et de celle basse.
                # dépend de l'intelligence du robot
                time.sleep(dif2)
        print(j2.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        #fin chrono
        tac=time.time()
        time.sleep(1.0)
        tps2=tac-tic
        print(j2.nom,"a trouvé le nombre en",tps2,"secondes !")
        time.sleep(1.0)
        #compare les temps
        if tps2-tps1>5 or tps1-tps2>5 : #si écart > 5 secondes duel écrasant
            print("Le score est écrasant !!")
        else:
           print("La partie a été serrée !!")
        time.sleep(3.0)
        if tps2==tps1:
            print("Il y a égalité, personne ne gagne de point !")
        if tps2>tps1 :
            print(j1.nom,"a été plus rapide de",tps2-tps1,"secondes ! Il gagne donc 1 point !")
            j1.score=j1.score+1 #ajout du point
        if tps2<tps1 :
            print(j2.nom,"a été plus rapide de",tps1-tps2,"secondes ! Il gagne donc 1 point !")
            j2.score=j2.score+1 #ajout du point
        time.sleep(1.0)


        # robot contre joueur

    if j1.typo=='Robot' and j2.typo=='Humain' :
    #intelligence du j1 qui est un robot
        if j1.mode=="Normal":
            dif1=3
        else :
            dif1=1.5
        #choix nombre limite
        print(j2.nom," a l'honneur de choisir le nombre limite :")
        time.sleep(1.0)
        nbre_max=int(input("Veuillez entrer le nombre limite :"))
        time.sleep(1.0)
        print("Le nombre limite a été choisi :",nbre_max)
        #choix du nombre par le joueur robot
        nbre_j1=random.randint(0,nbre_max)
        time.sleep(1.0)
        print(j1.nom,"a choisi son nombre !")
        time.sleep(1.0)
        print(j2.nom,"à votre tour !")
        #choix nombre par le joueur humain
        nbre_j2=int(input("Veuillez entrer votre nombre :"))
        while nbre_j2>nbre_max or nbre_j2<0 :
            nbre_j2=int(input("Erreur ! Veuillez entrer un nombre fonctionel :")) #vérification d'un nombre
        print(j2.nom,"a choisi son nombre !")
        time.sleep(1.0)
        print(j1.nom,"va d'abord deviner le nombre de",j2.nom)
        time.sleep(1.0)
        nbre_propose=random.randint(0,nbre_max)
        #début chrono
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        #trouve le nombre selon l'intelligence
        if j1.mode=="Normal" :
        #si normal :
            while nbre_propose != nbre_j2 :
                print(j1.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j2 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=random.randint(limiteb,limiteh-1) # en effet sinon il risque de se répéter.
                elif nbre_propose<nbre_j2 :
                    print ("Trop petit !")
                    limiteb=nbre_propose
                    nbre_propose=random.randint(limiteb+1,limiteh)  # en effet sinon il risque de se répéter.
                # dépend de l'intelligence du robot
                time.sleep(dif1)
        else :
        #si intelligent :
            while nbre_propose != nbre_j2 :
                print(j1.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j2 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=(limiteb+limiteh)//2 # la moitié de la limite haute et de celle basse.
                elif nbre_propose<nbre_j2 :
                    print ("Trop petit !")
                    #si on choisit le nombre limite comme nombre et donc qu'on obtient de fois de suite le nombre
                    if limiteb==nbre_propose:
                        nbre_propose=nbre_propose+1
                    else :
                    #choi judicieux
                        limiteb=nbre_propose
                        nbre_propose=(limiteb+limiteh)//2  # la moitié de la limite haute et de celle basse.
                # dépend de l'intelligence du robot
                time.sleep(dif1)
        print(j1.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        #fin chrono
        tac=time.time()
        tps1=tac-tic
        print(j1.nom," a trouvé le nombre en",tps1,"secondes !")
        time.sleep(3.0)
        #joueur 2
        print(j2.nom,"va désormais deviner le nombre de",j1.nom)
        time.sleep(3.0)
        #propose des nombres
        print(j2.nom,"propose :")
        nbre_propose=int(input())
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        #tant que pas bon choix, le joueur propose
        while nbre_propose != nbre_j1 :
            print(j2.nom,"propose :",nbre_propose)
            if nbre_propose>nbre_j1 :
                print("Trop grand !")
                print(j2.nom,"propose :")
                nbre_propose=int(input())
            elif nbre_propose<nbre_j1 :
                print ("Trop petit !")
                print(j2.nom,"propose :")
                nbre_propose=int(input())
        print(j2.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        #fin chrono
        tac=time.time()
        tps2=tac-tic
        print(j2.nom,"a trouvé le nombre en",tps2,"secondes !")
        time.sleep(1.0)
        #comparaison des temps
        if tps2-tps1>5 or tps1-tps2>5 :
            print("Le score est écrasant !!")
        else:
           print("La partie a été serrée !!")
        time.sleep(3.0)
        if tps2==tps1:
            print("Il y a égalité, personne ne gagne de point !")
        if tps2>tps1 :
            print(j1.nom,"a été plus rapide de",tps2-tps1,"secondes ! Il gagne donc 1 point !")
            j1.score=j1.score+1
        if tps2<tps1 :
            print(j2.nom,"a été plus rapide de",tps1-tps2,"secondes ! Il gagne donc 1 point !")
            j2.score=j2.score+1
        time.sleep(1.0)

        # joueur vs robot
        # même algorithme que précédemment mais inversement des deux joueurs
    if j2.typo=='Robot' and j1.typo=='Humain' :
        if j2.mode=="Normal":
            dif2=3
        else :
            dif2=1.5
        print(j1.nom," a l'honneur de choisir le nombre limite:")
        time.sleep(1.0)
        nbre_max=int(input("Veuillez entrer le nombre limite "))
        time.sleep(1.0)
        print("Le nombre limite a été choisi :",nbre_max)
        time.sleep(1.0)
        nbre_j2=random.randint(0,nbre_max)
        print(j2.nom,"a choisi son nombre !")
        time.sleep(1.0)
        print(j1.nom,"à votre tour !")
        nbre_j1=int(input("Veuillez entrer votre nombre :"))
        while nbre_j1>nbre_max or nbre_j1<0 :
            nbre_j1=int(input("Erreur ! Veuillez entrer un nombre fonctionel :"))
        print(j1.nom,"a choisi son nombre !")
        time.sleep(1.0)
        print(j2.nom,"va d'abord deviner le nombre de",j1.nom)
        time.sleep(1.0)
        nbre_propose=random.randint(0,nbre_max)
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        if j2.mode=="Normal" :
            while nbre_propose != nbre_j1 :
                print(j2.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j1 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=random.randint(limiteb,limiteh-1) # en effet sinon il risque de se répéter.
                elif nbre_propose<nbre_j1 :
                    print ("Trop petit !")
                    limiteb=nbre_propose
                    nbre_propose=random.randint(limiteb+1,limiteh)  # en effet sinon il risque de se répéter.
                # dépend de l'intelligence du robot
                time.sleep(dif2)
        else :
            while nbre_propose != nbre_j1 :
                print(j2.nom,"propose :",nbre_propose)
                if nbre_propose>nbre_j1 :
                    print("Trop grand !")
                    limiteh=nbre_propose
                    nbre_propose=(limiteb+limiteh)//2 # la moitié de la limite haute et de celle basse.
                elif nbre_propose<nbre_j1 :
                    print ("Trop petit !")
                    #si on choisit le nombre limite comme nombre et donc qu'on obtient de fois de suite le nombre
                    if limiteb==nbre_propose:
                        nbre_propose=nbre_propose+1
                    else :
                    #choi judicieux
                        limiteb=nbre_propose
                        nbre_propose=(limiteb+limiteh)//2  # la moitié de la limite haute et de celle basse.
                # dépend de l'intelligence du robot
                time.sleep(dif2)
        print(j2.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        tac=time.time()
        tps1=tac-tic
        print(j2.nom," a trouvé le nombre en",tps1,"secondes !")
        time.sleep(3.0)

        print(j1.nom,"va désormais deviner le nombre de",j2.nom)
        time.sleep(3.0)
        print(j1.nom,"propose :")
        nbre_propose=int(input())
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        while nbre_propose != nbre_j2 :
            print(j1.nom,"propose :",nbre_propose)
            if nbre_propose>nbre_j2 :
                print("Trop grand !")
                print(j1.nom,"proposez alors :")
                nbre_propose=int(input())
            elif nbre_propose<nbre_j2 :
                print ("Trop petit !")
                print(j1.nom,"propose alors :")
                nbre_propose=int(input())
        print(j1.nom,"propose :",nbre_propose)
        print("C'est gagné !")
        tac=time.time()
        tps2=tac-tic
        print(j1.nom,"a trouvé le nombre en",tps2,"secondes !")
        time.sleep(1.0)

        if tps2-tps1>5 or tps1-tps2>5 :
            print("Le score est écrasant !!")
        else:
           print("La partie a été serrée !!")
        time.sleep(3.0)
        if tps2==tps1:
            print("Il y a égalité, personne ne gagne de point !")
        if tps2>tps1 :
            print(j2.nom,"a été plus rapide de",tps2-tps1,"secondes ! Il gagne donc 1 point !")
            j2.score=j2.score+1
        if tps2<tps1 :
            print(j1.nom,"a été plus rapide de",tps1-tps2,"secondes ! Il gagne donc 1 point !")
            j1.score=j1.score+1
        time.sleep(1.0)

        # joueur vs joueur 
    # choix du joueur qui choisis la limite au hasard
    if j1.typo=='Humain' and j2.typo=='Humain' :
        hasard=random.randint(1,2)
        if hasard==1 :
            print(j1.nom,"a l'honneur de choisir le nombre limite !")
        if hasard==2 :
            print(j2.nom,"a l'honneur de choisir le nombre limite !")
        nbre_max=int(input("Veuillez entrer le nombre limite :"))
        time.sleep(1.0)
        print("Le nombre limite a été choisi :",nbre_max)
        time.sleep(1.0)
        #choix des nombres secrets
        print(j2.nom,"peut indiquer son nombre : (Ne t'inquiète pas, ça reste entre nous !)")
        nbre_j2=int(getpass.getpass("Nombre choisi :")) #getpass pour pas que ça s'affiche
        while nbre_j2>nbre_max or nbre_j2<0 :
            print("Erreur ! Veuillez entrer un nombre fonctionel")
            nbre_j2=int(getpass.getpass("Nombre choisi :"))
        print(j2.nom,"a choisi son nombre !")
        time.sleep(2.0)
        print(j1.nom,"peut indiquer son nombre : (Ne t'inquiète pas, ça reste entre nous !)")
        nbre_j1=int(getpass.getpass("Nombre choisi :")) #getpass pour pas que ça s'affiche
        while nbre_j1>nbre_max or nbre_j1<0 :
            print("Erreur ! Veuillez entrer un nombre fonctionel")
            nbre_j1=int(getpass.getpass("Nombre choisi :"))
        print(j1.nom,"a choisi son nombre !")
        time.sleep(2.0)
        #joueur2 
        print(j2.nom,"va désormais deviner le nombre de",j1.nom)
        time.sleep(2.0)
        print(j2.nom,"commence par proposer :")
        nbre_propose=int(input())
        #début chrono
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        while nbre_propose != nbre_j1 :
            if nbre_propose>nbre_j1 :
                print("Trop grand !")
                print(j2.nom,"propose alors :")
                nbre_propose=int(input())
            elif nbre_propose<nbre_j1 :
                print ("Trop petit !")
                print(j2.nom,"propose alors :")
                nbre_propose=int(input())
        print("C'est gagné !")
        tac=time.time()
        #fin chrono
        tps2=tac-tic #calcul du temps
        print(j2.nom,"a trouvé le nombre en",tps2,"secondes !")
        time.sleep(2.0)
        print(j1.nom,"va désormais deviner le nombre de",j2.nom)
        print(j1.nom,"commence par proposer :")
        nbre_propose=int(input())
        #début chrono
        tic=time.time()
        limiteh=nbre_max
        limiteb=0
        while nbre_propose != nbre_j2 :
            if nbre_propose>nbre_j2 :
                print("Trop grand !")
                print(j1.nom,"propose :")
                nbre_propose=int(input())
            if nbre_propose<nbre_j2 :
                print ("Trop petit !")
                print(j1.nom,"propose :")
                nbre_propose=int(input())
        print("C'est gagné !")
        tac=time.time()
        #fin chrono
        tps1=tac-tic #calcul du temps
        print(j1.nom,"a trouvé le nombre en",tps1,"secondes !")
        time.sleep(2.0)
        # écart de temps
        if tps2-tps1>5 or tps1-tps2>5 : #écart > 5 secondes ou pas
            print("Le score est écrasant !!")
        else:
           print("La partie a été serrée !!")
        time.sleep(3.0)
        # comparaison des temps
        if tps2==tps1:
            print("Il y a égalité, personne ne gagne de point !")
        if tps2>tps1 :
            print(j1.nom,"a été plus rapide de",tps2-tps1,"secondes ! Il gagne donc 1 point !")
            j1.score=j1.score+1 #ajout du point
        if tps2<tps1 :
            print(j2.nom,"a été plus rapide de",tps1-tps2,"secondes ! Il gagne donc 1 point !")
            j2.score=j2.score+1 #ajout du point
        time.sleep(1.0)