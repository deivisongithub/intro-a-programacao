#Aluno: Deivison rodrigues jordao
#Urna de votos

#Entrada de dados e definicao de variaveis

numero_de_eleitores = int(input("digite a quantidade de eleitores: "))

candidato1 = 11
candidato2 = 22
candidato3 = 33

candidato1_contagem = 0
candidato2_contagem = 0
candidato3_contagem = 0

print()
print("Os candidatos são :")
print("Os candidato1 de numero 11")
print("Os candidato2 de numero 22")
print("Os candidato3 de numero 33")
print()

#Processamento

for i in range(numero_de_eleitores):
    
    voto = int(input("digite o numero do candidato que deseja votar: "))
    
    if(voto == candidato1):
        candidato1_contagem = candidato1_contagem + 1
        
    elif(voto == candidato2):
        candidato2_contagem = candidato2_contagem + 1
    
    if(voto == candidato3):
        candidato3_contagem = candidato3_contagem + 1

#Saida
print()
print("O candidato1 recebeu ",candidato1_contagem," votos")
print("O candidato2 recebeu ",candidato2_contagem," votos")
print("O candidato3 recebeu ",candidato3_contagem," votos")
        
