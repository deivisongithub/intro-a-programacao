#Aluno: Deivison Rodrigues jordão
#Programa para classificar Triângulos

#Definição de variaveis
lado1 = 0
lado2 = 0
lado3 = 0

#Entrada de dados
lado1 = float(input("digite o tamanho do primeiro lado do triangulo: "))
lado2 = float(input("digite o tamanho do segundo  lado do triangulo: "))
lado3 = float(input("digite o tamanho do terceiro lado do triangulo: "))

#Processamento e saida de dados
if(lado1 == lado2 == lado3):
    print("esse triangulo é Equilatero")
elif(lado1 != lado2 != lado3 != lado1):
    print("esse triangulo é Escaleno")
else:
    print("esse triangulo é isosceles" )    
