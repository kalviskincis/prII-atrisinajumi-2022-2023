import PySimpleGUI as sg
import sqlite3
import hashlib

conn = sqlite3.connect("pizza.db")
c = conn.cursor()

def dabut_picu_nosaukumus():
    vaicajums = "SELECT nosaukums FROM picas"
    c.execute(vaicajums)
    picas_raw = c.fetchall()
    picas = []
    for viens in picas_raw:
        picas.append(viens[0])
    return picas

def dabut_picas_izmeru(pica):
    vaicajums = f"SELECT izmeri.diametrs, picas_ar_cenam.cena, picas.nosaukums FROM picas_ar_cenam INNER JOIN izmeri ON picas_ar_cenam.izmera_ID = izmeri.ID INNER JOIN picas ON picas.ID = picas_ar_cenam.picas_ID WHERE nosaukums LIKE \"{pica}\" "
    c.execute(vaicajums)
    izmeri_raw = c.fetchall()
    izmeri = []
    for viens in izmeri_raw:
        izmeri.append(viens[0])
    return izmeri

def dabut_izmerus():
    vaicajums = "SELECT diametrs FROM izmeri"
    c.execute(vaicajums)
    izmeri_raw = c.fetchall()
    izmeri = []
    for viens in izmeri_raw:
        izmeri.append(viens[0])
    return izmeri

def dabut_klientu_sarakstu():
    vaicajums = "SELECT vards FROM klienti"
    c.execute(vaicajums)
    klienti_raw = c.fetchall()
    klienti = []
    for viens in klienti_raw:
        klienti.append(viens[0])
    return klienti

def dabut_piegades():
    vaicajums = "SELECT veids FROM piegades_veidi"
    c.execute(vaicajums)
    piegades_raw = c.fetchall()
    piegades = []
    for viena in piegades_raw:
        piegades.append(viena[0])
    return piegades

picas = dabut_picu_nosaukumus()
izmeri = dabut_izmerus()
klienti = dabut_klientu_sarakstu()
piegade = dabut_piegades()

# pasūtījuma forma
layout1 = [
    [sg.Text("Picas izvēle:"), sg.Combo(values=picas, key="-PICA-PASUT-", enable_events=True)],
    [sg.Text("Izmērs:"), sg.Combo(values=izmeri, key="-IZM-PASUT-")],
    [sg.Text("Klients:"), sg.Combo(values=klienti, key="-KLIENTS-PASUT-")],
    [sg.Text("Piegāde:"), sg.Combo(values=piegade, key="-PIEGADE-PASUT-")],
    [sg.Button("Pasūtīt"), sg.Button("Parādīt pasūtījumu(-s)")],
    [sg.HSep()],
    [sg.Text(key="-PASUTIJUMA-TEKSTS-")]
]

# picu, izmēru un piegādes veidu pārvaldības forma
layout2 = [
    [sg.Text("Picas nosaukums"), sg.Input(key="-JAUNS-NOSAUKUMS-")],
    [sg.Button("Saglabāt nosaukumu", key="-NOSAUKUMA-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Izmērs (cm)"), sg.Input(key="-JAUNS-IZMERS-")],
    [sg.Button("Saglabāt izmēru", key="-IZMERA-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Picas nosaukums"), sg.Combo(values=picas, key="-PICA-")],
    [sg.Text("Picas izmērs"), sg.Combo(values=izmeri, key="-IZMERS-")],
    [sg.Text("Picas cena"), sg.Input(key="-CENA-")],
    [sg.Button("Saglabāt picu", key="-PICAS-AR-CENU-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Piegādes veids"), sg.Input(key="-JAUNA-PIEGADE-")],
    [sg.Text("Piegādes cema"), sg.Input(key="-JAUNA-PIEGADE-CENA-")],
    [sg.Button("Saglabāt piegādi", key="-PIEGADES-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Button("Poga bez eventa, lai kaut ko no tā visa parādītu. Izmantot pēc ieskatiem.")]
]

# Klientu pievienošana
layout3 = [
    [sg.Text("Vārds", size=14), sg.Input(key="-VARDS-")],
    [sg.Text("Tālrunis", size=14), sg.Input(key="-TALRUNIS-")],
    [sg.Text("Parole", size=14), sg.Input(key="-PAROLE-")],
    [sg.Button("Pievienot", size=14, key="-PIEVIENOT-KLIENTU-")],
    [sg.Button("Parādīt visus", key="-PARADIT-KLIENTUS-", size=14)],
    [sg.Text(key="-KLIENTA-INFO-")]
]

layout = [
    [sg.TabGroup([[sg.Tab("Picērija", layout1), sg.Tab("Pievienošana", layout2), sg.Tab("Klienti", layout3), ]])],
    [sg.Button("Iziet", size=12)]
]

window = sg.Window("PIZZA TIME", layout)

while True:
    event, values = window.read()

    if event == "Iziet" or event == sg.WINDOW_CLOSED:
        break

    if event == "-PICA-PASUT-":
        pica = values["-PICA-PASUT-"]
        window.find_element("-IZM-PASUT-").update(values=dabut_picas_izmeru(pica))

    if event == "Pasūtīt":
        pica = values["-PICA-PASUT-"]
        izmers = values["-IZM-PASUT-"]
        klients = values["-KLIENTS-PASUT-"]
        piegade = values["-PIEGADE-PASUT-"]

        picas_ar_cenu_vaicajums = f"""
        SELECT picas_ar_cenam.ID
        FROM picas_ar_cenam
        INNER JOIN picas
        ON picas.ID = picas_ar_cenam.picas_ID
        INNER JOIN izmeri 
        ON izmeri.ID = picas_ar_cenam.izmera_ID
        WHERE (picas.nosaukums = \"{pica}\" and izmeri.diametrs = \"{izmers}\")
        """

        klienta_vaicajums = f"SELECT ID FROM klienti WHERE vards LIKE \"{klients}\""
        piegades_vaicajums = f"SELECT ID FROM piegades_veidi WHERE veids LIKE \"{piegade}\""

        c.execute(picas_ar_cenu_vaicajums)
        picas_ID = c.fetchall()[0][0]

        c.execute(klienta_vaicajums)
        klienta_ID = c.fetchall()[0][0]

        c.execute(piegades_vaicajums)
        piegades_ID = c.fetchall()[0][0]

        pasutijums_DB = (picas_ID, klienta_ID, piegades_ID)
        c.execute("INSERT INTO pasutijumi (picas_ar_cenu_ID, klienta_ID, piegades_veida_ID) VALUES (?, ?, ?)", pasutijums_DB)
        conn.commit()

    if event == "Parādīt pasūtījumu(-s)":
        vaicajums = """
        SELECT klienti.vards, picas.nosaukums, izmeri.diametrs, piegades_veidi.veids
        FROM pasutijumi
        INNER JOIN klienti
        ON klienti.ID = pasutijumi.klienta_ID
        INNER JOIN picas_ar_cenam
        ON picas_ar_cenam.ID = pasutijumi.picas_ar_cenu_ID
        INNER JOIN picas
        ON picas.ID = picas_ar_cenam.ID
        INNER JOIN izmeri
        ON izmeri.ID = picas_ar_cenam.izmera_ID                
        INNER JOIN piegades_veidi
        ON pasutijumi.piegades_veida_ID = piegades_veidi.ID  
        """

        c.execute(vaicajums)
        pasutijumi = c.fetchall()
        print(pasutijumi)

        """
        "-PASUTIJUMA-TEKSTS-"
        """

    if event == "-NOSAUKUMA-PIEVIENOSANA-":
        jauns_nosaukums = values["-JAUNS-NOSAUKUMS-"]
        c.execute("INSERT INTO picas (nosaukums) VALUES (?)", (jauns_nosaukums,))
        conn.commit()

    if event == "-IZMERA-PIEVIENOSANA-":
        jauns_izmers = values["-JAUNS-IZMERS-"]
        c.execute("INSERT INTO izmeri (diametrs) VALUES (?)", (jauns_izmers,))
        conn.commit()

    if event == "-PICAS-AR-CENU-PIEVIENOSANA-":
        picas_nosaukums = values["-PICA-"]
        picas_izmers = values["-IZMERS-"]
        picas_cena = values["-CENA-"]

        picas_vaicajums = f"SELECT ID FROM picas WHERE nosaukums = \"{picas_nosaukums}\""
        izmera_vaicajums = f"SELECT ID FROM izmeri WHERE diametrs = \"{picas_izmers}\""

        c.execute(picas_vaicajums)
        picas_ID = c.fetchall()[0][0]

        c.execute(izmera_vaicajums)
        izmera_ID = c.fetchall()[0][0]

        pica_ar_cenu_DB = (picas_ID, izmera_ID, picas_cena)
        c.execute("INSERT INTO main.picas_ar_cenam (picas_ID, izmera_ID, cena) VALUES (?, ?, ?)", pica_ar_cenu_DB)
        conn.commit()

    if event == "-PIEGADES-PIEVIENOSANA-":
        veids = values["-JAUNA-PIEGADE-"]
        cena = values["-JAUNA-PIEGADE-CENA-"]

        piegade_DB = (veids, cena)
        c.execute("INSERT into piegades_veidi (veids, cena) VALUES (?, ?)", piegade_DB)
        conn.commit()

    if event == "-PIEVIENOT-KLIENTU-":
        vards = values["-VARDS-"]
        talrunis = values["-TALRUNIS-"]
        parole = values["-PAROLE-"]
        parole_b = str.encode(parole)
        parole_sha512 = hashlib.sha512(parole_b)
        parole_hash = parole_sha512.hexdigest()

        klients_DB = (vards, talrunis, parole_hash)
        c.execute("INSERT INTO klienti (vards, talrunis, parole) VALUES (?, ?, ?)", klients_DB)
        conn.commit()

    if event == "-PARADIT-KLIENTUS-":
        """
        "-KLIENTA-INFO-"
        """
        c.execute("SELECT vards, talrunis FROM klienti")
        visi_klienti = c.fetchall()
        for viens in visi_klienti:
            print(viens)


window.close()
conn.commit()
c.close()
conn.close()
