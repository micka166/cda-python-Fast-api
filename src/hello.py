# # * -------EXO1---------#
# !  addition basique
# print(12+5)

# # * -------EXO2---------#
# ! permet de fire bonjour + mon nom 
# # first_name = 'micka'
# # print('Bonjour',first_name)


# # * -------EXO3---------#
# !  print notre nom
# first_name = input('Votre prenom est .')
# print('vous êtes' , first_name)


# ## *-------EXO4---------#
# ! Formulaire sur nom age et prénom
# first_name =  input('Votre prenom est.')
# surname = input('Votre nom est')
# age = int(input('Votre année de naissance'))
# naissance = 2024 - age 

# print(first_name , surname ,'votre avez : ' , naissance , 'ans cette année' )

# # * -------EXO5---------#
# ! Double de 2 
# double = int(input('Le double de'))
# total = print(double*2)


# # * -------EXO6---------#

# ! Calcule de l'IMC

# poids = float(input('donnez votre poids'))
# taille = float(input('donnez votre taille '))

# imc = float(poids)/taille

# print(f'Votre imc est de ', imc)

## *-----------EXO7-----------

# ! cette fonction permet de mettre son prénom dans une boite 

# class AnsiColor:
#     GREEN = '\033[32m';'\033[44m'
#     RESET = '\033[0m'

# def draw_colored_box(text):
#     width = len(prenom) + 6 
#     height = 3

#     # Top border
#     print('┌' + '─' * (width - 2) + '┐')

#     # Side borders with space in between
#     for _ in range(height - 2):
#         print('│' + ' ' * (width - 2) + '│')

#     # Middle line with colored text
#     colored_text = AnsiColor.GREEN + text + AnsiColor.RESET
#     print(f'│  {colored_text}  │')

#     # Bottom border
#     print('└' + '─' * (width - 2) + '┘')

# # Example usage
# prenom = input('Mettez votre prénom : ')
# draw_colored_box(prenom)

# *-----------EXO8------------#

# ! cette fonction permet combiner 2 phrase

# phrase = input('Entrez une phrase : ')


# mots = phrase.split()

# phrase2 = '/'.join(mots)

# print(phrase2)


# *-----------EX10------------#
# ! cette fonction permet de convertir degres en fahrenheit

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# # Saisie de l'utilisateur
# celsius_temperature = float(input("Entrez la température en degrés Celsius : "))

# # Conversion
# fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# # Affichage du résultat
# print(f"{celsius_temperature} degrés Celsius équivalent à {fahrenheit_temperature:.2f} degrés Fahrenheit.")


# *-----------EX14------------#
# ! cette fonction permet de savoir le theorème de pythagore
# def pythagorean_theorem(a, b):
#     c = (a**2 + b**2)**0.5
#     return c


# side_a = float(input("Entrez la longueur du côté a : "))
# side_b = float(input("Entrez la longueur du côté b : "))


# side_c = pythagorean_theorem(side_a, side_b)


# print(f"Pour un triangle rectangle avec les côtés a={side_a} et b={side_b}, la longueur du l'hypothenuse c est {side_c:.2f}.")



# *-----------EX15------------#

# ! cette fonction permet de savoir la TVA ET LA HT
# def calcul_tva(montant_ht, taux_tva):
#     tva = montant_ht * (taux_tva / 100)
#     montant_ttc = montant_ht + tva
#     return tva, montant_ttc


# montant_ht = float(input("Entrez le montant hors taxe : "))
# taux_tva = float(input("Entrez le taux de TVA en pourcentage : "))


# tva_result, montant_ttc_result = calcul_tva(montant_ht, taux_tva)


# print(f"Montant HT : {montant_ht:.2f}€")
# print(f"Taux de TVA : {taux_tva}%")
# print(f"Montant TVA : {tva_result:.2f}€")
# print(f"Montant TTC : {montant_ttc_result:.2f}€")



# *-----------EX15------------#


# ! cette fonction permet de savoir la puissance de 2 d'un nombre
# import math

# n = int(input("Entrez le nombre de chiffres pour la puissance de 2: "))
# resultat = 2**n

# total = len(str(resultat))
# log = math.log10(resultat)

# print(f"2^{n} longueur {total}")



# *-----------EX16------------#

# ! cette fonction permet de savoir la racine et le log

# import math
# n = int(input("Entrez le chiffre: "))

# racine = math.sqrt(n)
# log = math.log(n)
# print(racine)
# print(log)



# *-----------EX17------------#
# ! cette fonction permet de savoir la racine carrée et cubique d'un nombre

# import math
# n = int(input("Entrez le chiffre: "))

# racine = math.sqrt(n)
# racine_cubique = math.pow(n, 1/3)

# print(racine)
# print(racine_cubique)


# *-----------EX18------------#

# ! cette fonction permet de calculer la rayon et l'aire d'un cercle
# import math

# rayon = float(input("Entrez le rayon du cercle"))

# perimetre = 2 *math.pi * rayon

# surface = math.pi * rayon**2



# print(perimetre)
# print(surface)


# *-----------EX19------------#
# ! cette fonction permet de faire un regex pour trouver les adresse email
# import re


# texte = "Voici une chaîne de caractères avec une adresse e-mail visual@studio.azertyuioigjreeiohrigfeljfifjiof exemple@example.com cci@campus.pizaezeaf et une autre adresse test@test.com. enculezefdgbvfebjnblj@grfijdbgnl.fr rexdmid@fkdslgbdgnj.fr zdifeklgnzrbf koefzgreolmfe,klge,bremtkb;fmb mclaren@campus.fr fkezl,nmegkrzpùek"


# pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# resultats = re.findall(pattern_email, texte)

# print("Adresses e-mail trouvées :")
# for adresse in resultats:
#     print(adresse)


 # !-----------EX19------------# Structure de contrôle Debut du jour 2 

# ?EXEMPLE D'UNE BOUCLE "FOR" CLASSIQUE

# # texte = "Voici une chaîne de caractères avec une adresse e-mail visual@studio.azertyuioigjreeiohrigfeljfifjiof exemple@example.com cci@campus.pizaezeaf et une autre adresse test@test.com. enculezefdgbvfebjnblj@grfijdbgnl.fr rexdmid@fkdslgbdgnj.fr zdifeklgnzrbf koefzgreolmfe,klge,bremtkb;fmb mclaren@campus.fr fkezl,nmegkrzpùek"
# print("Adresses e-mail trouvées :")
# for adresse in resultats:
#     print(adresse)


# ? Exemple de Boucle Infinty

# i = 1
# while i < 5:
#     print(f"{i=}")
#     i+=1



#  # * EX 20

# ! cette fonction permet de faire une somme de nombre entier 

# texte_utilisateur = input("Entrez une chaîne de nombres : ")

# mots = texte_utilisateur.split()


# somme = 0


# for mot in mots:
#     try:
#         nombre = int(mot)
#         if nombre > 0:
#             somme += nombre
#     except ValueError:
#         print('votre numero est invalide')

# print("Somme des nombres entiers positifs :", somme)


# * EX 21
# ! cette fonction permet de faire une boucle sur 101 nombres

# for i in range(2 ,101 ,2):
#     print(i,end='')
    
# print()    


# * EX 22
# ! cette fonction permet de savoir le nombre de voyelle dans une phrase
#? Pour faire sans les accent il faut importer unidecode et utiliser unidecode.unidecode(mot)
# texte_utilisateur = input("Entrez du texte : ")


# compteur_voyelles = 0


# voyelles = "aeiouàâäéèêëîïôöùûüyý"

# cap = voyelles.lower()



# for caractere in texte_utilisateur:
#     if caractere in voyelles:
#         compteur_voyelles += 1


# print("Le nombre de voyelles dans le texte est :", compteur_voyelles)

# * EX23


# ! cette fonction permet de savoir si un nombre est factorielle
# def factorielle(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorielle(n-1)

# nombre_utilisateur = int(input("Entrez un nombre pour calculer sa factorielle : "))

# if nombre_utilisateur < 0:
#     print("La factorielle n'est définie que pour les nombres positifs.")
# else:
#     resultat_factorielle = factorielle(nombre_utilisateur)
#     print(f"La factorielle de {nombre_utilisateur} est : {resultat_factorielle}")



# * EX24

# ! cette fonction permet de savoir si un mot est un palindrome
# def est_palindrome(chaine):

#     chaine = chaine.lower().replace(" ", "")
    
#     return chaine == chaine[::-1]


# texte_utilisateur = input("Entrez une chaîne de caractères : ")

# if est_palindrome(texte_utilisateur):
#     print("C'est un palindrome.")
# else:
#     print("Ce n'est pas un palindrome.")



# * EX25 
# ! cette fonction permet de savoir si un nombre est premier
 

# def est_premier(nombre):
#     est_premier = True
#     for i in range(2, int(nombre**0.5) + 1):
#         if nombre % i == 0:
#             est_premier = False
#             break
#     return est_premier

# # Demander à l'utilisateur d'entrer un nombre
# nombre_utilisateur = int(input("Entrez un nombre : "))

# # Vérifier si le nombre est premier et afficher le résultat
# if est_premier(nombre_utilisateur):
#     print(f"{nombre_utilisateur} est un nombre premier.")
# else:
#     print(f"{nombre_utilisateur} n'est pas un nombre premier.")




#* EXO 26

#! Suite de fibonnacci 


# def fibonacci(n):
#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib

# n = int(input("Entrez le nombre d'éléments de la suite de Fibonacci : "))

# resultat = fibonacci(n)
# print("Suite de Fibonacci :", resultat)

#* EXO 27

#! somme des carré de d'un nombre positif


# def somme_carres_chiffres(nombre):
#     if nombre < 0:
#         print("Veuillez entrer un nombre positif.")
#         return None

    # chiffres = [int(c) for c in str(nombre)]
    # somme_carres = sum(c**2 for c in chiffres)

#     return somme_carres


# nombre_utilisateur = int(input("Entrez un nombre positif : "))

# resultat = somme_carres_chiffres(nombre_utilisateur)

# if resultat is not None:
#     print(f"La somme des carrés des chiffres de {nombre_utilisateur} est : {resultat}")


#* EXO 28

#! PGDC de 2 nombre fait par l'utilisateur



# def pgcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# nombre1 = int(input("Entrez le premier nombre : "))
# nombre2 = int(input("Entrez le deuxième nombre : "))


# resultat_pgcd = pgcd(nombre1, nombre2)

# print(f"Le PGCD de {nombre1} et {nombre2} est : {resultat_pgcd}")
 

# import math

# user = int(input('Veuillez mettre un nombre'))
# user2 = int(input('Veuillez mettre un nombre'))

# total = math.gcd(user , user2)

# print('LE PGCD EST ' , total)

#* EXO 29

#! Nombre parfait donne par l'utilisateur

# def nombre_parfait(nombre):
#     if nombre <= 0:
#         return False

#     somme_diviseurs = sum(diviseur for diviseur in range(1, nombre) if nombre % diviseur == 0)

#     return somme_diviseurs == nombre


# nombre_utilisateur = int(input("Entrez un nombre positif : "))


# if nombre_parfait(nombre_utilisateur):
#     print(f"{nombre_utilisateur} est un nombre parfait.")
# else:
#     print(f"{nombre_utilisateur} n'est pas un nombre parfait.")
    
    
    
# def est_parfait(n):
#     somme_diviseurs = 1

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             somme_diviseurs += i
#             somme_diviseurs += n // i

#     return n == somme_diviseurs

# # Demander à l'utilisateur d'entrer un nombre positif
# nombre_utilisateur = int(input("Entrez un nombre positif : "))

# # Vérifier si le nombre est parfait
# if est_parfait(nombre_utilisateur):
#     print(f"{nombre_utilisateur} est un nombre parfait.")
# else:
#     print(f"{nombre_utilisateur} n'est pas un nombre parfait.")
#! pour trouver les 4 premiers nombre parfaits
# def est_parfait(n):
#     somme_diviseurs = 1

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             somme_diviseurs += i
#             somme_diviseurs += n // i

#     return n == somme_diviseurs

# def trouver_n_premiers_parfaits(n):
#     nombres_parfaits = []
#     i = 2

#     while len(nombres_parfaits) < n:
#         if est_parfait(i):
#             nombres_parfaits.append(i)
#         i += 1

#     return nombres_parfaits

# # Trouver les 4 premiers nombres parfaits
# premiers_nombres_parfaits = trouver_n_premiers_parfaits(4)

# print("Les 5 premiers nombres parfaits sont :", premiers_nombres_parfaits)


#* EXO 30
#! Nombre factorise division succesive donne par l'utilisateur

# def factoriser(nombre):
#     facteurs = []

   
#     while nombre % 2 == 0:
#         facteurs.append(2)
#         nombre = nombre // 2

   
#     for i in range(3, int(nombre**0.5) + 1, 2):
#         while nombre % i == 0:
#             facteurs.append(i)
#             nombre = nombre // i

#     if nombre > 2:
#         facteurs.append(nombre)

#     return facteurs


# nombre_utilisateur = int(input("Entrez un nombre à factoriser : "))


# facteurs = factoriser(nombre_utilisateur)

# print(f"Les facteurs de {nombre_utilisateur} sont : {facteurs}")



# * EX 31
# ! Nombre amis 


# def sommeDiviseurs(n):
#     somme = 0
#     for i in range(1, n):
#         if n % i == 0:
#             somme += i
#     return somme

# def nombresAmis(m, n):
#     return sommeDiviseurs(m) == n and sommeDiviseurs(n) == m

# # Demander à l'utilisateur d'entrer deux nombres
# nombre1 = int(input("Entrez le premier nombre : "))
# nombre2 = int(input("Entrez le deuxième nombre : "))

# # Vérifier si les nombres sont amis
# if nombresAmis(nombre1, nombre2):
#     print(f"{nombre1} et {nombre2} sont des nombres amis.")
# else:
#     print(f"{nombre1} et {nombre2} ne sont pas des nombres amis.")

# def sommeDiviseurs(n):
#     somme = 0
#     for i in range(1, n):
#         if n % i == 0:
#             somme += i
#     return somme

# def nombresAmis(m, n):
#     return sommeDiviseurs(m) == n and sommeDiviseurs(n) == m

# # Limite supérieure pour la recherche de paires de nombres amicaux
# limite = 5000

# # Boucle pour générer et tester des paires de nombres amicaux
# for nombre1 in range(2, limite):
#     for nombre2 in range(nombre1 + 1, limite):
#         if nombresAmis(nombre1, nombre2):
#             print(f"{nombre1} et {nombre2} sont des nombres amis.")

#? 
# ? # Opérateur "et" (and)
# ? x = 5
# ? y = 10
# ? z = 15
# ? resultat_et = (x < y) and (y < z)
# ? print(f"{x} < {y} et {y} < {z} est {resultat_et}")

# ? # Opérateur "ou" (or)
# ? a = True
# ? b = False
# ? resultat_ou = a or b
# ? print(f"{a} ou {b} est {resultat_ou}")

# ? # Opérateur "non" (not)
# ? c = True
# ? resultat_non = not c
# ? print(f"non {c} est {resultat_non}")

#!----------------------------------------------------------------------------------------passage en binaire avec les operateur logique
# * EX 31
# ! binaire

# def decimal_vers_binaire(decimal):
#     return bin(decimal)

# def demander_nombre_decimal():
#     return int(input("Entrez un nombre décimal : "))

# def afficher_representation_binaire(nombre_decimal, nombre_binaire):
#     print(f"Le nombre {nombre_decimal} en binaire est : {nombre_binaire}")

# # Utiliser les fonctions
# nombre_decimal = demander_nombre_decimal()

# # Utilisation des opérateurs logiques "et" et "ou"
# if nombre_decimal >= 0 and nombre_decimal % 1 == 0:
#     nombre_binaire = decimal_vers_binaire(nombre_decimal)
#     afficher_representation_binaire(nombre_decimal, nombre_binaire)
# else:
#     print("N/A (nombre invalide)")



# * EX 32
# ! Liste contenat les carre entre 1 et 10 



# carre = [x ** 2 for x in range(1, 11)]
# print(carre)


# * EX 33
# ! Liste contenat une liste de mots avec seulement de 4 caracteres

# mots = ["apple", "banana", "pear", "orange", "grape", "kiwi", "plum", "melon" , "lol"]

# quatre_lettres = [mot for mot in mots if len(mot) >4]

# print(quatre_lettres)


# * EX 34
# ! Écrivez une fonction qui compte le nombre d'occurrences de chaque élément dans une liste et retourne un dictionnaire avec ces comptages.
# import random
# import json
# import string

# def valeurs_dictionnaire(liste):
#     count = {}
    
#     for element in liste:
#         if element in count:
#             count[element] += 1
#         else:
#             count[element] = 1
#     return count

# lettre = [random.choice(string.ascii_letters) for _ in range(50)]



# resultat = valeurs_dictionnaire(lettre)
# json = json.dumps(resultat)
# print(json)


# * EX 35
# ! Fonction pour