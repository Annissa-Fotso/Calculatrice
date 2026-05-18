from calculator import addition , soustraction , multiplication , division , pourcentage , racine_carree
memoire = 0
historique = []
def afficher_menu ():
    print ("1. Addition") 
    print ("2. Soustraction") 
    print ("3. Multiplication") 
    print ("4. Division") 
    print ("5. Pourcentage")
    print ("6. Racine carree")
    print ("7. Résultat en mémoire" )
    print ("8. Historique")
    print ("9. Quitter")
afficher_menu ()
while True:
    choix = input ("choisissez une opération de 1 à 9 : "  )
    if choix in ["1" , "2" , "3" , "4"]:
        while True:
            try:
                a = float(input("Entrez le premier nombre : "))
                break
            except:
                print ("Entrée invalide, veuillez entrer un nombre")
        while True:
            try:
                 b = float (input ("Entrez le deuxieme nombre : ")) 
                 break
            except:
             print ("Entrée invalide, veuillez entrer un nombre")  
        if choix == "1":
            sum = addition (a , b)
            print ("Le résultat de l'addition est : ", sum )
            memoire = sum 
            historique.append(str(a) +   "+"   + str(b) +   "="   + str(sum))
        elif choix == "2":
            dif = soustraction (a , b)
            print (" Le résultat de la soustraction est : ", dif)
            memoire = dif
            historique.append(str(a) +   "-"   + str(b) +   "="   + str(dif))
        elif choix == "3":
            prod = multiplication (a , b)
            print ("Le résultat de la multiplication est : ", prod)
            memoire = prod
            historique.append(str(a) +   "*"   + str(b) +   "="   + str(prod))
        elif choix == "4":
            if b == 0:
                print ("Erreur, la division par zéro est impossible")
            else :
                quot = division (a , b)
                print ("Le résultat de la division est : ", quot)
                memoire = quot
                historique.append(str(a) +   "/"   + str(b) +   "="   + str(quot))
    elif choix == "5":
        p = float (input("Entrez un nombre: " ))
        résultat = pourcentage ( p ) 
        print ("Le résultat de la division par cent est : ", résultat, "%")
        memoire = résultat
        historique.append(str(p) +   "/"   + str(100) +   "="   + str(résultat))
    elif choix == "6":
        n = float (input("Entrez un nombre "))
        if n < 0:
            print ("Erreur, résulatat des nombres négatifs impossible")
        else :
            résultat = racine_carree (n)
            print (" La racine carrée de votre nombre est : ", résultat )
            memoire = résultat
            historique.append("√" + str(n) +  " = "  +  str(résultat))
    elif choix == "7":
        if memoire == 0:
            print ("Aucun résultat en mémoire")
        else: 
            print ("Le résultat en mémoire est : ", memoire)
    elif choix == "8":
        if len (historique) == 0:
            print ("Historique vide")
        else: 
            print ("Historique des calculs")
            for calcul in historique:
                print (calcul)
    elif choix == "9":
        print ("Aurevoir!")
        break
    else :
        print ("Entrée invalide, veuillez choisir un nombre de 1 à 9 " )

  
