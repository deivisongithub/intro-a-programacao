# Aluno: Deivison rodrigues jordÃ£o
 # programa para calcular o desconto de um bijuteria

Valor = float(input('Informe o valor da compra: '))

print('Use 1 para dinheiro,2 para cheque e 3 para cartão')

MdP = int(input('Informe a forma de pagamento: ')) #modo de pagamento

VcD = float(Valor - (Valor * 10/100)) #Valor com desconto




if( Valor >= 100 and MdP == 1):
    print('O valor a ser pago e ',VcD)
elif(MdP == 3):
    print("Forma de pagamento invalida")
else:
    print('O valor a ser pago e ', Valor)







