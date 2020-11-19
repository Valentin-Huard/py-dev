# Backend TANSion 

## Specification 

```
Python : 3.9
PostgreSQL : 13
``

## Setup

Des scripts pour automatisé l'installation sont disponibles dans le dossier "/api/bash"
Veuillez les executer à partir de "/api".

```bash
UNIX 
sh bash/setup.sh

Windows
bash/setup.bat
```
Ces scripts mettent en place :
- L'environnement virtuel python
- Les dépendances du projet
- La base de données
- Le jeu de données

## Configuration

Les identifiants de connexion de la base de données sont à rentrer dans le fichier "/api/settings.py"
