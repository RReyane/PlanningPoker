import pygame

pygame.init()

screen_info = pygame.display.Info()
width = int(screen_info.current_w * 0.8)
height = int(screen_info.current_h * 0.8)
ECRAN = pygame.display.set_mode((width, height))

def get_font(taille): 
    return pygame.font.Font("assets/font/Browood-Regular.ttf", taille)

def menuPrincipale():
   while True:
      ECRAN.fill("#4d4a52")

      TEXT_MENU = get_font(80).render("Planning Poker !", True, "#d9c7c7")
      TEXT_MENU_RECT = TEXT_MENU.get_rect(center = (width//2,50))


      ECRAN.blit(TEXT_MENU,TEXT_MENU_RECT)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
      pygame.display.flip()

menuPrincipale()