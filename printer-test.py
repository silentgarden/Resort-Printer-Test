import PySimpleGUI as sg

#######################
#Window Initialization#
#######################

sg.theme('DarkAmber')

layout = [[sg.Button('1', font='Kanit\ Black 35', size=(2, 1)), sg.Button('2', font='Kanit\ Black 35', size=(2, 1)), sg.Button('3', font='Kanit\ Black 35', size=(2, 1))]]

window = sg.Window('Printer Test', layout, size=(310, 90), resizable=False, element_justification='c')

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break

