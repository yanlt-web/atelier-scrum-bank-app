import os
import sqlite3

# Définition du chemin de la base de données
DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "banque.db")


def init_db():
    # S'assurer que le dossier data existe
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    # Connexion à la base SQLite (crée le fichier s'il n'existe pas)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("🛠️  Création des tables dans SQLite...")

    # 1. Création de la table Clients (US1 & US2)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            solde REAL NOT NULL
        )
    """
    )

    # 2. Création de la table Transactions (US1)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            montant REAL NOT NULL,
            categorie TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients (id)
        )
    """
    )

    # Nettoyage des anciennes données si le script est rejoué
    cursor.execute("DELETE FROM transactions")
    cursor.execute("DELETE FROM clients")

    print("💾  Injection du jeu d'essai (Données de test)...")

    # 3. Insertion des clients (Jeu d'essai)
    # Note : J'ai glissé un petit clin d'œil à votre profil d'études et vos passions pour personnaliser le test !
    clients = [
        ("Dupont", "Jean", "jean.dupont@bnpp.com", 1450.50),
        ("Ait", "Clemence", "clemence.ait@deutsch-droit.de", 250.00),
        ("Forensic", "Data", "detective@forensic.fr", 8900.00),
    ]

    cursor.executemany(
        "INSERT INTO clients (nom, prenom, email, solde) VALUES (?, ?, ?, ?)",
        clients,
    )

    # 4. Insertion des transactions en nombre suffisant (pour faire de la Data Viz)
    # Client 1 : Jean Dupont (Un compte classique)
    # Client 2 : Clemence Ait (Budget étudiant, beaucoup de petits achats)
    transactions = [
        # Transactions pour Jean Dupont (client_id = 1)
        (1, "2026-06-01", "Salaire BNPP", 2500.00, "Revenus"),
        (1, "2026-06-03", "Loyer mensuel", -850.00, "Logement"),
        (1, "2026-06-05", "Courses Supermarché", -120.50, "Alimentation"),
        (1, "2026-06-10", "Abonnement Streaming", -15.99, "Loisirs"),
        (1, "2026-06-15", "Restaurant entre amis", -63.00, "Alimentation"),
        # Transactions pour Clemence Ait (client_id = 2)
        (2, "2026-06-01", "Virement Parents", 400.00, "Revenus"),
        (2, "2026-06-02", "Librairie Universitaire (Livres Droit)", -85.00, "Études"),
        (2, "2026-06-04", "Boulangerie", -4.50, "Alimentation"),
        (2, "2026-06-08", "Inscription Certification Allemand B2", -120.00, "Études"),
        (2, "2026-06-12", "Fast Food", -15.50, "Alimentation"),
        (2, "2026-06-18", "Cafétéria Campus", -10.00, "Alimentation"),
        (2, "2026-06-20", "Cinéma", -15.00, "Loisirs"),
        # Transactions pour Data Forensic (client_id = 3)
        (3, "2026-06-01", "Solde Initial", 10000.00, "Revenus"),
        (3, "2026-06-12", "Achat Matériel Soudure / Métaux", -650.00, "Atelier"),
        (3, "2026-06-14", "Billetterie Théâtre Local", -45.00, "Culture"),
        (3, "2026-06-19", "Garage - Réparation Durite Auto", -405.00, "Transport"),
    ]

    cursor.executemany(
        "INSERT INTO transactions (client_id, date, description, montant, categorie) VALUES (?, ?, ?, ?, ?)",
        transactions,
    )

    # Sauvegarde et fermeture
    conn.commit()
    conn.close()

    print(
        f"🎉 Base de données SQLite initialisée avec succès ! (Fichier créé dans {DB_PATH})"
    )


if __name__ == "__main__":
    init_db()