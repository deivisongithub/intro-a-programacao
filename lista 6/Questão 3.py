#Aluno: Deivison rodrigues jordao
#Verificador de faixa etaria

#Definicao de variaveis

somatorio_das_idades = 0

#Entrada de dados e processamento

numeros_de_pessoas = int(input("digite a quantidade de pessoas que a sala e composta: "))

for i in range(0,numeros_de_pessoas):
    
    idades = float(input("digite sua idade: "))
    
    somatorio_das_idades = somatorio_das_idades + idades

media_das_idades = somatorio_das_idades / numeros_de_pessoas

#Saida

if( 0 <= media_das_idades <= 25):
    print("A turma e jovem")

elif( 26 <= media_das_idades <= 60):
    print("A turma e adulta")
    
elif( media_das_idades > 60):
    print("A turma e idosa")    