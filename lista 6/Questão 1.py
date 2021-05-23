#Aluno: Deivison rodrigues jordao
#visualisador de tabuada

#Entrada de dados
num = int(input("Digite o numero que deseja ver a tabuada: "))
resultados = 0

#Processamento

for i in range(1,11):
    resultados = i * num
    print(i," x ",num,"=",resultados)