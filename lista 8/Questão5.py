#Aluno: Deivison rodrigues jordao
#contador de letras em uma frase

#Definindo funcao

def criador_de_dicionario(string):
    lista_chaves = []
    lista_valores = []
    dicionario = {}
    numero_de_caractere = 0
    contador_de_letras = 0
    d = 0
    for i in string:
        lista_chaves.append(i)
        numero_de_caractere = numero_de_caractere + 1

    for j in range(numero_de_caractere):
        for i in string:
            if(i == string[j]):
                contador_de_letras = contador_de_letras + 1
        lista_valores.append(contador_de_letras)
        contador_de_letras = 0

    for k in range(numero_de_caractere):
        d = d + 1
        dicionario[lista_chaves[k]] = lista_valores[d-1]
    return(dicionario)

#Entrada

frase = input("Digite sua frase: ")

#Processamento e saida

print(criador_de_dicionario(frase))