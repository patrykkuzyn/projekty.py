
pesel = input("Podaj PESEL: ")

def sprawdzam_pesel(pesel):
    if len(pesel) != 11:
        print("PESEL musi mieć 11 cyfr")
        return False
    cyfry = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * cyfry[i]
        suma_ostatnaia_cyfra = abs(suma % 10 - 10)

    if suma_ostatnaia_cyfra == int(pesel[11]):
        return True
    else:
        return False
if sprawdzam_pesel(pesel):
    print("PESEL jest poprawny")
else:
    print("PESEL jest niepoprawny")
















