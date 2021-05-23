#Aluno: deivison rodrigues jordao
#conparador de distancias euclidianas

#Definicao de variaveis

n = int(input("Digite a quantidade de pontos que deseja informar: "))
d = 0
distancia_media = 0

#Preechimento de lista e tuplas

lista = []
for i in range(0,n):
    x = int(input("X: "))
    y = int(input("Y: "))
    lista.append((x,y))

#Processamento

lista_resultados = []

contador = 0
for i in range(n):
    contador += 1
    for j in range(contador,n):
        calculo_euclidiano = ( ((lista[i][0]- lista[j][0]) **2) + ((lista[i][1]- lista[j][1]) **2) ) **0.5
        lista_resultados.append(calculo_euclidiano)
        d = d + 1
for k in range(d):
    distancia_media = distancia_media + lista_resultados[k]
distancia_media = distancia_media / d

#Saida

print(" A distancia maxima entre dois pontos e ",max(lista_resultados))
print(" A distancia minima entre dois pontos e ",min(lista_resultados))
print(" A distancia media entre dois pontos e ",distancia_media)
    