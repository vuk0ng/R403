import socket
import sys

# Paramètres de connexion
TCP_IP_srv = '10.0.0.5'
TCP_PORT = 2000
confirmation_msg = 'Connexion réssie : message bien reçu'

# Création du socket
try:
    # Création d'un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Une erreur s'est produite lors de la création du socket")
    sys.exit()

# Liaison du socket à l'adresse et au port
server_socket.bind((TCP_IP_srv, TCP_PORT))

# Mise en écoute du socket
server_socket.listen(3)
print("En écoute ...")

while True:
    connexion, adresse = server_socket.accept()

    print('Connecté avec :', adresse)
    data = connexion.recv(1024)
    print("Message reçu :", data)

    # Envoi d'un message de confirmation
    connexion.send(data)

    # Fermeture de la connexion
    connexion.close()
