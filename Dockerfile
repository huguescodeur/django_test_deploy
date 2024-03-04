# Utilisez une image de base Python 3
FROM python:3.8-slim

# Définissez le répertoire de travail
WORKDIR /src

# Copiez les fichiers de requirements et installez les dépendances
COPY requirements.txt /src/
RUN pip install -r requirements.txt

# Copiez le reste des fichiers du projet
COPY . /src/

# Exposez le port sur lequel l'application sera exécutée
EXPOSE 8000

# Démarrez l'application avec Gunicorn
CMD ["gunicorn", "test_deploy.wsgi:application", "-b", "0.0.0.0:8000"]
