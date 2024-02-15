
regon = input("Podaj Regon:")

def sprawdzam_regon(regon):
    if len(regon) != 9:
        return False
        print("Regon musi posiadać 9 cyfr")
    wagi = [8, 9, 2, 3, 4, 5, 6, 7]
    suma = 0
    for i in range(8):
        suma += int(regon[i]) * wagi[i]
        cyfra_kontrolna = suma % 11
        return cyfra_kontrolna
        if cyfra_kontrolna == int(regon[9]):
            return True
        else:
            return False

if sprawdzam_regon(regon):
    print("Poprawny Regon")
else:
    print("Niepoprawny Regon")





