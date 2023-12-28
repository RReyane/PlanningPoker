import pygame

class Button:
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


class InputBox:

    def __init__(self, x, y, w, h, font, text=''):
        self.originalW = w
        self.rect = pygame.Rect(x, y, w, h)
        self.color = "gray"
        self.font = font
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, posMouse):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(posMouse):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                


    def update(self, screen):
        # Re-render the text.
        self.txt_surface = self.font.render(self.text, True, "black")
        # Resize the box if the text is too long.
        width = max(self.originalW, self.txt_surface.get_width()+10)
        self.rect.w = width
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 0)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))


class DropDown:
    def __init__(self, x, y, w, h, font, defaut, options):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.texteDefaut = defaut
        self.Listeoptions = options
        self.draw_menu = False
        self.menu_active = False
        self.option_active = -1

    def update(self, fenetre):
        pygame.draw.rect(fenetre, "gray", self.rect, 0)
        msg = self.font.render(self.texteDefaut, True, "black")
        fenetre.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.Listeoptions):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(fenetre, "white", rect, 0)
                msg = self.font.render(text, 1, "black")
                fenetre.blit(msg, msg.get_rect(center = rect.center))
    
    def handle_event(self, event, posMouse):
        self.menu_active = self.rect.collidepoint(posMouse)
        
        for i in range(len(self.Listeoptions)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(posMouse):
                self.option_active = i
                break

        if not self.menu_active and self.option_active == -1:
            self.draw_menu = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.menu_active:
                self.draw_menu = not self.draw_menu
            elif self.draw_menu and self.option_active >= 0:
                self.draw_menu = False
                return self.option_active
        return -1