import tkinter as tk


def create_new_game():
   print("Nouvelle partie")

def resume_game():
   print("Reprendre une partie")


# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Planning Poker")
x = int((fenetre.winfo_screenwidth()/2) - 400)
fenetre.geometry("800x800+{}+0".format(x))

# Créer une étiquette pour afficher le message de bienvenue
message = tk.Label(fenetre, text="Bienvenue dans Planning Poker !",bg="black",fg="white", height= 3,width=50, font=("Courrier", 18))
message.pack(pady=100)

new_game_button = tk.Button(fenetre, text="Nouvelle partie", command=create_new_game,width=30, height=10, bg='orange')
new_game_button.pack(side="left",expand=True)

resume_game_button = tk.Button(fenetre, text="Reprendre une partie", command=resume_game,width=30, height=10, bg='orange')
resume_game_button.pack(side="left",expand=True)

# Lancer la boucle principale de Tkinter
fenetre.mainloop()