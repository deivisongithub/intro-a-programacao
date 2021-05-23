#Aluno: Deivison rodrigues jordao
#juntar dois vetores intercalando seus indices

#Definicao dos vetores:

vetor1 = [None] * 5

vetor2 = [None] * 5

#Preenchimento
for i in range(0,5):
    vetor1[i] = (input("Digite um numero para o vetor1: "))

for i in range(0,5):
    vetor2[i] = (input("Digite um numero para o vetor2: "))

vetor3 = [vetor1[0],vetor2[0],vetor1[1],vetor2[1],vetor1[2],vetor2[2],vetor1[3],vetor2[3],vetor1[4],vetor2[4]]

#Saida
print()
print(vetor3)