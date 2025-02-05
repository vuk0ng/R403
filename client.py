import socket
import sys

# Informations du serveur
TCP_IP = '10.0.0.5'
TCP_PORT = 2001
MESSAGE_TO_SERVER = "Bonjour, je suis le client"

# Création du socket
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket créé avec succès")
except socket.error:
    sys.exit()

# Connexion au serveur
client_socket.connect((TCP_IP, TCP_PORT))

# Envoi de données
try:
    client_socket.send(MESSAGE_TO_SERVER.encode('utf-8'))
except socket.error:
    sys.exit()

# Affichage du message envoyé
print("Message envoyé avec succès")

# Réception de données
data = client_socket.recv(1024)

# Fermeture du socket
client_socket.close()

# Affichage du message reçu
print("Message reçu: ", data.decode('utf-8'))