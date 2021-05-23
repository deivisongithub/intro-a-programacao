#Aluno: Deivison rodrigues jordao
#Calculadora de exponenciacao

#Entrada de dados

numero = float(input("digite o numero de deseja potencializar: "))

expoente = int(input("digite o numero equivalente ao expoente: "))

resultado = numero

#Processamento

for i in range(expoente -1):
   resultado = resultado * numero

if(expoente == 0):
    resultado = 1

print("O resultado de ",numero,"elevado a ",expoente,"e igual a ",resultado)
