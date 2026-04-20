from calculator import addition , soustraction , multiplication , division
def afficher_menu ():
    print ("1. Addition")
    print ("2. Soustraction")
    print ("3. Multiplication")
    print ("4. Division")
afficher_menu ()
choix = input ("choisissez une opération, (1 , 2 , 3 ou 4): ")
a = float (input ("Entrez le premier nombre : "))
b = float (input ("Entrez le deuxieme nombre : ")) 
if choix == "1":
  sum = addition (a , b)
  print ("Le résultat de l'addition est : ", sum ) 
if choix == "2":
 dif = soustraction (a , b)
 print (" Le résultat de la soustraction est : ", dif)
if choix == "3":
  prod = multiplication (a , b)
  print ("Le résultat de la multiplication est : ", prod)
if choix == "4":
    if b == 0:
      print ("Erreur, la division par zéro est impossible")
    else :
     quot = division (a , b)
     print ("Le résultat de la division est : ", quot)

  
