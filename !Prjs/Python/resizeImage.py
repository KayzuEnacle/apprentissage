import tkinter as tk
from tkinter import filedialog
from PIL import Image

def resize_images():
    # Sélectionner les images à redimensionner
    file_paths = filedialog.askopenfilenames(filetypes=[("PNG Files", "*.png")])
    
    # Obtenir les dimensions de redimensionnement
    resize_width = int(entry_width.get())
    resize_height = int(entry_height.get())
    
    # Redimensionner chaque image sélectionnée
    for file_path in file_paths:
        image = Image.open(file_path)
        original_width, original_height = image.size
        aspect_ratio = original_width / original_height
        
        if aspect_ratio > 1:
            new_width = resize_width
            new_height = int(resize_width / aspect_ratio)
        else:
            new_width = int(resize_height * aspect_ratio)
            new_height = resize_height
        
        resized_image = image.resize((new_width, new_height))
        resized_image.save(file_path)
    
    # Afficher un message de confirmation
    label_message.config(text="Les images ont été redimensionnées avec succès!")

# Créer la fenêtre principale
window = tk.Tk()
window.title("Redimensionner les images")
window.geometry("400x200")

# Créer les widgets
label_width = tk.Label(window, text="Largeur de redimensionnement:")
label_width.pack()

entry_width = tk.Entry(window)
entry_width.pack()

label_height = tk.Label(window, text="Hauteur de redimensionnement:")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

button_select = tk.Button(window, text="Sélectionner les fichiers", command=resize_images)
button_select.pack()

label_message = tk.Label(window, text="")
label_message.pack()

# Lancer la boucle principale de l'interface graphique
window.mainloop()