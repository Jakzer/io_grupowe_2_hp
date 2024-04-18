import time
import random

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
