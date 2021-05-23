# Aluno: Deivison Rodrigues jordao
# somador de numeros impares multiplos de 3 de 1 a 500

#Definindo variaveis
soma = 0
numeros = 0

#Processamento
while(numeros < 501):
    if(numeros % 2 != 0):
        if(numeros % 3 == 0):
            soma = soma + numeros
    numeros = numeros + 1

#Saida    
print("O resutado da soma dos numeros impares multiplos de 3 de 1 a 500 e ",soma)
