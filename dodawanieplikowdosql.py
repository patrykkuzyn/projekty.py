import sqlite3
# Otwórz połączenie z bazą danych SQLite
conn = sqlite3.connect('baza_danych.db')

# Utwórz kursor do wykonywania poleceń SQL
cursor = conn.cursor()

# Utwórz tabelę Pliki, jeśli nie istnieje
cursor.execute('''CREATE TABLE IF NOT EXISTS Pliki
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nazwa TEXT NOT NULL,
                   zawartosc TEXT NOT NULL)''')

# Zatwierdź zmiany i zamknij połączenie
conn.commit()
conn.close()
# Otwórz połączenie z bazą danych SQLite
conn = sqlite3.connect('baza_danych.db')

# Otwórz plik i przeczytaj jego zawartość
with open('walidacjanip.txt', 'r') as file:
    zawartosc = file.read()

# Wstaw dane pliku do tabeli w bazie danych
conn.execute("INSERT INTO Pliki (nazwa, zawartosc) VALUES (?, ?)", ('walidacjanip.txt', zawartosc))

# Zatwierdź zmiany i zamknij połączenie
conn.commit()
conn.close()
