import datetime

date = datetime.date.today()

vendredi_13 = []

for i in range(0, 1000*365):
    date += datetime.timedelta(days=1)
    if date.weekday() == 4 and date.day == 13:
        vendredi_13.append(date)

mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
with open('resultat.txt', 'w', encoding='utf-8') as f:
    for date in vendredi_13:
        f.write(f"Vendredi {date.day} {mois[date.month-1]} {date.year}\n")