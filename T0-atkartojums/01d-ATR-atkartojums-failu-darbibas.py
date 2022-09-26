import csv
import json

# Dotas datnes epakalpojumi.csv un pancakes.json
# Vismaz vienu no tiem atver un nolasi, izmantojot piemērotu moduli. Nolasīto saturu parādi Tevis izvēlētā izskatā.
with open("pancakes.json", "r", encoding="utf-8") as f:
    dati_raw = f.read()
    dati = json.loads(dati_raw)
    for atslega in dati:
        print(f"{atslega}: {dati[atslega]}")


with open("epakalpojumi.csv", "r", encoding="utf-8") as f:
    dati = csv.reader(f)
    for rinda in dati:
        print(rinda)

# Dota viena vārdnīca un viens masīvs. Izmantojot piemērotu moduli (bibliotēku), vismaz vienu tiem ieraksti piemērota formāta failā.
oga = {"Nosaukus": "Dzērvene", "Krāsa": "Sarkana", "Augšanas vieta": "Purvs, dārzs"}
darzeni = ["Kartupeļi", "Burkāni", "Bietes", "Kabači", "Kāļi"]

with open("dzervene.json", "w", encoding="utf-8") as f:
    dati = json.dumps(oga, ensure_ascii=False)
    f.write(dati)

with open("darzeni.csv", "w", encoding="utf-8") as f:
    saglabasanai = csv.writer(f, delimiter=",")
    saglabasanai.writerow(darzeni)