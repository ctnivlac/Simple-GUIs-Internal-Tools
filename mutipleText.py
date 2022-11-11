import PySimpleGUI as sg

default = "0.00"
labels = ('Numbers of pulses:', 'Frequency (Hz):', 'Pulse width (ms):', 'Amplitude (V):')
size = max(map(len, labels))

font = ('Courier New', 11)
sg.theme('DarkBlue4')
sg.set_options(font=font)

layout = [
    [sg.Text(label, size=size), sg.Input(default, key=label.split()[0])]
        for label in labels] + [
    [sg.Push(), sg.Button('Send')]
]
window = sg.Window('Window Title', layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event, values)

window.close()