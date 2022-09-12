import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# arriere plan du jeu
background = pygame.image.load(r"PygameAssets-main/bg.jpg")

#charger la baniere
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer le boutton play
play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan
    screen.blit(background, (0, -200))

    #verifier si le jeu a commencer ou non
    if game.is_playing:
        #déclencher les instruction de la partie
        game.update(screen)
    #verifier si le jeu n'a pas commencé
    else:
        #ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else :
                    # mettre le jeu en 'lancer'
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le boutton play
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en 'lancer'
                game.start()
                #jouer le son
                game.sound_manager.play('click')
    # fixer le nombre de fps sur la clock
    clock.tick(FPS)