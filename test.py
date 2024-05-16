from main import licz_sume

suma = licz_sume({
    "geleon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
})
assert suma=={'geleon': 12, 'sykl': 0, 'knut': 14}
