import pygame

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.cartes = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, -1, -2]
        self.carteChoisie = None
        

class Cartes:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.surfaces = []
        self.sprites = {"0":"./assets/cartes/png/cartes_0.png", "1":"./assets/cartes/png/cartes_1.png", "2":"./assets/cartes/png/cartes_2.png", 
                        "3":"./assets/cartes/png/cartes_3.png", "5":"./assets/cartes/png/cartes_5.png", "8":"./assets/cartes/png/cartes_8.png", 
                        "13":"./assets/cartes/png/cartes_13.png", "20":"./assets/cartes/png/cartes_20.png", "40":"./assets/cartes/png/cartes_40.png",
                        "100":"./assets/cartes/png/cartes_100.png", "?":"./assets/cartes/png/cartes_interro.png", "cafe":"./assets/cartes/png/cartes_cafe.png"}
        
    def renderSprite(self,fenetre, spritePath, x,y):
        sprite = pygame.image.load(spritePath)
        surf = pygame.transform.scale(sprite,(self.width,self.height))
        self.surfaces.append(surf)
        fenetre.blit(surf,(x,y))
        