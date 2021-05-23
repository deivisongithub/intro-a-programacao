#Aluno: Deivison rodrigues jordao
#Contador de digitos de um numero

#definicao de funcao

def contador_de_digitos(numero):
    quantidade_de_digitos = len(str(numero))
    return(quantidade_de_digitos)
#Entrada

n = int(input("Digite um numero: "))

#Processamento e saida

print("A quantidade de digitos de seu numero e ",contador_de_digitos(n))


