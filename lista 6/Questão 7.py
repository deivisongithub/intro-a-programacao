#Aluno: Deivison rodrigues jordao
#Programa que verifica se um numero e primo

#Entrada de dados

numero = int(input("digite o numero que deseja verificar se e primo: "))
x = -1 

#Processamento

for i in range(2,numero):
    
    if(numero % i == 0):
        x = 1
        break
    elif(numero % i != 0):
        x = 2

#Saida
        
if(x == 1):
    print("esse numero nao e primo")
elif(x == 2):
    print("esse numero e primo")
elif(numero == 2):
    print("esse numero e primo")
elif(numero == 0 or 1):
    print("esse numero nao e primo")





        
        