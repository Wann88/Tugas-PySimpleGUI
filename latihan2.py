import PySimpleGUI as sg

sg.theme_text_color("#0000FF")
sg.theme_background_color("red")
window = sg.Window(title="Profile", layout=[
    [sg.Text("NPM      : 221001032 ")],
    [sg.Text("Nama     : Wanda ")],
    [sg.Text("Kelas     : 5N Regular Banjarmasin ")],
    [sg.Text("Matkul    : Pemograman Visual 3 ")],
    
    ],size=(400,200))
window()
window.close()