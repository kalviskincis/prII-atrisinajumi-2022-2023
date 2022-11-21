import PySimpleGUI as sg
from bibliotekaPlus import Biblioteka
from bibliotekaPlus import Lasitajs

izvelne = [
    ["Datne", ["Saglabāt iespieddarbu", "Saglabāt lasītāju", "Iziet"]]
]

layout1 = [
    [sg.Text("Iespieddarba kategorija", size=25), sg.InputText(key="-KATEGORIJA-")],
    [sg.Text("Iespieddarba nosaukums", size=25), sg.InputText(key="-NOSAUKUMS-")],
    [sg.Text("Iespieddarba autors", size=25), sg.InputText(key="-AUTORS-")],
    [sg.Text("Izdevums pieejams", size=25), sg.InputText(key="-PIEJAMS-")],
    [sg.Text("Izsniegšanas datums", size=25), sg.InputText(key="-DATUMS-")],
    [sg.Text("Izsniegšanas termiņš", size=25), sg.InputText(key="-TERMINS-")],
    [sg.Text("Atgriešanas datums", size=25), sg.InputText(key="-ATGRIEŠANAS-")],
    [sg.Button("Izveidot ierakstu iespieddarbam")],
    [sg.Text("Lasītāja vārds", size=25), sg.InputText(key="-VARDS-")],
    [sg.Text("Lasītāja uzvārds", size=25), sg.InputText(key="-UZVARDS-")],
    [sg.Button("Izveidot ierakstu lasītājam")]
]

layout2 = [
    [sg.VPush()],
    [sg.Button("Sagatavot aprakstu")],
    [sg.Text(key = "-APRAKSTS-")],
    [sg.VPush()]
]

layout = [
    [sg.Menu(izvelne)],
    [sg.TabGroup([[sg.Tab("Izveidot ierakstu", layout1), sg.Tab("Apskatīt ierakstu", layout2)]])]

]

window = sg.Window("Bibliotēka", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Iziet":
        break

    if event == "Izveidot ierakstu iespieddarbam":
        kategorija = values["-KATEGORIJA-"]
        nosaukums = values["-NOSAUKUMS-"]
        autors = values["-AUTORS-"]
        pieejams = values["-PIEJAMS-"]
        datums = values["-DATUMS-"]
        termins = values["-TERMINS-"]
        atgriesanas = values["-ATGRIEŠANAS-"]
        biblio = Biblioteka(kategorija, nosaukums, autors, pieejams, datums, termins, atgriesanas)

    if event == "Izveidot ierakstu lasītājam":
        vards = values["-VARDS-"]
        uzvards = values["-UZVARDS-"]
        lasitajs = Lasitajs(vards, uzvards)
        

    if event == "Sagatavot aprakstu":
        izd_apraksts = biblio.iespieddarba_info()
        las_apraksts = lasitajs.lasitaja_info()
        apraksts = izd_apraksts + "\n" + las_apraksts
        window["-APRAKSTS-"].update(apraksts)


    if event == "Saglabāt iespieddarbu":
        biblio.iespieddarba_info_print()

    if event == "Saglabāt lasītāju":
        lasitajs.lasitaja_info_print()


window.close()