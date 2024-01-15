from random import randint
import time

roll = randint(0, 100)

def print_anim(text):
    dots = ""
    for _ in range(3):
        dots += "."
        print(text + dots, end='\r')
        time.sleep(0.5)  # Délai de 0.5 seconde entre chaque ajout de point
    print(text + dots)  # Affiche la phrase complète avec les trois points de suspension

# Utilisation
phrase = "La pièce est lancée"
print_anim(phrase)

time.sleep(2)


print("Le résultat est : ")
if roll < 50:
    print("Pile")
else:
    print("Face")
