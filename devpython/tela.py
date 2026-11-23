import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        Layout = [
        [sg.Text('Nome'),sg.Input()],
        [sg.Text('Idade'),sg.Input()],
        [sg.Button('Enviar Dados')]
        ]

        #Janela
        janela = sg.Window("Dados do Usuário", Layout)

        #Extrair os dados da Tela
        self.button, self.values = janela.read()
        janela.close()

    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()
