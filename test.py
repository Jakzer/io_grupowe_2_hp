from main import licz_sume
from main import waluta_dict_na_str

suma = licz_sume({
    "geleon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
})
assert suma=={'geleon': 12, 'sykl': 0, 'knut': 14}
from main import waluta_str_na_dict

def test_dict_na_str():
    dict_test = {'galeon': 9, 'sykl': 5, 'knut': 2}
    expected = "9 galeon 5 sykl 2 knut"
    assert waluta_dict_na_str(dict_test) == expected
    print("Wszystko cool")

test_dict_na_str()

def test_waluta_str_na_dict():
    ciag_znakow = "5 galeon 10 knut 3 sykl"
    oczekiwany_wynik = {'galeon': 5, 'sykl': 3, 'knut': 10}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    ciag_znakow = ""
    oczekiwany_wynik = {}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    ciag_znakow = "10 galeon 5"
    oczekiwany_wynik = {'galeon': 10}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    ciag_znakow = "5 galeon"
    oczekiwany_wynik = {'galeon': 5}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    ciag_znakow = "5"
    oczekiwany_wynik = {}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    ciag_znakow = "5 galeon 10 knut 3"
    oczekiwany_wynik = {'galeon': 5, 'knut': 10}
    assert waluta_str_na_dict(ciag_znakow) == oczekiwany_wynik

    print("funkcja waluta str na dict działa git")


test_waluta_str_na_dict()
