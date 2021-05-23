# Aluno: Deivison rodrigues jordao
# gerador de dicionario

x = 0
while(x != -1):
    #Definindo variaveis
    numero_de_caractere = 0
    contador_de_letras = 0
    d = 0

    #Processamento

    mensagem = input("Digite a mensagem: ")

    lista_chaves = []
    lista_valores = []
    dicionario = {}

    for i in mensagem:
        lista_chaves.append(i)
        numero_de_caractere = numero_de_caractere + 1

    for j in range(numero_de_caractere):
        for i in mensagem:
            if(i == mensagem[j].lower() or i == mensagem[j].upper()):
                contador_de_letras = contador_de_letras + 1
        lista_valores.append(contador_de_letras)
        contador_de_letras = 0

    for k in range(numero_de_caractere):
        d = d + 1
        dicionario[lista_chaves[k]] = lista_valores[d-1]

    print(dicionario)

    x = int(input("digite 0 para digitar outra mensagem ou -1 para para o codigo:"))

print("FIM DO CODIGO")