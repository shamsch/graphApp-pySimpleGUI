import PySimpleGUI as sg

layout = [
    [sg.Input()],
    [sg.Text('text here')]
]

window = sg.Window('something', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()