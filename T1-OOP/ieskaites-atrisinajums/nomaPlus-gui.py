from nomaPlus import Noma
from nomaPlus import Nomnieks
import PySimpleGUI as sg

izvelne = [
    ["Datne", ["Saglabāt produktu", "Saglabāt nomnieku", "Iziet"]]
]

layout1 = [
    [sg.Text("Produkta kategorija", size=21), sg.InputText(key="-KATEGORIJA-")],
    [sg.Text("Produkta nosaukums", size=21), sg.InputText(key="-NOSAUKUMS-")],
    [sg.Text("Tehniskie raksturojumi", size=21), sg.InputText(key="-RAKSTUROJUMI-")],
    [sg.Text("Produkts pieejams", size=21), sg.InputText(key="-PIEJAMS-")],
    [sg.Button("Izveidot ierakstu produktam", size=21)],
    [sg.Text("Nomnieka vards", size=21), sg.InputText(key="-VARDS-")],
    [sg.Text("Nomnieka uzvards", size=21), sg.InputText(key="-UZVARDS-")],
    [sg.Text("Nomnieka pk", size=21), sg.InputText(key="-PK-")],
    [sg.Text("Nomnieka tel nr", size=21), sg.InputText(key="-TEL-")],
    [sg.Text("Nomas sakuma datums", size=21), sg.InputText(key="-SAKUMS-")],
    [sg.Text("Nomas beigu datums", size=21), sg.InputText(key="-BEIGAS-")],
    [sg.Text("Nomas cena diena", size=21), sg.InputText(key="-CENA-")],
    [sg.Button("Izveidot ierakstu nomniekam", size=21)]
]

layout2 = [
    [sg.Text(key="-APRAKSTS-")]
]

layout = [
    [sg.Menu(izvelne)],
    [sg.TabGroup([[sg.Tab("Ievade", layout1), sg.Tab("Apraksts", layout2)]])]
]

window = sg.Window("Noma", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Izveidot ierakstu produktam":
        kategeorija = values["-KATEGORIJA-"]
        nosaukums = values["-NOSAUKUMS-"]
        raksturojumi = values["-RAKSTUROJUMI-"]
        pieejams = values["-PIEJAMS-"]
        noma = Noma(kategeorija, nosaukums, raksturojumi, pieejams)

    if event == "Izveidot ierakstu nomniekam":

        vards = values["-VARDS-"]
        uzvards = values["-UZVARDS-"]
        pk = values["-PK-"] 
        tel = values["-TEL-"] 
        sakums = values["-SAKUMS-"]
        beigas = values["-BEIGAS-"]
        cena = float(values["-CENA-"])

        nomnieks = Nomnieks(vards, uzvards, pk, tel, sakums, beigas, cena)

        teksts1 = noma.produkta_info()
        teksts2 = nomnieks.nomnieka_info()

        atlicis = nomnieks.nomas_atlikusais_laiks()
        maksa = nomnieks.cena_kopa()

        apraksta_teksts = f"{teksts1}\n\n{teksts2}\nAtlicis laiks: {atlicis}\nMaksa: {maksa}"

        window["-APRAKSTS-"].update(apraksta_teksts)

    if event == "Saglabāt produktu":
        noma.produkta_info_print()

    if event == "Saglabāt nomnieku":
        nomnieks.nomnieka_info_print()

window.close()
