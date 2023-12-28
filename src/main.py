"""
@file main.py
@author Reyane Redjem
@brief Application de planning Poker 

"""

import pygame
import json
import sys
from UIobjects import Button, InputBox, DropDown
from Entities import Joueur as player, Cartes

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

def lireBacklog():
   """
    Lit les données du fichier JSON du backlog.

    Returns:
      @return list  Liste contenant les informations de chaque élément du backlog.
    """
   #Lire le json
   with open('./json/backlog.json', 'r') as file:
      data = json.load(file)

   # Liste pour stocker les informations de chaque élément du backlog
   backlog_items = []
    
    # Parcours de chaque élément du backlog
   for item in data['backlog']:
      # Stockage des informations dans un dictionnaire
      backlog_item = {
         "id": item['id'],
         "feature": item['feature'],
         "description": item['description']
      }
         
      # Ajout du dictionnaire à la liste
      backlog_items.append(backlog_item)
        
   return backlog_items

def saveJson(backlog_items,listeJoueurs,typeJeu,indexFeature,votes):
   """
   Sauvegarde les données du planning poker dans un fichier JSON.

   Args:
   @param backlog_items (list): Liste contenant les informations de chaque élément du backlog.
   @param listeJoueurs (list): Liste des joueurs participant au planning poker.
   @param typeJeu (int): Type de jeu (0: strict, 1: moyenne, 2: majorité relative).
   @param indexFeature (int): Indice de la fonctionnalité courante dans le backlog.
   @param votes (list): Liste des votes attribués à chaque fonctionnalité.
    """
   
   data = {}

   match typeJeu:
      case 0:
         typeJeu = 'strict'
      case 1:
         typeJeu = 'moyenne'
      case 2:
         typeJeu = 'majoriteRelative'
   data['PlanningPoker'] = {
       'type': typeJeu,
       'joueurs': [joueur.nom for joueur in listeJoueurs],
       'IndexFeatureCourante': indexFeature if indexFeature < len(backlog_items) else 'Fini'
   }

   data['backlog'] = []
   for i,item in enumerate(backlog_items):
       # Créer un nouveau dictionnaire pour chaque item
      if i < indexFeature:
         backlog_item = {
            'id': item['id'],
            'feature': item['feature'],
            'description': item['description'],
            'Difficulte': votes[i]
         }
      else:
         backlog_item = {
            'id': item['id'],
            'feature': item['feature'],
            'description': item['description']
         }

       # Ajouter le dictionnaire à la liste 'backlog'
      data['backlog'].append(backlog_item)
   
   # Sauvegarder l'objet JSON dans un fichier
   with open('./json/sauvegardePlanningPoker.json', 'w') as file:
       json.dump(data, file, indent=4)

def Parametres():
   """
   Fonction gérant la fenêtre des paramètres du jeu.

   Returns:
   @return None
    """
   
   input_box = InputBox(45,80,300,60,get_font(40))
   liste_joueur = []
   dropDown_typeJeu = DropDown(45,335,300,60,get_font(40),"Choisir mode",["strict","moyenne","majoriteRelat"])

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
      

      dropdown_typeJeu_Text = get_font(40).render("Regle du poker:", True, "#f8d4fc")
      dropdown_typeJeu_Text_rect = input_text_box.get_rect(center = (150,300))
      Fenetre.blit(dropdown_typeJeu_Text,dropdown_typeJeu_Text_rect)

      dropDown_typeJeu.update(Fenetre)

      LancerPartie_Button = Button((400,(Fenetre.get_height()//4)*3),"Lancer partie",get_font(60),"#ed402d","#a61808")

      for button in [input_box_button,LancerPartie_Button]:
         button.changeColor(param_MousePos)
         button.update(Fenetre)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         input_box.handle_event(event,param_MousePos)
         selected_option = dropDown_typeJeu.handle_event(event,param_MousePos)
         if selected_option >= 0:
            dropDown_typeJeu.texteDefaut = dropDown_typeJeu.Listeoptions[selected_option]
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box_button.checkForInput(param_MousePos):
               if input_box.text != '':
                  liste_joueur.append(input_box.text)
                  input_box.text = ''
               input_box.update(Fenetre)
            if LancerPartie_Button.checkForInput(param_MousePos):
               if len(liste_joueur) >= 2 and dropDown_typeJeu.option_choisie >=0:
                  Game(liste_joueur,dropDown_typeJeu.option_choisie)

      x_pos = Fenetre.get_width() //2 
      y_pos = 115
      for Joueur in liste_joueur:
         new_text_surface = get_font(40).render(Joueur, True, "#f8d4fc")
         Fenetre.blit(new_text_surface,(x_pos, y_pos))
         x_pos +=new_text_surface.get_width()+20
         if x_pos > (Fenetre.get_width()//6)*5:
            x_pos = Fenetre.get_width() //2 
            y_pos += new_text_surface.get_height() + 10

      pygame.display.flip()

def Charger():
   """
   Charge les données d'une sauvegarde du planning poker depuis un fichier JSON.

   Returns:
   @return None
    """
   
   with open('./json/sauvegardePlanningPoker.json', 'r') as file:
      data = json.load(file)

   typeJeu = data['PlanningPoker']['type']
   match typeJeu:
      case 'strict':
         typeJeu = 0
      case 'moyenne':
         typeJeu = 1
      case 'majoriteRelative':
         typeJeu = 2
   joueurs = data['PlanningPoker']['joueurs']
   indexFeature = data['PlanningPoker']['IndexFeatureCourante']
   backlog_items = data['backlog']
   votes = []
   for i, item in enumerate(backlog_items):
      if i < indexFeature:
         votes.append(item['Difficulte'])

   Game(joueurs,typeJeu,indexFeature,votes,backlog_items)

def Game(Joueurs, TypeJeu, activeTask=0,listeVoteChoisie = [],backlog=None):
   """
   Fonction principale gérant le déroulement du jeu.

   Args:
   @param Joueurs (list): Liste des noms des joueurs.
   @param TypeJeu (int): Type de jeu (0: strict, 1: moyenne, 2: majorité relative).
   @param activeTask (int): Indice de la tâche actuelle dans le backlog.
   @param listeVoteChoisie (list): Liste des votes attribués à chaque tâche.
   @param backlog (list): Liste des tâches à évaluer.

   Returns:
   @return None
   """
   
   ListeObjJoueurs= []
   for joueur in Joueurs:
      ListeObjJoueurs.append(player(joueur))

   listeCartes = Cartes(100,150)

   tour = 1
   
   if backlog == None:
      backlog = lireBacklog()
   maxTask = len(backlog)
   activeJoueurNb = 0

   while True:
      Fenetre.fill("#4d4a52")

      if activeJoueurNb >= len(ListeObjJoueurs):
         if tour !=1:
            egal = True
            carteComparaison = 11
            for j in ListeObjJoueurs:
                  if j.carteChoisie != carteComparaison:
                     egal = False
            if egal == True:
               saveJson(backlog,ListeObjJoueurs,TypeJeu,activeTask,listeVoteChoisie)
               pygame.quit()
               sys.exit()
         if tour == 1:
            Discussion(ListeObjJoueurs,True)
            activeJoueurNb=0
            tour +=1
         elif TypeJeu == 0: #typeJeu = strict
            egal = True
            carteComparaison = ListeObjJoueurs[0].carteChoisie
            for j in ListeObjJoueurs:
               if j.carteChoisie != carteComparaison:
                  egal = False
            if egal == False:
               Discussion(ListeObjJoueurs)
               activeJoueurNb=0
               tour+=1
            else:
               listeVoteChoisie.append(ListeObjJoueurs[0].cartes[carteComparaison])
               activeJoueurNb=0
               tour = 1
               activeTask +=1
         elif TypeJeu ==1: #typeJeu = moyenne
            moyenne = 0
            for j in ListeObjJoueurs:
               if j.cartes[j.carteChoisie] >=0:
                  moyenne += j.cartes[j.carteChoisie]
            moyenne /= len(ListeObjJoueurs)+1
            listeVoteChoisie.append(moyenne)
            activeJoueurNb=0
            tour = 1
            activeTask +=1
         elif TypeJeu ==2: #typeJeu = majorité Absolue
            cpt_vote = {}
            for j in ListeObjJoueurs:
               if j.cartes[j.carteChoisie]>=0:
                  if j.cartes[j.carteChoisie] in cpt_vote:
                     cpt_vote[j.cartes[j.carteChoisie]] +=1
                  else:
                     cpt_vote[j.cartes[j.carteChoisie]] = 1
            
            majorite = False
            chosenCard = None
            for c,cpt in cpt_vote.items():
               if cpt >= len(ListeObjJoueurs)//2 +1:
                  majorite = True
                  chosenCard = c
            
            if majorite:
               listeVoteChoisie.append(chosenCard)
               activeJoueurNb=0
               tour = 1
               activeTask +=1
            else:
               Discussion(ListeObjJoueurs)
               activeJoueurNb=0
               tour+=1

      if activeTask >= maxTask:
         saveJson(backlog,ListeObjJoueurs,TypeJeu,activeTask,listeVoteChoisie)
         pygame.quit()
         sys.exit()

      cpt_Tour = get_font(70).render("Tour " + str(tour), True, "#d9c7c7")
      cpt_Tour_rect = cpt_Tour.get_rect(center = (Fenetre.get_width()//2,50))
      Fenetre.blit(cpt_Tour,cpt_Tour_rect)

      Tache = get_font(30).render(backlog[activeTask]['feature'], True, "#d9c7c7")
      Tache_rect = Tache.get_rect(topleft = (20,Fenetre.get_height()//8))
      Fenetre.blit(Tache,Tache_rect)

      Tache_desc = get_font(20).render(backlog[activeTask]['description'], True, "#d9c7c7")
      Tache_desc_rect = Tache_desc.get_rect(topleft = (20,Fenetre.get_height()//8 + 40))
      Fenetre.blit(Tache_desc,Tache_desc_rect)
      
      Joueur_votant = get_font(50).render(ListeObjJoueurs[activeJoueurNb].nom,True,"#6e1713")
      Joueur_votant_rect = Joueur_votant.get_rect(center = (Fenetre.get_width()//2,Fenetre.get_height()//2))
      Fenetre.blit(Joueur_votant,Joueur_votant_rect)

      offset =0
      for c in listeCartes.sprites:
         listeCartes.renderSprite(Fenetre,listeCartes.sprites[c],(Fenetre.get_width()//25)+offset,(Fenetre.get_height()//4)*3)
         offset+= 120


      Game_MousePos = pygame.mouse.get_pos()

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.MOUSEBUTTONDOWN:
            offset = 0
            for nCarte,_ in enumerate(listeCartes.sprites):
               if listeCartes.surfaces[nCarte].get_rect(topleft = (Fenetre.get_width()//25 +offset,(Fenetre.get_height()//4)*3)).collidepoint(Game_MousePos):
                  ListeObjJoueurs[activeJoueurNb].carteChoisie = nCarte
                  activeJoueurNb+=1
               offset+=120
               

      pygame.display.flip()

def Discussion(listeJoueur,tour1=False):
   """
   Affiche l'écran de discussion où les joueurs peuvent discuter de leurs choix de cartes.

   Args:
   @param listeJoueur (list): Liste des joueurs participant à la discussion.
   @param tour1 (bool): Indique si c'est le tour 1 ou non.

   Returns:
   @return None
    """
   Discute = True
   dict_carte = {0:'0',1:'1',2:'2',3:'3',4:'5',5:'8',6:'13',7:'20',8:'40',9:'100',10:'?'}
   while Discute:
      Fenetre.fill("#4d4a52")
      
      if not tour1:
         cartePlus = 0
         carteMoins = 10
         for joueur in listeJoueur:
            if joueur.carteChoisie != 11:
               if joueur.carteChoisie < carteMoins:
                  carteMoins = joueur.carteChoisie
               if joueur.carteChoisie> cartePlus:
                  cartePlus = joueur.carteChoisie

         texte_carte_plus = get_font(60).render("La plus grande carte est "+ dict_carte[cartePlus], True, "#d9c7c7")
         texte_carte_plus_rect = texte_carte_plus.get_rect(center = (Fenetre.get_width()//2,(Fenetre.get_height()//4)*1))
         Fenetre.blit(texte_carte_plus,texte_carte_plus_rect)

         texte_carte_moins = get_font(60).render("La plus petite carte est " + dict_carte[carteMoins], True, "#d9c7c7")
         texte_carte_moins_rect = texte_carte_moins.get_rect(center = (Fenetre.get_width()//2,(Fenetre.get_height()//4)*2))
         Fenetre.blit(texte_carte_moins,texte_carte_moins_rect)
      else:
         texte_T1 = get_font(90).render("C'est le tour 1, discuter !", True, "#d9c7c7")
         texte_T1_rect = texte_T1.get_rect(center = (Fenetre.get_width()//2,Fenetre.get_height()//2))
         Fenetre.blit(texte_T1,texte_T1_rect)

      finDiscussion_button = Button(pos=(Fenetre.get_width()//2, (Fenetre.get_height()//4)*3), text_input="Fin", font=get_font(70), base_color="#f8d4fc", hovering_color="#bb7ec2")
      
      Dsicussion_MousePos = pygame.mouse.get_pos()

      finDiscussion_button.changeColor(Dsicussion_MousePos)
      finDiscussion_button.update(Fenetre)
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if finDiscussion_button.checkForInput(Dsicussion_MousePos):
               Discute = False

      pygame.display.flip()

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