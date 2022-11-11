import PySimpleGUI as sg

default = "0.00"
labels = ('Velocity:', 'Time:', 'Acceleration:')
size = max(map(len, labels))

font = ('Courier New', 11)
sg.theme('DarkAmber')
sg.set_options(font=font)

layout = [
    [sg.Text(label, size=size), sg.Input(default, key=label.split()[0])]
        for label in labels] + [
    [sg.Push(), sg.Button('Calculate')],
    [sg.Push(), sg.Text(size=(20, 1), justification='right', key='-AREA-'),sg.Text(' units')]
]

window = sg.Window('Area Calculator', layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Calculate':
        print (f"{event} called")
        vi = float(values['Velocity:'])
        t = float(values['Time:'])
        a = float(values['Acceleration:'])
        area = (vi * t) + (.5 * a * (t * t))
        window['-AREA-'].Update(area)

window.close()