#Aluno: Deivison rodrigues jordao
# Programa analista de strings

#Entrada

string_1 = input("Digite o conteudo da primeira string: ")
string_2 = input("Digite o conteudo da segunda string: ")

#Processamento e Saida

comprimento_1 = len(string_1)
comprimento_2 = len(string_2)
print()
print("O conteudo da primeira string e ",string_1)
print("O comprimento da primeira string e de ",comprimento_1)
print("O conteudo da segunda string e " ,string_2)
print("O comprimento da segunda e de ",comprimento_2)

if (comprimento_1 == comprimento_2):
    print("As strings tem o mesmo comprimento")
else:
    print("As strings nao tem o mesmo comprimento")

if (string_1 == string_2):
    print("O conteudo das strings sao iguais")
else:
    print("O conteudo das strings sao diferentes")


