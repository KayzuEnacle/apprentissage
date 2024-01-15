import pygame
import random
import os
import webbrowser

# Masquer le message d'accueil de Pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Initialisation de pygame
pygame.init()

# Définition des dimensions de la fenêtre du jeu
largeur = 800
hauteur = 400

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Dinosaure")

# Chargement des images
repertoire = os.path.dirname(os.path.abspath(__file__))
dinosaure_img = pygame.image.load(os.path.join(repertoire, "dinosaure.png"))
cactus_img = pygame.image.load(os.path.join(repertoire, "cactus.png"))

# Position initiale du dinosaure
dinosaure_x = 50
dinosaure_y = hauteur - dinosaure_img.get_height() - 10

# Variables pour les cactus
cactus_x = largeur
cactus_y = hauteur - cactus_img.get_height() - 10
vitesse_cactus = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Variables pour le saut
saut_en_cours = False
hauteur_saut = 100
gravite = 10

def update():
    global cactus_x, score, dinosaure_y, saut_en_cours, gravite

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not saut_en_cours:
                saut_en_cours = True

   # Logique de saut
    if saut_en_cours:
        dinosaure_y -= gravite
        gravite -= 1
        if gravite < -hauteur_saut:
            saut_en_cours = False
            gravite = 10

    # Mise à jour de la position du cactus
    cactus_x -= vitesse_cactus
    if cactus_x < -cactus_img.get_width():
        cactus_x = largeur
        score += 1

    # Vérification des collisions
    if dinosaure_x + dinosaure_img.get_width() > cactus_x and dinosaure_x < cactus_x + cactus_img.get_width() and dinosaure_y + dinosaure_img.get_height() > cactus_y:
        # webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        pygame.quit()
        quit()

    # Affichage des éléments du jeu
    fenetre.fill(blanc)
    fenetre.blit(font.render("Score: " + str(score), True, noir), (10, 10))
    fenetre.blit(dinosaure_img, (dinosaure_x, dinosaure_y))
    fenetre.blit(cactus_img, (cactus_x, cactus_y))
    pygame.display.flip()

def main():
    # Boucle principale du jeu
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30)  # Limite le taux de rafraîchissement à 30 images par seconde
        update(hauteur_saut)

if __name__ == "__main__":
    hauteur_saut = 150  # Modifier la hauteur du saut ici
    main()