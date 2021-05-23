#Aluno: Deivison rodrigues jordao
#Escrever numero do usuario n vzs em forma de piramide

#Definindo funcao

def funcao_maluca(numero):
    string_maluca = ""
    for i in range(numero):
        string_maluca = string_maluca + str(numero)
        print(string_maluca)
#Entrada

n = int(input("Digite um numero: "))

#Processamento e saida

funcao_maluca(n)
