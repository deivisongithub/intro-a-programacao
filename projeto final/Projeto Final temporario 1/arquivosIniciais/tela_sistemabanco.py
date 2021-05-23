
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Conta', size=(5,0)), sg.Input(size=(15,0), key='conta')],
            [sg.Text('Senha', size=(5,0)), sg.Input(size=(15,0), key='senha')],
            [sg.Text('Selecione o banco')],
            [sg.Checkbox('Bradesco', key='bradesco'), sg.Checkbox('Santander', key='santander'), sg.Checkbox('Caixa', key='caixa')],
            [sg.Text('Esqueceu a senha?')],
            [sg.Radio('Sim','senha', key='esqueceuSenha'), sg.Radio('Não','senha', key='naoEsqueceuSenha')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela
        self.janela = sg.Window('CAIXA 24 HORAS').layout(layout)

        
    def Iniciar(self):
        cont = 0
        while True:
            # Entrada de dados
            self.button, self.values = self.janela.Read()
            
            conta = self.values['conta']
            senha = self.values['senha']
            esqueceu_senha = self.values['esqueceuSenha']
            
            print(self.values)
            
            cont += 1
            
            if cont == 3:
                break

tela = TelaPython()
tela.Iniciar()
