# Aluno: Deivison rodrigues jordÃ£o
 # programa para calcular o desconto de um bijuteria

Valor = float(input('Informe o valor da compra: '))

print('Use 1 para dinheiro,2 para cheque,3 para cartão e 4 para outras formas de pagamento')

MdP = int(input('Informe a forma de pagamento: ')) # Modo de pagamento

if(MdP == 3):       # Quantidade de parcelas
    print('Use 1 para Credito e 2 para Debito')
    CoD = int(input('Informe se será no credito ou debito: '))
    if(CoD == 1):
        QdP = int(input('Informe a quantidade de parcelas: '))
        VP = Valor/QdP
    
VcD = float(Valor - (Valor * 10/100)) #Valor com desconto




if( Valor >= 100 and MdP == 1):
    print('O valor a ser pago e ',VcD)
    
elif (MdP == 3 and CoD == 1 and 0<QdP ):
    if(QdP > 3):
        print('Quantidade de parcelas inválidas')
    else:
        print('O valor a ser pago e ',Valor,' em',QdP,' vezes de ',VP)
    
else:
    print('O valor a ser pago e ', Valor)
    
