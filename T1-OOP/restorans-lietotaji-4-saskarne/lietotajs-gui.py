from lietotajs import Lietotajs
import PySimpleGUI as sg

layout = [
    [sg.Text("Vārds")],
    [sg.Input(key = "-VARDS-")],
    [sg.Text("Uzvārds")],
    [sg.Input(key = "-UZVARDS-")],
    [sg.Text("Lietotājvārds")],
    [sg.Input(key = "-LIETOTAJVARDS-")],
    [sg.Text("e-pasts")],
    [sg.Input(key = "-EPASTS-")],
    [sg.Push(),sg.Button("Izveidot"), sg.Button("Parādīt"), sg.Button("Iziet"),sg.Push()],
    [sg.Push(), sg.Text(key = "-IZVADE-"),sg.Push()]
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
        jaunslietotajs = Lietotajs(vards, uzvards, lietotajvards, epasts)

        sg.popup(f"Sveiki, {vards}!")

    if event == "Parādīt":
        try:
            apraksts = jaunslietotajs.lietotaja_apraksts()
            window["-IZVADE-"].update(apraksts)
        except:
            sg.popup_ok("Radās kļūda. Iespējams, nav izveidots lietotājs")



