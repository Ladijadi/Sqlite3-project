import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# a) Sélectionner tous les clients
def get_all_clients():
    cursor.execute('SELECT * FROM Clients')
    clients = cursor.fetchall()
    for client in clients:
        print(client)

# b) Récupérer les commandes d'un client spécifique
def get_orders_by_client(client_id):
    cursor.execute('SELECT * FROM Commandes WHERE client_id = ?', (client_id,))
    orders = cursor.fetchall()
    if orders:
        print(f"Commandes du client {client_id}:")
        for order in orders:
            print(order)
    else:
        print(f"Aucune commande trouvée pour le client {client_id}")

# c) Mettre à jour l'adresse e-mail d'un client
def update_client_email(client_id, new_email):
    cursor.execute('UPDATE Clients SET email = ? WHERE id = ?', (new_email, client_id))
    conn.commit()
    print(f"Email du client {client_id} mis à jour avec succès.")

# d) Supprimer une commande
def delete_order(order_id):
    cursor.execute('DELETE FROM Commandes WHERE id = ?', (order_id,))
    conn.commit()
    print(f"Commande {order_id} supprimée avec succès.")

# Appel des fonctions (modifie les valeurs selon tes besoins)
get_all_clients()                # Affiche tous les clients
get_orders_by_client(1)          # Récupère les commandes du client avec id = 1
update_client_email(1, 'new.email@example.com')  # Met à jour l'email du client avec id = 1
delete_order(1)                  # Supprime la commande avec id = 1

# Fermeture de la connexion
conn.close()
