#Aluno: Deivison rodrigues jordao
# programa que calcula e mostra o tempo que uma populacao ultrapassa a outra em numero de pessoais

#Definicao de variaveis

populacao_X = 70000
populacao_Y = 180000
populacao_X2 = 70000
populacao_Y2 = 180000
tempo1 = 0
tempo2 = 0

#Processamento

while(populacao_X < populacao_Y):
    
    populacao_X = populacao_X + (populacao_X * (3.5/100)) 
    populacao_Y = populacao_Y + (populacao_Y * (1.5/100))
    tempo1 = tempo1 + 1

while(populacao_X2 <= populacao_Y2):
    
    populacao_X2 = populacao_X2 + (populacao_X2 * (3.5/100)) 
    populacao_Y2 = populacao_Y2 + (populacao_Y2 * (1.5/100))
    tempo2 = tempo2 + 1

#Saida

print("O tempo necessario para que a populacao x se iguale a populacao y e de aproximadamente ",tempo1-1," anos.")
print("O tempo necessario para que a populacao x ultrapasse a populacao y e de ",tempo2," anos.")
print()
print("OBS: como o numero de pessoas de cada populacao")
print("aumenta em pulsos de crescimento,nao e possivel")
print("ter um valor exato de igulidade, Mas usei um aproximacao")
print("para baixo,pois para cima seria uma ultapassagem.")
