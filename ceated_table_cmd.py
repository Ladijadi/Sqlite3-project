import sqlite3

# Connexion à la base de données SQLite (création du fichier clients.db si non existant)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Création de la table Clients (si elle n'existe pas encore)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        date_inscription TEXT NOT NULL
    )
''')

# Création de la table Commandes avec client_id comme clé étrangère
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Commandes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        produit TEXT NOT NULL,
        date_commande TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES Clients(id)
    )
''')

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()

print("Table 'Commandes' créée avec succès.")
