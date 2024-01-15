import cv2
import numpy as np

def melange_pixels(image, image2=None):
    # Lire l'image
    img = cv2.imread(image)

    # Mélanger les pixels
    np.random.shuffle(img)

    # Supprimer quelques pixels
    nb_pixels = int(0.35 * img.shape[0] * img.shape[1])  # 35% des pixels
    for i in range(nb_pixels):
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        img[x, y] = [0, 0, 0]  # Remplacer par des pixels noirs

    # Si une deuxième image est fournie, ajouter 50% de ses pixels à l'image finale
    if image2:
        img2 = cv2.imread(image2)
        nb_pixels2 = int(0.50 * img2.shape[0] * img2.shape[1])  # 50% des pixels
        for i in range(nb_pixels2):
            x = np.random.randint(0, img.shape[0])
            y = np.random.randint(0, img.shape[1])
            
            img[x, y] = img2[x, y]

    # Enregistrer l'image
    cv2.imwrite('image_finale.png', img)

melange_pixels('1.png', '2.png')

