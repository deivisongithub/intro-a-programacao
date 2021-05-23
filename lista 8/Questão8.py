#Aluno: Deivison rodrigues jordao
#Jogo da forca

#Definicao da palavra

palavra = "ventilador"

#Definicao de variaveis

contador = 0
letras_2= ''
confirmador_de_vitoria = 0

#Processamento e saida
while True:
    letra = input("Digite uma letra: ")
    letra = letra.lower()
    if contador == 5:
        print("Voce errou pela", contador+1 ,"vez,acabou o jogo")
        break

    elif letra in palavra:
        letras_2 += letra
        print("palavra e: ", end='')
        for l in palavra:


            if l != letra and l not in letras_2:
                print("_", end='')

            else:
                print(f'{l}', end='')
    else:
        contador += 1
        print("Voce errou pela", contador ,"vez, Tente de novamente")
    if(len(letras_2) == len(palavra)):
        for i in range(len(letras_2)):
            if(letras_2[i] in palavra):
                confirmador_de_vitoria += 1
    if(confirmador_de_vitoria == len(palavra)):
        print()
        print("parabens,voce ganhou!!!")
        break