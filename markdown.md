# Variables et Types de Données:

x = 10 (affectation de variable)

Types de données: int, float, str, list, tuple, dict, set, bool, etc.

# Opérations de Base:

+, -, \*, / (opérations mathématiques)

% (modulo)

// (division entière)
\*\* (exponentiation)


# Structures de Contrôle:

if, elif, else (instructions conditionnelles)

for (boucle for)

while (boucle while)

break, continue (contrôle de boucle)


# Fonctions:

def (définir une fonction)

return (retourner une valeur depuis une fonction)

Paramètres et arguments de fonction

# Listes et Tuples:

Indexation et découpage (liste[1], liste[1:3])

Méthodes de liste: append(), extend(), insert(), remove(), pop()

Dictionnaires:

Définition et accès (dictionnaire = {'clé': 'valeur'})

### Méthodes de dictionnaire: keys(), values(), items()
#### Ensemble

Définition (ensemble = {1, 2, 3})

Opérations d'ensemble: union, intersection, différence, etc.

# Entrée/Sortie:

print() (affichage)

input() (saisie utilisateur)

Gestion d'Exceptions:

try, except, finally
# Modules et Bibliothèques:

import (importer des modules)

Bibliothèques populaires: math, random, datetime, os, sys

Travail avec des Fichiers:

open(), read(), write(), close()
# Classes et Objets:

class (définir une classe)

**init** (méthode d'initialisation)

Attributs et méthodes de classe

Expressions Régulières:

Module re

# Manipulation de Chaînes de Caractères:

Concaténation, découpage, méthodes de chaîne

Opérations sur les Fichiers et Répertoires:

Module os
# Gestion de la Date et de l'Heure:

Module datetime

# Opérateurs Logiques
and : Retourne True si les deux expressions booléennes à gauche et à droite de l'opérateur sont vraies.
or : Retourne True si au moins l'une des expressions booléennes à gauche ou à droite de l'opérateur est vraie.
not : Retourne l'inverse de la valeur booléenne de l'expression suivant l'opérateur.

# OPERATEUR DE COMPARAISON
    == : Égal à

    != : Différent de

    < : Inférieur à

    > : Supérieur à

    <= : Inférieur ou égal à

    >= : Supérieur ou égal à




# Bonne commande pour deployer sur fast API des pages facile a faire 



    python3 src/main.py    


    ```python 
        @app.get("/", response_class=HTMLResponse)
    ```    
##### Pas obliger de HTML RESPONSE 
```python
        puis if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
```


   #### Pour avoir le reload automatique voir au dessus 



   # Deploiement Azure sur cette exercice




1. Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants :

Un compte Azure actif.
Une application FastAPI prête à être déployée.
Docker installé sur votre machine locale.
2. Dockerfile
Assurez-vous d'avoir un Dockerfile pour votre application FastAPI. Le Dockerfile spécifie comment construire l'image Docker de votre application.

Voici un exemple de Dockerfile pour une application FastAPI :

Dockerfile
Copy code
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app
Assurez-vous d'ajuster le chemin vers votre application FastAPI si nécessaire.

3. Construction de l'image Docker
Construisez l'image Docker de votre application FastAPI en exécutant la commande suivante dans le répertoire de votre projet (où se trouve votre Dockerfile) :

bash
Copy code
docker build -t nom_image .
Remplacez nom_image par le nom que vous souhaitez donner à votre image Docker.

4. Connexion à Azure
Connectez-vous à votre compte Azure en exécutant la commande suivante :

bash
Copy code
az login
Suivez les instructions pour vous connecter à votre compte Azure.

5. Création d'un groupe de ressources
Créez un groupe de ressources Azure pour votre application en exécutant la commande suivante :

bash
Copy code
az group create --name mon-groupe-ressources --location emplacement
Remplacez mon-groupe-ressources par le nom que vous souhaitez donner à votre groupe de ressources et emplacement par la région Azure de votre choix.

6. Déploiement sur Azure App Service
Déployez votre application sur Azure App Service en exécutant la commande suivante :

bash
Copy code
az webapp up --name nom_webapp --resource-group mon-groupe-ressources --sku F1 --docker-registry-image nom_image
Remplacez nom_webapp par le nom que vous souhaitez donner à votre application web, mon-groupe-ressources par le nom de votre groupe de ressources, nom_image par le nom de l'image Docker que vous avez construite.

7. Accès à votre application
Une fois le déploiement terminé, vous pouvez accéder à votre application en ouvrant le navigateur et en naviguant vers l'URL fournie par Azure App Service.

Voilà ! Votre application FastAPI est maintenant déployée sur Azure App Service et accessible en ligne.




# exception sur les valeurs d'erreurs 


```python

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée")
        result = None
    return result

numerator = 10
denominator = 0

result = division(numerator, denominator)
if result is not None:
    print("Le résultat de la division est :", result)
else:
    print("La division a échoué.")


```

# Liste d'exception que python prends en charge

1. **Exception** : La classe de base pour toutes les exceptions.

2. **ArithmeticError** : La classe de base pour toutes les erreurs arithmétiques.

3. **OverflowError** : Levée lorsqu'une opération numérique dépasse la limite de capacité d'un type numérique.
   
4. **ZeroDivisionError** : Levée lorsqu'une division ou un modulo par zéro est tenté.

5. **FloatingPointError** : Levée lorsqu'une erreur de point flottant se produit.

6. **AssertionError** : Levée lorsqu'une instruction assert échoue.

7.  **AttributeError** : Levée lorsqu'un attribut référencé n'est pas trouvé.

8.  **EOFError** : Levée lorsqu'il n'y a plus d'entrée à lire dans une fonction intégrée input().

9.  **ImportError** : Levée lorsqu'un module importé ne peut pas être trouvé.

10. **IndexError** : Levée lorsqu'un index d'une séquence est hors de portée.

11. **KeyError** : Levée lorsqu'une clé de dictionnaire n'est pas trouvée.

12. **NameError** : Levée lorsqu'un nom n'est pas trouvé localement ou globalement.

13. **NotImplementedError** : Levée lorsqu'une fonctionnalité n'est pas implémentée dans une classe ou un module donné.

14. **TypeError** : Levée lorsqu'une opération ou une fonction est appliquée à un objet de type incorrect.

15. **ValueError** : Levée lorsqu'une fonction reçoit un argument du bon type mais avec une valeur inappropriée.

16. **FileNotFoundError** : Levée lorsqu'un fichier ou un répertoire n'est pas trouvé.

17. **PermissionError** : Levée lorsqu'un opération n'est pas autorisée en raison de permissions insuffisantes.

18. **OSError** : La classe de base pour les exceptions liées au système d'exploitation.


# Lecture & écriture de fichiers sur le language python

En Python, vous pouvez lire et écrire des fichiers en utilisant les fonctions open(), read(), write() et close(). Voici un exemple de lecture et d'écriture de fichiers en Python :

## Methode pour lire les fichiers
```python 

# Ouvrir un fichier en mode lecture
with open('mon_fichier.txt', 'r') as fichier:
    # Lire le contenu du fichier ligne par ligne
    for ligne in fichier:
        print(ligne.strip())  # Afficher chaque ligne (strip() pour retirer les sauts de ligne)

# Le fichier est automatiquement fermé à la fin du bloc "with"  
```

## Méthode pour ecrire les fichiers 

```python

# Ouvrir un fichier en mode écriture
with open('nouveau_fichier.txt', 'w') as fichier:
    # Écrire dans le fichier
    fichier.write("Ceci est une nouvelle ligne.\n")
    fichier.write("Voici une autre ligne.")

# Le fichier est automatiquement fermé à la fin du bloc "with"

```

| Caractère | Signification                                           |
|-----------|---------------------------------------------------------|
| `'r'`     | ouvre en lecture (par défaut)                          |
| `'w'`     | ouvre en écriture, en effaçant le contenu du fichier   |
| `'x'`     | ouvre pour une création exclusive, échouant si le fichier existe déjà |
| `'a'`     | ouvre en écriture, ajoutant à la fin du fichier s'il existe |
| `'b'`     | mode binaire                                            |
| `'t'`     | mode texte (par défaut)                                 |
| `'+'`     | ouvre en modification (lecture et écriture)            |


# Commande pour lire rapidement des fichiers 

| Commande                            | Description                                                                                       | Exemple d'utilisation         |
|-------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------|
| `wc [nom_fichier]`                  | Compte le nombre de lignes, de mots et de caractères dans le fichier spécifié.                   | `wc votre_fichier.txt`       |
| `wc -l [nom_fichier]`               | Compte uniquement le nombre de lignes dans le fichier spécifié.                                  | `wc -l votre_fichier.txt`    |
| `wc -w [nom_fichier]`               | Compte uniquement le nombre de mots dans le fichier spécifié.                                    | `wc -w votre_fichier.txt`    |
| `wc -c [nom_fichier]`               | Compte uniquement le nombre de caractères dans le fichier spécifié.                               | `wc -c votre_fichier.txt`    |
| `wc -m [nom_fichier]`               | Compte uniquement le nombre de caractères multioctets dans le fichier spécifié.                  | `wc -m votre_fichier.txt`    |
| `wc -L [nom_fichier]`               | Affiche la longueur de la ligne la plus longue dans le fichier spécifié.                         | `wc -L votre_fichier.txt`    |
