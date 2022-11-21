from noma import Noma
import PySimpleGUI as sg

menu = [
    ["File", ["Saglabāt", "Iziet"]]
]

layout1 = [
    [sg.Text("Produkta kategorija", size=21), sg.InputText(key="-KATEGORIJA-")],
    [sg.Text("Produkta nosaukums", size=21), sg.InputText(key="-NOSAUKUMS-")],
    [sg.Text("Tehniskie raksturojumi", size=21), sg.InputText(key="-RAKSTUROJUMI-")],
    [sg.Text("Nomas cena diena", size=21), sg.InputText(key="-CENA-")],
    [sg.Text("Produkts pieejams", size=21), sg.InputText(key="-PIEJAMS-")],
    [sg.Text("Nomnieka vards", size=21), sg.InputText(key="-VARDS-")],
    [sg.Text("Nomnieka uzvards", size=21), sg.InputText(key="-UZVARDS-")],
    [sg.Text("Nomnieka pk", size=21), sg.InputText(key="-PK-")],
    [sg.Text("Nomnieka tel nr", size=21), sg.InputText(key="-TEL-")],
    [sg.Text("Nomas sakuma datums", size=21), sg.InputText(key="-SAKUMS-")],
    [sg.Text("Nomas beigu datums", size=21), sg.InputText(key="-BEIGAS-")],
    [sg.Button("Saglabāt", size=21)]
]

layout2 = [
    [sg.Text(key="-APRAKSTS-")]
]

layout = [
    [sg.Menu(menu)],
    [sg.TabGroup([[sg.Tab("Ievade", layout1), sg.Tab("Apraksts", layout2)]])]
]

window = sg.Window("Noma", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Saglabāt":
        kategeorija = values["-KATEGORIJA-"]
        nosaukums = values["-NOSAUKUMS-"]
        raksturojumi = values["-RAKSTUROJUMI-"]
        cena = float(values["-CENA-"])
        pieejams = values["-PIEJAMS-"]
        vards = values["-VARDS-"]
        uzvards = values["-UZVARDS-"]
        pk = values["-PK-"] 
        tel = values["-TEL-"] 
        sakums = values["-SAKUMS-"]
        beigas = values["-BEIGAS-"]

        noma = Noma(kategeorija, nosaukums, raksturojumi, cena, pieejams, vards, uzvards, pk, tel, sakums, beigas)

        teksts1 = noma.produkta_info()
        teksts2 = noma.nomnieka_info()

        apraksta_teksts = f"{teksts1}\n\n{teksts2}"

        window["-APRAKSTS-"].update(apraksta_teksts)

    if event == "Saglabāt":
        noma.produkta_info_print()
        noma.nomnieka_info_print()   

window.close()
