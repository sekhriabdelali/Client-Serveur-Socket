import socket
import threading
from tkinter import *

# pour la création de la socket
# pour la connextion au serveur
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(('127.0.0.1', 5010))


# pour les fonctions

def recevoir():
    while True:
        try:
            # pour recevoir les messages envoyés par le client
            message = user.recv(1024).decode('ascii')

            # si le message == "ps" ==> le serveur demande le pseudo du client
            if message == 'ps':
                # le client envoie son pseudo au serveur
                user.send(userup.cget("text").encode('ascii'))
            # sinon
            else:
                # le client enregistre les messages envoyés par le serveur
                listmessage.insert(END, message)
        except:
            # pour fermer la socket
            user.close()
            break


def ecrire():
    # pour archiver le pseudo et le message
    message = '{}: {}'.format(userup.cget("text"), entry.get())
    print(message)
    # pour encoder le message et l'envoyer à la socket "user"
    user.send(message.encode('ascii'))
    # pour supprimer la valeur de entry
    entry.delete(0, END)


def get_user():
    username = entry.get()
    if(username != ''):
        # pour changer les champs
        userup.config(text=username)
        btn.config(text='Envoyer', command=ecrire)
        label.config(text='Saisir votre Message :')
        entry.config(width=50)
        # pour supprimer la valeur de entry
        entry.delete(0, END)
        # pour lancer la fonction recevoir()
        receive_thread = threading.Thread(target=recevoir)
        receive_thread.start()


fenetre = Tk()

# des info sur la fenetre
fenetre.title("CHAT")
fenetre.geometry('1000x700')
fenetre.resizable(False, False)
title = Label(fenetre, text='My CHAT', fg='black', bg='#f5f0e1')
title.config(font=('times', 20, 'bold'))
title.pack(fill=X)

# label "userup" pour écrire le nom
userup = Label(fenetre, text=' ', fg='black')
userup.config(font=('times', 20, 'bold'))
userup.place(x=10, y=0)

# frame "userframe" pour le saisie et les bouttons
userframe = Frame(fenetre)
userframe.pack(pady=10)

# label "lablframe" dans la frame "userframe" pour la saisie et les bouttons
lablframe = Label(userframe, text='', fg='white',
                  bg='#e1f0f5', width=1000, height=8)
lablframe.pack()

# label "label" dans "userframe" pour saisir le pseudo
label = Label(userframe, text='Saisir votre pseudo :',
              fg='black', bg="#e1f0f5")
label.config(font=('times', 14, 'bold'))
label.place(x=20, y=40)

# entry "entry" dans "userframe" pour entrer ...
entry = Entry(userframe, width=30, fg='#008B8B', bg='white')
entry.config(font=('times', 14, 'bold'))
entry.place(x=250, y=40)

# button "btn"
btn = Button(userframe, text='confirmer',
             command=get_user, bg='#1e3d59', fg='white')
btn.config(font=('times', 14, 'bold'))
btn.place(x=800, y=35)

# une autre frame "messageframe"
messageframe = Frame(fenetre)
messageframe.pack()

# scrollbar
scroll = Scrollbar(messageframe, orient=VERTICAL)

# listbox "listmessage" pour afficher les messages
listmessage = Listbox(messageframe, width=1000, height=30,
                      bg='#F0FFFF', yscrollcommand=scroll.set)
listmessage.pack()

# config scroll
scroll.config(command=listmessage.yview)
scroll.pack(side=RIGHT, fill=Y)


fenetre.mainloop()
