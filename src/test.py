# #! TEST CODE UNITAIRE 

# import pytest

# def addition(a, b):
#     return a + b

# def test_addition_with_positive_numbers():
#     result = addition(3, 5)
#     assert result == 8

# def test_addition_with_negative_numbers():
#     result = addition(-3, -5)
#     assert result == -8

# def test_addition_with_mixed_numbers():
#     result = addition(3, -5)
#     assert result == -2

# def test_addition_with_zero():
#     result = addition(0, 0)
#     assert result == 0
    
# # # #! TEST CODE SUITE DE FIBONNACCI

# import pytest

# def fibonacci(n):
#     if n <= 0:
#         raise ValueError("N doit être un entier positif pour calculer la suite de Fibonacci.")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def test_fibonacci_with_positive_integer():
#     assert fibonacci(1) == 0
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 1
#     assert fibonacci(4) == 2
#     assert fibonacci(5) == 3
#     assert fibonacci(6) == 5

# def test_fibonacci_with_invalid_input():
#     with pytest.raises(ValueError):
#         fibonacci(0)
#     with pytest.raises(ValueError):
#         fibonacci(-1)
#     with pytest.raises(ValueError):
#         fibonacci(-10)

# #! TEST NOMBREs premiers Jumeaux

# import pytest

# def est_premier(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def test_est_premier():
#     assert est_premier(2) == True
#     assert est_premier(3) == True
#     assert est_premier(5) == True
#     assert est_premier(7) == True
#     assert est_premier(11) == True
#     assert est_premier(4) == False
#     assert est_premier(6) == False
#     assert est_premier(9) == False
#     assert est_premier(15) == False
#     assert est_premier(25) == False

# def nombres_premiers_jumeaux(limite):
#     paires = []
#     for i in range(2, limite):
#         if est_premier(i) and est_premier(i + 2):
#             paires.append((i, i + 2))
#     return paires

# def test_nombres_premiers_jumeaux():
#     paires_attendues = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283), (311, 313), (347, 349), (419, 421), (431, 433), (461, 463), (521, 523), (569, 571), (599, 601), (617, 619), (641, 643), (659, 661), (809, 811), (821, 823), (827, 829), (857, 859), (881, 883)]
#     assert nombres_premiers_jumeaux(1000) == paires_attendues

# if __name__ == '__main__':
#     pytest.main()


# #! Hexadecimal Puissance 16

# def hex_to_decimal(hexadecimal):
#     # Tableau des caractères hexadécimaux
#     hex_chars = '0123456789ABCDEF'
#     # Convertir la chaîne hexadécimale en majuscules pour la cohérence
#     hexadecimal = hexadecimal.upper()
#     # Initialiser la valeur décimale
#     decimal = 0
#     # Parcourir la chaîne hexadécimale
#     for digit in hexadecimal:
#         # Vérifier si le caractère est un chiffre hexadécimal valide
#         if digit in hex_chars:
#             # Convertir le chiffre hexadécimal en décimal
#             decimal = decimal * 16 + hex_chars.index(digit)
#         else:
#             # Si un caractère invalide est trouvé, retourner une erreur
#             return "Le nombre hexadécimal saisi n'est pas valide."
#     # Retourner la valeur décimale calculée
#     return decimal

# # Demander à l'utilisateur d'entrer le nombre hexadécimal
# hexadecimal = input("Entrez un nombre hexadécimal : ")

# # Convertir le nombre hexadécimal en décimal
# decimal = hex_to_decimal(hexadecimal)

# # Afficher le résultat
# print("Le nombre hexadécimal", hexadecimal, "est égal à", decimal, "en décimal.")


# #! Hexadecimal Puissance 36

# def hex_to_decimal(hexadecimal):
#     # Convertir la chaîne hexadécimale en majuscules pour la cohérence
#     hexadecimal = hexadecimal.upper()
#     # Tableau des caractères hexadécimaux
#     hex_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # Initialiser la valeur décimale
#     decimal = 0
#     # Parcourir la chaîne hexadécimale
#     for digit in hexadecimal:
#         # Convertir le chiffre hexadécimal en décimal
#         if digit in hex_chars:
#             decimal = decimal * 16 + hex_chars.index(digit)
#         else:
#             # Si un caractère invalide est trouvé, retourner une erreur
#             return "Le nombre hexadécimal saisi n'est pas valide."
#     # Retourner la valeur décimale calculée
#     return decimal

# # Demander à l'utilisateur d'entrer le nombre hexadécimal
# hexadecimal = input("Entrez un nombre hexadécimal : ")

# # Convertir le nombre hexadécimal en décimal
# decimal = hex_to_decimal(hexadecimal)

# # Afficher le résultat
# print("Le nombre hexadécimal", hexadecimal, "est égal à", decimal, "en décimal.")



# #! Creation de fichiers en code python 


# try:
#     # Ouverture du fichier en mode écriture
#     with open('test.txt', 'w') as f:
#         # Écriture du contenu dans le fichier
#         f.write("Ceci est un fichier de test en Python.\n")
#         f.write("Il contient quelques lignes de texte.\n")
#         f.write("C'est un exemple simple.\n")
#     print("Fichier 'test.txt' créé avec succès.")

# except IOError:
#     print("Une erreur est survenue lors de la création du fichier.")

# #! Creation de fichiers en code Json

# import json

# # Données fictives
# donnees = [
#     {"nom": "Alice", "age": 30, "ville": "Paris"},
#     {"nom": "Bob", "age": 25, "ville": "Londres"},
#     {"nom": "Charlie", "age": 35, "ville": "New York"}
# ]

# # Chemin du fichier JSON
# nom_fichier_json = 'donnees.json'

# # Écriture des données dans le fichier JSON
# try:
#     with open(nom_fichier_json, mode='w') as fichier_json:
#         json.dump(donnees, fichier_json, indent=4)
#     print(f"Fichier JSON '{nom_fichier_json}' créé avec succès.")
# except IOError:
#     print("Une erreur est survenue lors de la création du fichier JSON.")



# #! Creation de fichiers en code python en format CSV avec Faker  

# import csv
# from faker import Faker

# # Création d'une instance Faker
# fake = Faker()

# # Creation des colonnes du csv
# donnees = [['Nom', 'Âge', 'Ville' , 'Email']]

# # Boucle for de 10 entité pour création de mes entité
# for _ in range(10):
#     nom = fake.name()
#     age = fake.random_int(min=18, max=90)
#     ville = fake.city()
#     email = fake.email()
#     donnees.append([nom, age, ville])

# # Chemin vers le nom de mon fichiers
# nom_fichier = 'donnees.csv'

# # Open de mon fichiers
# try:
#     with open(nom_fichier, mode='w', newline='') as fichier_csv:
#         writer = csv.writer(fichier_csv, delimiter=',')
#         writer.writerows(donnees)
#     print("Fichier CSV '{}' créé avec succès.".format(nom_fichier))

# except IOError:
#     print("Une erreur est survenue lors de la création du fichier CSV.")


# #! Lire un fichier CSV ou TXT

# import csv

# # Chemin du fichier CSV
# nom_fichier = 'donnees.csv'

# # Lecture des données depuis le fichier CSV
# try:
#     with open(nom_fichier, mode='r') as fichier_csv:
#         lecteur_csv = csv.reader(fichier_csv)
        
#         # Parcourir chaque ligne du fichier CSV
#         for ligne in lecteur_csv:
#             print(ligne)
# except FileNotFoundError:
#     print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
# except IOError:
#     print("Une erreur est survenue lors de la lecture du fichier CSV.")



# #! Compteur de ligne caracteres and mots avec 1000 caractères en trop

# # Chemin du fichier
# nom_fichier = 'donnees.csv'

# # Initialisation des compteurs
# nb_lignes = 0
# nb_mots = 0
# nb_caracteres = 0

# # Lecture du fichier
# try:
#     with open(nom_fichier, 'r') as fichier:
#         # Comptage des lignes, mots et caractères
#         for ligne in fichier:
#             nb_lignes += 1
#             nb_mots += len(ligne.split())
#             nb_caracteres =+ len(ligne)
# except FileNotFoundError:
#     print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
# except IOError:
#     print("Une erreur est survenue lors de la lecture du fichier.")

# # Affichage des résultats
# print("Nombre de lignes:", nb_lignes)
# print("Nombre de mots:", nb_mots)
# print("Nombre de caractères:", nb_caracteres)
