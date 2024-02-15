import sqlite3



# Połącz się z bazą danych SQLite
conn = sqlite3.connect('baza_danych.db')
cursor = conn.cursor()

nazwa_pliku = 'walidacjanip.txt'
cursor.execute("SELECT id FROM Pliki WHERE nazwa = ?", (nazwa_pliku,))
id_pliku = cursor.fetchone()[0]

# Zapytanie SQL do pobrania nazwy i zawartości pliku o określonym identyfikatorze
cursor.execute("SELECT nazwa, zawartosc FROM Pliki WHERE id = ?", (id_pliku,))
nazwa_pliku, zawartosc_pliku = cursor.fetchone()

# Zapisz zawartość pliku do nowego pliku na dysku
with open(nazwa_pliku, 'wb') as file:
    file.write(zawartosc_pliku.encode('utf-8'))


# Zamknij połączenie z bazą danych SQLite
conn.close()

with open(nazwa_pliku, 'rb') as file:
    zawartosc_pliku = file.read().decode('utf-8')
    print(zawartosc_pliku)

with open("walidacjanip.txt", "r") as file:
    kod_pythona = file.read()

exec(kod_pythona)