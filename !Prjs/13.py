import datetime

# Date de départ
date = datetime.date.today()

# Liste pour stocker les dates
vendredi_13 = []

# Boucle pour les 30 prochaines années
for i in range(0, 1000*365):
    # Ajoute un jour à la date
    date += datetime.timedelta(days=1)
    
    # Vérifie si le jour est un vendredi 13
    if date.weekday() == 4 and date.day == 13:
        vendredi_13.append(date)

# Affiche les dates
mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
with open('resultat.txt', 'w', encoding='utf-8') as f:
    for date in vendredi_13:
        f.write(f"Vendredi {date.day} {mois[date.month-1]} {date.year}\n")