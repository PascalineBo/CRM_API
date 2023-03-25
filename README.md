# CRM API

## Objectif du projet: développer une API avec une base de données PostgreSQL pour élaborer un système de CRM sécurisé interne à une entreprise d'évenementiel appelée Epic Events

### Exigences techniques Kanban[https://www.notion.so/5a4642c14eef48c78c9e1b98a8e0a3fc?v=12d25b7081ba436a9e06f0e99cdcae25]

#### Architecture du projet:

Le projet est découpé selon les dossiers suivants:

#### Dossier authentication:
Ce dossier contient:
- tous les fichiers de code définissant les interfaces (views) et les procédés de sign up et de login; 
l'API utilise les modèles AbstractUser et UserAdmin de Django; l'authentification est sécurisée grâce à djangorestframework-simple-jwt) 
- un fichier permissions.py qui définit les permissions des différents utilisateurs pour les opérations CRUD des ModelViewsets

#### Dossier Epic:
Ce dossier contient:
- le fichier settings.py où est défini notamment le recours à 'rest_framework', 'rest_framework_simplejwt', 'authentication' de Django. 
Egalement, ligne 84 et suivantes, ce fichier settings.py définit les paramètres de connection à une base de données PostgreSQL. IMPORTANT: ligne 90, pour la clé 'HOST', 
veuillez modifier la valeur et mettre le nom de votre localhost.
- le fichier urls.py, où sont définies les urls de connexion, d'obtention et de rafraîchissement des tokens, et les routers définissant 
les différents endpoints. La liste des endpoints de cette API est:

- <pre>epic/customers/  <pre>/customers/{id}/:

liste complète des clients; CRUD d'un client selon son id et les permissions

- <pre>/epic/users/ <pre> /epic/users/{id}

liste complète des utilisateurs de la base de données; CRUD d'un utilisateur d'un projet selon son id, uniquement pour le management (CONTROLLING)

- <pre>/epic/contracts/ <pre>/epic/contracts/{id}

liste complète des contrats de la base de données; CRUD d'un contrat selon son id et les permissions

- <pre>/epic/events/ <pre>/epic/events/{id}

liste complète des évènements de la base de données; CRUD d'un évenement selon son id et les permissions

#### Dossier core:
Ce dossier contient un fichier models.py et un fichier views.py, où sont définis respectivement un Modèle dont vont hériter les autres modèles des Appli (sauf authentication), et un Mixin dont vont hériter les autres views des Appli (sauf authentication).


#### Dossier contract:
Ce dossier est découpé de la façon suivante:
- un fichier models.py avec le modèle de table contrat de la base de données
- un fichier serializers.py avec le serializers qui permettent de charger les données dans la base de données et de les rapatrier (au format JSON)
- un fichier views.py qui définit (i) les fonctions de service des données grâce aux ModelViewsets: Un ModelViewset  est comparable à une super vue Django qui regroupe   à la fois CreateView, UpdateView, DeleteView, ListView  et DetailView
(ii) les filtres de l'endpoint: [http://localhost:8000/epic/contracts/].
Les filtres disponibles sont:
 - `?name = <company_name>`, 
 - `?search= <part_of_the_creation_date>`,
 - `?e-mail= <customer_email>`,
 - `?price= <contract_amount>`,
 
 #### Dossier customer:
 Dossier similaire au dossier contract, appli qui gère le code pour les Clients de la base de données.
Les filtres de l'endpoint: [http://localhost:8000/epic/customers/] disponibles sont:
 - `?name = <company_name>`, 
 - `?e-mail= <customer_email>`,
 
 #### Dossier event:
 Dossier similaire au dossier contract, appli qui gère le code pour les Clients de la base de données.
Les filtres de l'endpoint: [http://localhost:8000/epic/events/] disponibles sont:
 - `?name = <company_name>`, 
 - `?e-mail= <customer_email>`,
 - `?search= <part_of_the_event_date>`,

#### Fichier manage.py:
Ce fichier contient le script utilitaire de ligne de commande de Django

#### Permissions: 
Les utilisateurs ont les permissions suivantes:
- Le Management (CONTROLLING) a accès à tous les endpoints et peut faire toutes les opérations du CRUD
- L'équipe Ventes (SALES) a accès à tous les objets de la Base de Données en Lecture, sauf les données des Utilisateurs; 
Elle peut créer des Clients, les mettre à jour si ce sont les siens, créer des Contrats et les mettre à jour si ce sont les siens;
- L'équipe Support (SUPPORT) a accès à tous les objets de la Base de Données en Lecture, saut les données des Utilisateurs;
Elle peut uniquement modifier et mettre à jour les évènements dont elle est responsable.

## Comment installer cette Appli sur votre ordinateur:
(i) Requis: téléchargez **[Python 3.10](https://www.python.org/downloads/)**

(ii) puis, avec les commandes du terminal, positionnez-vous sur le dossier dans lequel vous souhaitez installer l'Appli

(iii) pour importer les fichiers de ce repository, tapez la commande git:

`git clone https://github.com/MargueriteEffren/OC_Projet12.git`

(iv) puis positionnez vous dans le dossier OC_Projet12 (`cd OC_Projet12`)

(v) créez votre environnement virtuel, par exemple avec la commande:

`python3 -m venv env`

(vi) à l'aide des commandes du terminal, activez votre environnement virtuel 
(si votre environnement virtuel s'appelle env):
> Sur Windows  
- terminal de type bash : `source env/Scripts/activate`
- terminal de type shell : `env\Scripts\activate`
  
> Sur Mac ou Linux
- `source env/bin/activate`

(vii) puis installez les packages requirements du projet à l'aide de la commande:

`pip install -r requirements.txt`

## Comment utiliser l'Appli:

### Expérience Admin:

Pour avoir une vue admin de la base de données, vous pouvez utiliser directement dans votre navigateur l'url http://127.0.0.1:8000/admin, et vous connecter en tant que superuser avec les identifiants:

username: Admin2

password: Admin-OC

### Expérience Développeur:

(i) avec votre terminal, positionnez vous dans le dossier dans lequel vous avez installé l'Appli

(ii) activez l'environnement virtuel

(iii) ensuite tapez la commande 

`python3 manage.py runserver`

pour exécuter le serveur de développement

(iv) puis, avec Postman par exemple, vous pouvez vous connecter avec l'url http://127.0.0.1:8000/epic/login, en remplissant les champs username et password;

(v) vous pouvez exécuter des requêtes (Postman) vers  http://127.0.0.1:8000/epic/, suivi de l'url des différents endpoints:

Exemple: http://127.0.0.1:8000/epic/customers/1/ pour requêter le client 1

### Informations de logging:
Vous pourrez trouver les informations de logging dans le fichier epic_logging.log qui sera automatiquement généré à la racine du projet à chaque requête.
