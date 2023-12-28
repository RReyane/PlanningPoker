import pygame

class Joueur:
    """
    @class Représente un joueur participant à un jeu de cartes.

    Attributes:
        nom (str): Le nom du joueur.
        cartes (list): La liste des valeurs des cartes que le joueur peut choisir.
        carteChoisie (int): La valeur de la carte choisie par le joueur.
    """
    def __init__(self, nom):
        """
        Initialise un objet Joueur.

        Args:
        @param nom (str): Le nom du joueur.
        """
        self.nom = nom
        self.cartes = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, -1, -2]
        self.carteChoisie = None
        

class Cartes:
    """
    @class Représente un ensemble de cartes avec des images associées.

    Attributes:
        width (int): La largeur souhaitée des images des cartes.
        height (int): La hauteur souhaitée des images des cartes.
        surfaces (list): La liste des surfaces des images des cartes rendues.
        sprites (dict): Le dictionnaire associant les valeurs des cartes à leurs chemins d'image.
    """
    def __init__(self, w, h):
        """
        Initialise un objet Cartes.

        Args:
        @param w (int): La largeur souhaitée des images des cartes.
        @param h (int): La hauteur souhaitée des images des cartes.
        """
        self.width = w
        self.height = h
        self.surfaces = []
        self.sprites = {"0":"./assets/cartes/png/cartes_0.png", "1":"./assets/cartes/png/cartes_1.png", "2":"./assets/cartes/png/cartes_2.png", 
                        "3":"./assets/cartes/png/cartes_3.png", "5":"./assets/cartes/png/cartes_5.png", "8":"./assets/cartes/png/cartes_8.png", 
                        "13":"./assets/cartes/png/cartes_13.png", "20":"./assets/cartes/png/cartes_20.png", "40":"./assets/cartes/png/cartes_40.png",
                        "100":"./assets/cartes/png/cartes_100.png", "?":"./assets/cartes/png/cartes_interro.png", "cafe":"./assets/cartes/png/cartes_cafe.png"}
        
    def renderSprite(self,fenetre, spritePath, x,y):
        """
        Affiche une carte sur la fenêtre du jeu.

        Args:
        @param fenetre (pygame.Surface): La surface d'affichage du jeu.
        @param spritePath (str): Le chemin d'accès à l'image de la carte.
        @param x (int): La position horizontale de l'image de la carte sur la fenêtre.
        @param y (int): La position verticale de l'image de la carte sur la fenêtre.
        """
        sprite = pygame.image.load(spritePath)
        surf = pygame.transform.scale(sprite,(self.width,self.height))
        self.surfaces.append(surf)
        fenetre.blit(surf,(x,y))
        