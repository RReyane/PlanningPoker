"""
@file main.py
@author Reyane Redjem
@brief Application de planning Poker 

"""

import pygame
import sys
from button import Button

pygame.init()

## @var contient les information de l'ecran 
screen_info = pygame.display.Info()
## @var La fenetre du programme
Fenetre = pygame.display.set_mode((int(screen_info.current_w * 0.8), int(screen_info.current_h * 0.8)))

def get_font(taille): 
   """! Donne la police avec la taille entrée en parametre.

   @param taille  Taille de la police 
   
   @return La police avec la bonne taille
   """
   return pygame.font.Font("assets/font/Browood-Regular.ttf", taille)

def menuPrincipale():
   """! Boucle du menu principale au lancement du programme."""

   while True:
      Fenetre.fill("#4d4a52")

      Text_menu = get_font(90).render("Planning Poker !", True, "#d9c7c7")
      Text_menu_rect = Text_menu.get_rect(center = (Fenetre.get_width()//2,50))

      Play_button = Button(pos=(Fenetre.get_width()//2, Fenetre.get_height()//2-60), text_input="Jouer", font=get_font(70), base_color="#f8d4fc", hovering_color="#bb7ec2")
      Continue_button = Button(pos=(Fenetre.get_width()//2, Fenetre.get_height()//2+60), text_input="Continuer", font=get_font(70), base_color="#f8d4fc", hovering_color="#bb7ec2")

      Fenetre.blit(Text_menu,Text_menu_rect)

      MousePos = pygame.mouse.get_pos()

      for button in [Play_button, Continue_button]:
            button.changeColor(MousePos)
            button.update(Fenetre)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if Play_button.checkForInput(MousePos):
               print('Button 1 clicked')
            if Continue_button.checkForInput(MousePos):
               print('Button 2 clicked')
   
      pygame.display.flip()

menuPrincipale()