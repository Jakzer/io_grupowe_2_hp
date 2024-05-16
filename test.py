from main import waluta_str_na_dict

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
