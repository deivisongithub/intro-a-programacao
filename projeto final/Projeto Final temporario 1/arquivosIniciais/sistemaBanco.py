

# Inserindo a senha

senha = 'ABC'
count = 0
acesso = 'Negado'

ent = input('Digite sua senha: ')

if ent != senha:
    while ent != senha:
        count += 1
        if count == 3:
            print('\nSenha bloqueada!')
            break
        
        ent = input('Senha incorreta.\nDigite novamente: ')
        if ent != senha: continue
        
        acesso = 'Permitido'
        
else:
    acesso = 'Permitido'

# Acessando o sistema    

saldo = 0

while acesso == 'Permitido':
    res = int(input('<1> Depositar\n'\
                    '<2> Sacar\n'\
                    '<3> Consultar Saldo\n'\
                    '<4> Sair\n'\
                    'Digite o valor da opcao: '))
    
    if res == 1:
        dep = float(input('Digite o valor para deposito: '))
        saldo = saldo + dep
        print(f'\nSaldo atual = {saldo:.2f}')
    elif res == 2:
        saque = float(input('Digite o valor para saque: '))
        if saque <= saldo:
            saldo = saldo - saque
        else:
            print('\nSaldo insuficiente!')
        print(f'\nSaldo atual = {saldo:.2f}')
    elif res == 3:
        print(f'\nSaldo atual = {saldo:.2f}')
    elif res == 4:
        print('\nOperacao encerrada!')
        break
    else:
        print('\nOperacao invalida, tente novamente!')

