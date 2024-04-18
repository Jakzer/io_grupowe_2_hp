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
    
    # Sprawdzenie potwierdzenia odbioru
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