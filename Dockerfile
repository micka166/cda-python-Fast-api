# Utiliser l'image de base Python 3.8 slim-buster
FROM python:3.8-slim-buster

# Définir le répertoire de travail à la racine du projet
WORKDIR /

# Copier le fichier requirements.txt à la racine du projet
COPY requirements.txt .

# Installer les dépendances Python spécifiées dans requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copier tous les fichiers du projet à la racine du conteneur
COPY . .

# Exposer le port 8000 pour permettre l'accès à votre application FastAPI
EXPOSE 8000

# Commande pour exécuter l'application FastAPI lorsque le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




