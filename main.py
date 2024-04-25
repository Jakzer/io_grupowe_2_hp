import time
import random
import os
import pandas as pd


def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0,1) <= 0.85:
        return True
    else:
        return False

# print(wyslij_sowe("Hagrid", "Wpadamy na herabtkę"))
def licz_sume(money_dict):
    
    if "geleon" not in money_dict or "sykl" not in money_dict or "knut" not in money_dict:
        return "Brakuje jednego z kluczy: geleon, sykl, knut"
    
    
    geleon_list = money_dict["geleon"]
    sykl_list = money_dict["sykl"]
    knut_list = money_dict["knut"]
    
    
    total_knut = geleon_list[0] * 17 * 21 + sykl_list[0] * 21 + knut_list[0]
    total_knut += geleon_list[1] * 17 * 21 + sykl_list[1] * 21 + knut_list[1]
    total_knut += geleon_list[2] * 17 * 21 + sykl_list[2] * 21 + knut_list[2]
    

    geleon_result = total_knut // (17 * 21)
    total_knut %= 17 * 21
    sykl_result = total_knut // 21
    knut_result = total_knut % 21
    
    return {
        "geleon": geleon_result,
        "sykl": sykl_result,
        "knut": knut_result
    }


money_dict = {
    "geleon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}

print(licz_sume(money_dict))
def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt = 0
    
    
    if odleglosc == 'lokalna':
        if typ == 'list':
            koszt += 2
        elif typ == 'paczka':
            koszt += 7
    elif odleglosc == 'krajowa':
        if typ == 'list':
            koszt += 12
        elif typ == 'paczka':
            koszt += 1 * 5 + 2
    elif odleglosc == 'dalekobiezna':
        if typ == 'list':
            koszt += 20
        elif typ == 'paczka':
            koszt += 2 * 5 + 1
    
    # Sprawdzenie potwierdzenia odbior
    if potwierdzenie_odbioru:
        koszt += 7
    
    # Sprawdzenie opcji specjalnej
    if specjalna == 'wyjec':
        koszt += 4
    elif specjalna == 'list gonczy':
        koszt += 1 * 5
    
    # Zamiana na galeony, sykle i knuty
    galeony = koszt // 29
    reszta_po_galeonach = koszt % 29
    sykle = reszta_po_galeonach // 17
    knuty = reszta_po_galeonach % 17
    
    return {
        "galeon" : galeony,
        "sykl" : sykle,
        "knut" : knuty
    }

# Przykładowe wywołanie
wynik = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
print(wynik)


def waluta_dict_na_str(slownik):
    return "17 galeon 2 sykl 13 knut"

def nadaj_sowe(adresat:str,tresc:str,potwierdzenie:bool,
               odleglosc:str,typ:str,specjalna:str):
    koszt_sowy = wybierz_sowe_zwroc_koszt(potwierdzenie,odleglosc,typ,specjalna)
    if os.path.exists("poczta_nadania_lista.csv"):
        header = False
    else:
        header = True
    pd.DataFrame([{
        'adresat': adresat,
        'tresc': tresc,
        'koszt_przesylki': waluta_dict_na_str(koszt_sowy),
        'potwierdzenie_odb': 'TAK' if potwierdzenie else 'NIE'
    }]).to_csv('poczta_nadania_lista.csv', mode='a', index=False,header=header)