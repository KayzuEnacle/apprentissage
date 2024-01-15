import os
import re

# Spécifiez le chemin du dossier contenant les curseurs
folder_path = "C:\Users\Kayzu\Documents\OneDrive\Cursors\Hololive Mouse cursor\Hololive 0th\Hoshimachi suiseiMouse cursor\Hoshimachi suisei(new costume)Mouse cursor"

# Liste des noms de curseurs appropriés
cursor_names = []

# Scanner tous les fichiers dans le dossier spécifié
for file in os.listdir(folder_path):
    # Vérifier si le fichier est un fichier de curseur
    if file.endswith(".cur"):
        # Extraire le nom du curseur du nom du fichier
        cursor_name = re.search(r'(.*)\.cur', file).group(1)
        # Ajouter le nom du curseur à la liste des noms de curseurs
        cursor_names.append(cursor_name)

for cursor_name in cursor_names:
    # Construire le chemin du fichier de curseur
    cursor_file_path = os.path.join(folder_path, cursor_name + ".cur")
    
    # Copier le fichier de curseur dans le dossier des curseurs de Windows
    shutil.copy(cursor_file_path, "C:\\Windows\\Cursors")
        
    # Modifier le curseur actuel
    windll.user32.SystemParametersInfoW(0x0057, 0, cursor_file_path, 0)

