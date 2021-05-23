# Aluno: Deivison Rodrigues jordao
# programa que ler numeros e exiba o menor,o maior e a soma dos valores

#Declarando variaveis

numero = 0
maior_N = 0
menor_N = 0
soma_N = 0

#Processamento

while(numero != -1):
    numero = float(input("digite qualquer numero ou -1 para parar o programa: "))
    if(numero != -1):
        if(maior_N == 0):
            maior_N = numero
            menor_N = numero
        elif(numero > maior_N):
            maior_N = numero
        elif(numero < menor_N):
            menor_N = numero
        soma_N = soma_N + numero

#Saida

print("O maior numero e ",maior_N)
print("O menor numero e ",menor_N)
print("A soma dos numeros e ",soma_N)