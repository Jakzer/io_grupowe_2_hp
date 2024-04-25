import random
import csv
def wyslij_sowe(adresat, treść, koszt, potwierdzenie):
    dolecialo = random.choice(["Tak", "Nie"])

    if dolecialo == "Tak":
        rzeczywisty_koszt = 0
    else:
        rzeczywisty_koszt = float(koszt)
    
    return(adresat, treść, koszt, potwierdzenie)

def poczta_wyslij_sowy(kontakt.csv):
    wyniki = []