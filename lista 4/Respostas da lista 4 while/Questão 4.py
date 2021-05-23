#Aluno: Deivison rodrigues jordao
# programa que mostra a divisao inteora e o resto da divisao de 2 numeros

#Declaracao de variaveis

numero_1 = 0
numero_2 = 0
divisao_int = 0
resto = 0

#Processamento

numero_1 = float(input("Digite o primeiro numero(dividendo): "))
numero_2 = float(input("Digite o segundo numero(divisor): "))

while(numero_1 > 0 ):
    numero_1 = numero_1 - numero_2
    if(numero_1 < 0):
        numero_1 = numero_1 + numero_2
        break
    divisao_int = divisao_int + 1    
resto = numero_1

#Saida    
print(divisao_int)
print(resto)