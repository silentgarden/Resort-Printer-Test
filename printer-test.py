import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Button('1'), sg.Button('2'), sg.Button('3')]]

window = sg.Window('Printer Test', layout, size=(310, 90), resizable=False)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break
