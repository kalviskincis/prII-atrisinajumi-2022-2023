from lietotajs import Lietotajs
import PySimpleGUI as sg

menu_layout = [
    ["Datne", ["Saglabāt TXT", "Saglabāt JSON", "Iziet"]],
    ["Palīdzība", ["Par"]]
]

layout1 = [
    [sg.Text("Vārds")],
    [sg.Input(key = "-VARDS-")],
    [sg.Text("Uzvārds")],
    [sg.Input(key = "-UZVARDS-")],
    [sg.Text("Lietotājvārds")],
    [sg.Input(key = "-LIETOTAJVARDS-")],
    [sg.Text("e-pasts")],
    [sg.Input(key = "-EPASTS-")],
    [sg.Text("Dzimšanas datums (formātā GGGG-MM-DD)")],
    [sg.Input(key="-DZIM-")],
    [sg.Push(),sg.Button("Izveidot"), sg.Push()]
]

layout2 = [
    [sg.Push(),sg.Button("Parādīt"), sg.Push()],
    [sg.Push(),sg.Button("Saglabāt TXT"), sg.Button("Saglabāt JSON"), sg.Push()]
]

layout3 = [
    [sg.Push(), sg.Text(key = "-IZVADE-"),sg.Push()]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.TabGroup([[sg.Tab("Datu ievade", layout1), sg.Tab("Darbības ar datiem", layout2), sg.Tab("Lietotāja apraksts", layout3)]])],
    [sg.Push(), sg.Button("Iziet"),sg.Push()]
]

window = sg.Window("Lietotāju pievienošana", layout)

while True:
    event, values = window.read()
    if event in ("Iziet", sg.WINDOW_CLOSED):
        break

    if event == "Izveidot":
        vards = values["-VARDS-"]
        uzvards = values["-UZVARDS-"]
        lietotajvards = values["-LIETOTAJVARDS-"]
        epasts = values["-EPASTS-"]
        dzimsanas_datums = values["-DZIM-"]
        jaunslietotajs = Lietotajs(vards, uzvards, lietotajvards, epasts, dzimsanas_datums)

        sg.popup(f"Sveiki, {vards}!")

    if event == "Parādīt":
        try:
            apraksts = jaunslietotajs.lietotaja_apraksts()
            window["-IZVADE-"].update(apraksts)
        except:
            sg.popup_ok("Radās kļūda. Iespējams, nav izveidots lietotājs")

    if event == "Saglabāt TXT":
        try:
            jaunslietotajs.saglabat_txt()
        except:
            sg.popup_ok("Radās kļūda. Iespējams, nav izveidots lietotājs")

    if event == "Saglabāt JSON":
        try:
            jaunslietotajs.saglabat_json()
        except:
            sg.popup_ok("Radās kļūda. Iespējams, nav izveidots lietotājs")

    if event == "Pārbaudīt dzimšanas dienu":
        try:
            pazinojuma_teksts = jaunslietotajs.nakama_dzimsanas_diena()
            sg.popup(pazinojuma_teksts)
        except:
            sg.popup_ok("Radās kļūda. Iespējams, nav izveidots lietotājs")




