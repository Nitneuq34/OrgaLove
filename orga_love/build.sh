#!/usr/bin/env bash
# Sortie en cas d'erreur
définir -o errexit 

# Modifiez cette ligne selon les besoins de votre gestionnaire de paquets (pip, poetry, etc.)
pip install -r requirements.txt 

# Convertir des fichiers d'actifs statiques
python manage.py collectstatic --no-input

# Appliquer toutes les migrations de bases de données en suspens
python manage.py migrate
