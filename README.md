<!-- cSpell:disable -->

# 🏦 Projet : MyScrumBank - Sprint 1

_Atelier d'initiation au développement et à l'Agilité pour les stagiaires de seconde_

Bienvenue dans l'équipe ! Vous allez réaliser le premier Sprint de notre nouvelle application bancaire web en utilisant **Streamlit** (Python) et **SQLite**.

- **Streamlit** est un framework Python qui permet de créer des applications web interactives et des tableaux de bord de données très rapidement, sans avoir besoin de connaître le HTML ou le CSS.
- **SQLite** est un moteur de base de données ultra-léger. Contrairement aux gros serveurs de base de données, il stocke toutes les informations (clients, soldes, transactions) dans un simple fichier sur votre ordinateur (`data/banque.db`). Il est directement intégré dans Python, donc rien à installer !

---

## 🎯 Le Challenge du Sprint 1

Votre objectif est de développer l'application en autonomie en utilisant une **Intelligence Artificielle (IA)** pour vous aider à coder. Votre application devra valider les 4 User Stories (US) suivantes :

- **US1 (Data) :** Je veux une application bancaire qui affiche mes transactions et mon solde.
- **US2 (Sécurité) :** Je veux pouvoir me connecter et ne voir _que_ mes données (étanchéité des comptes).
- **US3 (Fonctionnalité) :** Je veux pouvoir contacter le service client (via un formulaire ou un bouton).
- **US4 (Design) :** Je veux respecter la charte graphique BNPP (couleurs vert/blanc, style épuré).

---

## 🛠️ Étape 1 : Préparation de votre environnement

### 🐍 Étape Optionnelle : Installer Python sur Windows (Si non présent)

Avant de commencer, vérifiez si Python est déjà installé sur votre machine :

1. Ouvrez l'invité de commandes Windows (tapez `cmd` dans la barre de recherche).
2. Tapez : `python --version`

Si un message d'erreur s'affiche, installez-le :

- **Sur un PC personnel :** Rendez-vous sur [python.org/downloads](https://www.python.org/downloads/) et téléchargez la version proposée.
- **Sur un PC d'entreprise :** Ouvrez le "Centre Logiciel" (Software Center) de votre poste et installez Python.
- ⚠️ **ATTENTION PIÈGE À L'INSTALLATION :** Lors du lancement du fichier `.exe` téléchargé, **cochez impérativement la case tout en bas : `[X] Add python.exe to PATH`** avant de cliquer sur _Install Now_.
- Fermez votre terminal, ouvrez-en un nouveau et re-testez `python --version`.

### 📦 Étape 2 : Installer Streamlit

Dans votre invité de commandes (`cmd`), tapez la commande suivante :

````bash
pip install streamlit

Si vous êtes sur Linux :
Si Linux vous bloque avec un message parlant de "externally-managed-environment", forcez l'installation locale pour votre utilisateur en tapant cette commande :
```bash
pip3 install streamlit --break-system-packages


### 4. Préparation : installation des scripts depuis github
Connectez-vous sur
https://github.com/yanlt-web/atelier-scrum-bank-app/
télécharger le .zip: Cliquez sur le bouton vert Code, puis sur Download ZIP.
décompressez-le dans un dossier de votre choix.


### 5. : Initialisation de la Base de Données (SQLite)

Ouvrez votre terminal directement dans le dossier de votre projet décompressé, puis lancez le script qui va générer le fichier
 de la base de données et injecter le jeu d'essai (faux clients et historique) :
Bash

python data/import_tests.py

Si tout fonctionne, le message suivant apparaît : 🎉 Base de données SQLite initialisée avec succès !


### 6. Agis comme un développeur Python expert. Je crée une application Web interactive avec Streamlit. L'application doit se connecter à une base de données SQLite locale située dans le fichier data/banque.db.

Ouvrez le fichier src/app.py dans votre éditeur de code (VS Code ou Bloc-notes). 
Il est actuellement vide. Vous allez copier le "Prompt" (la consigne) ci-dessous et le donner à votre assistant IA pour générer le premier code de votre application.

"Écris le code pour le Sprint 1 qui contient :

    Une barre latérale pour se connecter avec une adresse e-mail (US2).

    Une fois connecté, une requête SQL SELECT va chercher dans la table clients le solde et les informations de cet utilisateur pour les afficher proprement (US1).

    Un formulaire ou un bouton pour contacter le service client (US4).

    Applique un style visuel épuré inspiré de la charte graphique de la BNP Paribas (Utilise le vert comme couleur principale pour les boutons ou les titres) (Ref: US3)."
"
````
### 7. Lancer votre application pour la tester :

Pour voir votre application s'afficher dans votre navigateur web, tapez cette commande dans votre terminal :
Bash

streamlit run src/app.py

À chaque fois que vous modifiez votre code ou demandez une correction à l'IA, sauvegardez le fichier et actualisez la page de votre navigateur !