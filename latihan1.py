import PySimpleGUI as sg
window = sg.Window(title="Profile", layout=[
    [sg.Text("NPM      : 221001032 ")],
    [sg.Text("Nama     : Wanda ")],
    [sg.Text("Kelas     : 5N Regular Banjarmasin ")],
    [sg.Text("Matkul    : Pemograman Visual 3 ")],
    
    ],size=(400,200))
window()
window.close()