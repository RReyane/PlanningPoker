"""
@file main.py
@author Reyane Redjem
@brief Application de planning Poker 

"""

import pygame
import sys
from UIobjects import Button, InputBox

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

def Parametres():
   input_box = InputBox(45,80,300,60,get_font(40))
   liste_joueur = []
   while True:
      param_MousePos = pygame.mouse.get_pos()

      Fenetre.fill("#4d4a52")

      input_text_box = get_font(40).render("Nom joueur:", True, "#f8d4fc")
      input_text_box_rect = input_text_box.get_rect(center = (150,50))
      Fenetre.blit(input_text_box,input_text_box_rect)

      listeJoueur_Text = get_font(40).render("Liste joueurs:", True, "#f8d4fc")
      listeJoueur_Text_Rect = input_text_box.get_rect(center = (Fenetre.get_width() //2 + 15,50))
      Fenetre.blit(listeJoueur_Text,listeJoueur_Text_Rect)

      input_box.update(Fenetre)

      input_box_button = Button(pos=(380, 115), text_input="Ok", font=get_font(40), base_color="#f8d4fc", hovering_color="#bb7ec2")
      input_box_button.changeColor(param_MousePos)
      input_box_button.update(Fenetre)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box_button.checkForInput(param_MousePos):
               new_text_surface = get_font(40).render(input_box.text, True, "#f8d4fc")
               liste_joueur.append(new_text_surface)
               input_box.text = ''
               input_box.update(Fenetre)
         input_box.handle_event(event,param_MousePos)


      x_pos = Fenetre.get_width() //2 
      y_pos = 115
      for Joueur in liste_joueur:
         Fenetre.blit(Joueur,(x_pos, y_pos))
         x_pos +=Joueur.get_width()+20
         if x_pos > (Fenetre.get_width()//6)*5:
            x_pos = Fenetre.get_width() //2 
            y_pos += Joueur.get_height() + 10

      pygame.display.flip()



def Charger():
   print()

def menuPrincipale():
   """! Boucle du menu principale au lancement du programme."""

   while True:
      Fenetre.fill("#4d4a52")

      Text_menu = get_font(90).render("Planning Poker !", True, "#d9c7c7")
      Text_menu_rect = Text_menu.get_rect(center = (Fenetre.get_width()//2,50))

      Fenetre.blit(Text_menu,Text_menu_rect)

      Play_button = Button(pos=(Fenetre.get_width()//2, Fenetre.get_height()//2-60), text_input="Jouer", font=get_font(70), base_color="#f8d4fc", hovering_color="#bb7ec2")
      Continue_button = Button(pos=(Fenetre.get_width()//2, Fenetre.get_height()//2+60), text_input="Continuer", font=get_font(70), base_color="#f8d4fc", hovering_color="#bb7ec2")

      Menu_MousePos = pygame.mouse.get_pos()

      for button in [Play_button, Continue_button]:
            button.changeColor(Menu_MousePos)
            button.update(Fenetre)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if Play_button.checkForInput(Menu_MousePos):
               Parametres()
            if Continue_button.checkForInput(Menu_MousePos):
               Charger()
   
      pygame.display.flip()

menuPrincipale()