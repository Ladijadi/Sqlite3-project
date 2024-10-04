import sqlite3

# Connexion à la base de données SQLite (création du fichier clients.db si non existant)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Création de la table Clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        date_inscription TEXT NOT NULL
    )
''')

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()

print("Table 'Clients' créée avec succès.")
