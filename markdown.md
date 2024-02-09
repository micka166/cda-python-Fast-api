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


   #### Pour avoir le reload automatique