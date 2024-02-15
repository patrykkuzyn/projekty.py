program = """nip = input("Podaj NIP: ")

def sprawdzanie_nip(nip):
    if len(nip) != 10:
        return False
    waga = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    suma = 0
    for i in range(9):
        suma += int(nip[i]) * waga[i]
        ostatnia_liczba = suma % 11
        return ostatnia_liczba
    if ostatnia_liczba == int(nip(10)):
        return True

    else:
        return False
if sprawdzanie_nip(nip):
    print("Poprawny NIP")
else:
    print("Niepoprawny NIP")"""
with open("/Users/kubus/OneDrive/Desktop/projekty.py/walidacjarego.txt", "w")as file:
    file.write(program)
