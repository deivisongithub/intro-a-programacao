# Aluno: Deivison rodrigues jordão
# Programa que mostra o peso ideal apartir da altura

#Definição das variáveis

H = 0
peso_ideal = 0
sexo = 0

#Entrada de dados

sexo = int(input("informe seu sexo usando 1 para masculino e 0 pra feminino:  "))
H = float(input("informe sua altura: "))

#Processamento e saída
 
if(sexo == 1):
    peso_ideal = (72.7 * H) - 58
    print("O peso ideal para sua altura é ",peso_ideal)
elif(sexo == 0):
    peso_ideal = (62.1 * H) - 44.7
    print("O peso ideal para sua altura é ",peso_ideal)
else:
    print("use apenas 1 pra masculino e 0 para feminino")
    print("faça novamente o teste")