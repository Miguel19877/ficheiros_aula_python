import PySimpleGUI as sg
text = sg.popup_get_text('Escreva a palavra-passe', password_char='*')
if not text:
	sg.popup('Nenhuma password introduzida')
else:
	sg.popup(f'Password:{text}')