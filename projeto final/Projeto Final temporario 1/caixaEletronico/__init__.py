import PySimpleGUI as sg


# CAIXA ELETRÔNICO

class CaixaEletronico:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('< 1 > Deposito\n< 2 > Saque\n< 3 > Saldo\n< 4 > Sair'), sg.Input(size=(15, 0), key='opcao')],
            [sg.Text('Valor', size=(5, 0)), sg.Input(size=(15, 0), key='valor')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window('SISTEMA DO CLIENTE').layout(layout)

    def Inic(self):

        saldo = 0

        while True:
            # Entrada de dados
            self.button, self.values = self.janela.Read()

            opcao = int(self.values['opcao'])
            try:
                valor = float(self.values['valor'])
            except:
                valor = 0

            if opcao == 1:
                saldo += valor
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == 2:
                if valor <= saldo:
                    saldo = saldo - valor
                else:
                    print('\nSaldo insuficiente!')
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == 3:
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == 4:
                print('\nOperacao encerrada!')
                break
            else:
                print('\nOperacao invalida, tente novamente!')
