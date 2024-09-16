# import de lib
import random

#Création de ma liste de mot 
ma_liste = ['Papillon', 'Bicyclette', 'Etoile', 'Crocodile']

#choix dans ma liste
mon_mot = random.choice(ma_liste)
print(mon_mot)

# création de ma variable et de mes tirets

longueur_mot = len(mon_mot)

mot_secret = '-'* longueur_mot

print(mot_secret)