from tkinter import Tk, Label

# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Planning Poker")
x = int((fenetre.winfo_screenwidth()/2) - 400)
fenetre.geometry("800x800+{}+0".format(x))

# Créer une étiquette pour afficher le message de bienvenue
message = Label(fenetre, text="Bienvenue dans Planning Poker !",bg="black",fg="white")
message.pack()

# Lancer la boucle principale de Tkinter
fenetre.mainloop()