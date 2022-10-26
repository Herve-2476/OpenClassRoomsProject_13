## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Herve-2476/OpenClassRoomsProject_13.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Deployement

The CI/CD pipeline that we are going to use will allow, after a local push to your github repository, to automatically perform various operations. First of all the linting and the tests. If these are valid, we build a Docker image that we push to Docker Hub. If the containerization went well we put the site in production on Heroku. Finally we will monitoring our application with Sentry.

### Requirements

- a Docker account
- a CircleCi account
- a Heroku account
- a Sentry account

### Configuration

First of all you have to create a remote repository on your Github account of your local repository. Then go to your Heroku account and create a new app with the button `new`. You have to retrieve also your heroku token. You can do that via the CLI of Heroku (heroku login, heroku auth:token). Then go to your Circleci account and link it to your Github account. Follow your remote repository with the button `Set up project`.For the following you also need a valid django secret key, you can generate one with this command on the terminal :
- python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

The important point now is to set the environment variables in Circleci. Select the button `Project Settings` and add the following environment variables.


- DJANGO_SECRET_KEY = A valid django secret key, different from the one in the settings.py file
- DOCKER_PASS = Your password of your Docker account
- DOCKER_USER = Your username of your Docker account
- HEROKU_API_KEY = You find this key on you Heroku account
- HEROKU_APP_NAME = The name of the app you have created on your Heroku account
- HEROKU_TOKEN = You retrieve it via the CLI of Heroku
- HEROKU_USER = Your username of your Heroku account

To use Sentry, go to your account and create a Django project. Copy the `dsn` and paste it in the settings.py file to replace mine. The Sentry dsn is not secret.

### Running the pipeline
Push a modification of your local repository to your remote repository and the pipeline runs automatically

### Link to the deployement Heroku
 - https://oc-lettings-2476.herokuapp.com/

### Running the Docker image
You can use the Docker image on your local machine. For that install Docker desktop app on your machine and retrieve the name and the tag of the image CircleCi created. Use the following command :

- docker run -d -p 7999:7999 <image_name:tag>

You can use website at : 127.0.0.1:7999

