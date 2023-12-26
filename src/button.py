class Button():
    """
    @class Représente un bouton graphique avec la possibilité de changement de couleur au survol.

    Attributes:
        x_pos (int): La position horizontale du bouton.
        y_pos (int): La position verticale du bouton.
        font (pygame.font.Font): La police d'écriture utilisée pour le texte du bouton.
        base_color (str): La couleur du texte lorsque le bouton n'est pas survolé.
        hovering_color (str): La couleur du texte lorsque le bouton est survolé.
        text_input (str): Le texte à afficher sur le bouton.
        text (pygame.Surface): La surface représentant le texte rendu avec la police et la couleur actuelles.
        rect (pygame.Rect): Le rectangle entourant le texte, utilisé pour les collisions et le positionnement.
    """
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        """! Initialise un objet Button.

        Args:
        @param pos (tuple): La position du bouton (x, y).
        @param text_input (str): Le texte à afficher sur le bouton.
        @param font (pygame.font.Font): La police d'écriture à utiliser.
        @param base_color (str): La couleur du texte lorsque le bouton n'est pas survolé.
        @param hovering_color (str): La couleur du texte lorsque le bouton est survolé.
        """
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """! Met à jour l'affichage du bouton sur l'écran.

        @param screen (pygame.Surface): La surface d'affichage sur laquelle dessiner le bouton.
        """
        screen.blit(self.text, self.rect)

    def checkForInput(self, position):
        """! Vérifie si la position donnée est à l'intérieur des limites du bouton.

        @param position La position à vérifier (x, y).

        @return True si la position est à l'intérieur du bouton, False sinon.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        """! Change la couleur du texte en fonction de la position donnée.

        @param position La position de la souris.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)