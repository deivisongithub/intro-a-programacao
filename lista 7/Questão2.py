#Aluno: Deivison rodrigues jordao
#troca da linha 2 pela coluna 2

#Definindo matriz

matriz = [[None]*3 for i in range(0,3)]

#Processamento

for i in range(3):
    for j in range(3):
        matriz[i][j] = (input("digite um número para a linha [%d] e para a coluna [%d] :"%(i,j)))

#Saida

print()
print("matriz normal")
for i in range(0,3):
    print()
    for j in range(0,3):
        print(matriz[i][j], end =" ")

print()
print()
print("matriz trocada")
matriz_trocada =  [[matriz[0][0],matriz[1][0],matriz[0][2]],[matriz[0][1],matriz[1][1],matriz[2][1]],[matriz[2][0],matriz[1][2],matriz[2][2]]]

for i in range(0,3):
    print()
    for j in range(0,3):
        print(matriz_trocada[i][j], end =" ")