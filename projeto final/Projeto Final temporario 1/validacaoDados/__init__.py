import PySimpleGUI as sg

# VALIDAÇÃO DE DADOS

class ValidacaoDados:
    def __init__(self):
        valid = False
        # Layout
        layout = [
            [sg.Text('Conta', size=(5, 0)), sg.Input(size=(15, 0), key='conta')],
            [sg.Text('Senha', size=(5, 0)), sg.Input(size=(15, 0), key='senha')],
            [sg.Text('Selecione o banco')],
            [sg.Checkbox('Bradesco', key='bradesco'), sg.Checkbox('Santander', key='santander'),
             sg.Checkbox('Caixa', key='caixa')],
            [sg.Text('Esqueceu a senha?')],
            [sg.Radio('Sim', 'senha', key='esqueceuSenha'), sg.Radio('Não', 'senha', key='naoEsqueceuSenha')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
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

            # Verificando banco

            if self.values['bradesco']:
                banco = 'Bradesco'
            elif self.values['santander']:
                banco = 'Santander'
            elif self.values['caixa']:
                banco = 'Caixa'

            dados_bancarios = open(f'contas{banco}', 'rt')

            contas_senhas = {}
            for linha in dados_bancarios:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                contas_senhas[f'{dado[0]}'] = dado[1]

                if dado[0] == conta:
                    saldo = dado[2]
            dados_bancarios.close()

            try:
                if senha_dig != contas_senhas[f'{conta}']:
                    print('Senha Inválida! Tente Novamente.')
                else:
                    if senha_dig == contas_senhas[f'{conta}']:
                        return saldo
                        break
                if cont == 3:
                    return False
                    break
            except:
                print('Número de conta inválido!')
