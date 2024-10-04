import sqlite3
from datetime import datetime

# Connexion à la base de données SQLite (création du fichier clients.db si non existant)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Insertion de données dans la table Clients
clients_data = [
    ('JAMIRI', 'Saad', 'saad.jamiri@example.com', '2024-10-01'),
    ('PATOCHE', 'Maitre', 'maitre.patoche@example.com', '2024-10-02'),
    ('BADJI', 'Khadija', 'khadija.badji@example.com', '2024-10-03')
]

cursor.executemany('''
    INSERT INTO Clients (nom, prenom, email, date_inscription) 
    VALUES (?, ?, ?, ?)
''', clients_data)

# Validation des changements après l'insertion des clients
conn.commit()

# Récupérer les ids des clients insérés pour les utiliser dans les commandes
cursor.execute('SELECT id FROM Clients WHERE email=?', ('saad.jamiri@example.com',))
client1_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM Clients WHERE email=?', ('maitre.patoche@example.com',))
client2_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM Clients WHERE email=?', ('khadija.badji@example.com',))
client3_id = cursor.fetchone()[0]

# Insertion de données dans la table Commandes
commandes_data = [
    (client1_id, 'Ordinateur portable', datetime.now().strftime('%Y-%m-%d')),
    (client2_id, 'Smartphone', datetime.now().strftime('%Y-%m-%d')),
    (client3_id, 'Tablette', datetime.now().strftime('%Y-%m-%d'))
]

cursor.executemany('''
    INSERT INTO Commandes (client_id, produit, date_commande)
    VALUES (?, ?, ?)
''', commandes_data)

# Validation des changements après l'insertion des commandes
conn.commit()

# Fermeture de la connexion
conn.close()

print("Données insérées dans les tables Clients et Commandes avec succès.")
