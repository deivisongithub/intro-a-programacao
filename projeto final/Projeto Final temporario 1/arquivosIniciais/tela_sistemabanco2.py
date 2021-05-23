
import PySimpleGUI as sg

# CAIXA ELETRÔNICO
            
class CaixaEletronico:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('< 1 > Deposito\n< 2 > Saque\n< 3 > Saldo\n< 4 > Sair'), sg.Input(size=(15,0), key='opcao')],
            [sg.Text('Valor', size=(5,0)), sg.Input(size=(15,0), key='valor')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela
        self.janela = sg.Window('SISTEMA DO CLIENTE').layout(layout)

        
    def Inic(self):
        while True:
            # Entrada de dados
            self.button, self.values = self.janela.Read()
            
            saldo = 0
            
            opcao = self.values['opcao']
            valor = float(self.values['valor'])
            
            if opcao == '1':
                saldo += valor
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == '2':
                if valor <= saldo:
                    saldo = saldo - valor
                else:
                    print('\nSaldo insuficiente!')
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == '3':
                print(f'\nSaldo atual = {saldo:.2f}')
            elif opcao == '4':
                print('\nOperacao encerrada!')
                break
            else:
                print('\nOperacao invalida, tente novamente!')
                print(self.values)
                print(opcao)

# VALIDAÇÃO DE DADOS

class ValidacaoDados:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Conta', size=(5,0)), sg.Input(size=(15,0), key='conta')],
            [sg.Text('Senha', size=(5,0)), sg.Input(size=(15,0), key='senha')],
            [sg.Text('Selecione o banco')],
            [sg.Checkbox('Bradesco', key='bradesco'), sg.Checkbox('Santander', key='santander'), sg.Checkbox('Caixa', key='caixa')],
            [sg.Text('Esqueceu a senha?')],
            [sg.Radio('Sim','senha', key='esqueceuSenha'), sg.Radio('Não','senha', key='naoEsqueceuSenha')],
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
            senha_dig = self.values['senha']
            esqueceu_senha = self.values['esqueceuSenha']
            
            print(self.values)
        
            # Verificando a senha
            
            senha = 'ABC'
            
            if senha_dig != senha:
                print('Senha Inválida! Tente Novamente.')
            else:
                if senha_dig == senha:
                    tela_sec = CaixaEletronico()
                    tela_sec.Inic()
                break
                
            
            if cont == 3:
                break



tela = ValidacaoDados()
tela.Iniciar()


