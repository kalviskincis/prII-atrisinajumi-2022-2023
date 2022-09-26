import sqlite3

# Dota datubāze biblioteka.db
# Izveido savienojumu un kursoru
conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

# No datu bāzes parādi visus tabulas Lasitajs ierakstus
c.execute('SELECT * FROM Lasitajs')
rezultats = c.fetchall()
for viens in rezultats:
    print(viens)

# Izveido jaunu datubāzes tabulu Pakalpojumi
# ar šādiem laukiem: id, nosaukums, maksa
c.execute('CREATE TABLE IF NOT EXISTS Pakalpojumi (id INTEGER PRIMARY KEY AUTOINCREMENT, nosaukums TEXT, maksa REAL)')
conn.commit()

# Tabulai Pakalpojumi pievieno ierakstu pakalpojumu "skenēšana" ar cenu "0,50"
skenesana = ("skenēšana", "0.5")
c.execute('INSERT INTO Pakalpojumi (nosaukums, maksa) VALUES (?, ?)', skenesana)

# Saglabā izmaiņas DB un slēdz savienojumu
conn.commit()
c.close()
conn.close()