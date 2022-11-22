import socket
import threading


def envoyer(message):
    # pour envoyer les messages a tous les clients
    for user in users:
        user.send(message)


def ecrire(user):
    while True:
        try:
            # pour recevoir les messages du client
            message = user.recv(1024)
            # pour les renvoyer au client
            envoyer(message)
        except:
            # si il y a une coupeur de la connexion
            # pour supprimer le connexion du tableau
            index = users.index(user)
            users.remove(user)

            # pour fermer la socket
            user.close()

            # pour envoyer au client le message d'erreur
            pseudo = pseudos[index]
            envoyer('{} left!'.format(pseudo).encode('ascii'))

            # pour supprimer le pseudo du client du tableau
            pseudos.remove(pseudo)
            break


def connection():
    while True:
        # dequ'on lance le programme utilisateur
        # la connextion est établie
        user, address = server.accept()
        print("user connectée est :  ")

        # le serveur envoie "ps" au client pour demander le pseudo
        user.send('ps'.encode('ascii'))

        # le serveur recoit par le client son pseudo
        pseudo = user.recv(1024).decode('ascii')

        # pour mettre le pseudo deans le tableau dse pseudos
        pseudos.append(pseudo)
        users.append(user)

        # pour afficher le pseudo du client
        print(f"{pseudo}")

        # pour les envoyer au client
        envoyer(f"{pseudo} joined!".encode('ascii'))
        user.send('Connected to server!'.encode('ascii'))

        # pour lancer la fonction ecrire
        thread = threading.Thread(target=ecrire, args=(user,))
        thread.start()


# pour les data de la connexion
host = '127.0.0.1'
port = 5010

# pour déclarer les deux tableaux
users = []
pseudos = []

# pour la création de la socket &
# pour la connextion au serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# pour dire que le serveur est en écoute
print("serveur est en ecoute")

# pour lancer la fonction connection
connection()
