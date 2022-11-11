import PySimpleGUI as sg

default = "0.00"
labels = ('Velocity:', 'Time:', 'Acceleration:')
size = max(map(len, labels))

font = ('Courier New', 11)
sg.theme('DarkAmber')
sg.set_options(font=font)

timePerSecondUnits = ['ft/s', 'cm/s', 'm/s']
timeUnits = ['s', 'm', 'h']

def convert(num, currentUnit, desiredUnit):
    if (currentUnit == desiredUnit):
        return num

    if (desiredUnit == 'ft/s'):
        if (currentUnit == 'cm/s'):
            return (num / 30.48)
        
        if (currentUnit == 'm/s'):
            return (num * 3.28084)

    if (desiredUnit == 's'):
        if (currentUnit == 'm'):
            return (num / 60)
        if (currentUnit == 'h'):
            return (num / 3600)


layout = [
    
    [sg.Text("Initial Velocity", size=20), sg.Input(default, key= "VELOCITY"),
        sg.OptionMenu(values = timePerSecondUnits, key = 'VEL-OPTION')   ],

    [sg.Text("Time", size=20), sg.Input(default, key= "TIME"),
        sg.OptionMenu(values = timeUnits, key = 'TIME-OPTION')],

    [sg.Text("Accerlation", size=20), sg.Input(default, key= "ACCELERATION"),
        sg.OptionMenu(values = timePerSecondUnits, key = 'ACC-OPTION')   ],


    [sg.Push(), sg.Button('Calculate')],
    [sg.Push(), sg.Text(size=(20, 1), justification='right', key='-AREA-'),sg.Text('ft/s')]
]

window = sg.Window('Area Calculator', layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break   
    
    if event == 'Calculate':
        print (f"{event} called")
        print (bool(values['VEL-OPTION']))

        if (not (bool(values['VEL-OPTION']) and bool(values['TIME-OPTION']) and bool(values['ACC-OPTION']))):
            window['-AREA-'].Update('Please select a unit')

        else:
            vi =convert(float(values['VELOCITY']), values['VEL-OPTION'], "ft/s")
            t = convert(float(values['TIME']), values['TIME-OPTION'], "s")
            a = convert(float(values['ACCELERATION']), values['ACC-OPTION'], "ft/s")

            area = (vi * t) + (.5 * a * (t * t))
            window['-AREA-'].Update(area)


window.close()