#Aluno: Deivison rodrigues jordao
#Programa q mostra o total a ser pago,juros pago e quantidade de meses a pagar

#Definicao de variaveis

valor_inicial = float(input("digite o valor inicial da divida: "))
juros_mensalinput = float(input("digite o juros mensal: "))
juros_mensal = valor_inicial * (juros_mensalinput/100)
valor_mensalpago = float(input("digite o valor mensal da divida: "))
total_pago = 0
total_de_jurospago = 0
y = 0
#Processammento

if(valor_inicial % valor_mensalpago != 0):
    x = 1
else:
    x = 0

quantidade_de_meses = (valor_inicial // valor_mensalpago) + x

while(y != quantidade_de_meses):
    
    total_pago = total_pago + valor_mensalpago + juros_mensal
            
    y = y + 1

total_de_jurospago =  (juros_mensal * quantidade_de_meses)

if(x == 1):
    
    total_pago = total_pago - (total_pago - total_de_jurospago - valor_inicial)
    
#Saida
print()
print("A quantidades de meses a pagar e de ",quantidade_de_meses)
print("O total pago foi de ",total_pago)
print("total de juros pago e de ",total_de_jurospago)



