#Aluno: Deivison rodrigues jordão
#Programa que calcula a media e exibe o conceito do aluno

#Definição de variaveis
nota1 = 0
nota2 = 0
media = (nota1 + nota2)/2

#Entrada de dados
nota1 = float(input("digite sua primeira nota :"))
nota2 = float(input("digite sua segunda nota :"))

#processamento
media = (nota1 + nota2)/2

#saida de dados
if(0 > nota1 or nota1 > 10):
    print("confira se colocou suas notas corretamente,lembre que cada nota deve ser de 0 a 10")

elif(0 > nota2 or nota2 > 10):
    print("confira se colocou suas notas corretamente,lembre que cada nota deve ser de 0 a 10")

elif(10 >= media >= 9.1):
    print("seu conceito é A")

elif(9 >= media >= 7.6):
    print("seu conceito é B")

elif(7.5 >= media >= 6.1):
    print("seu conceito é C")

elif(6 >= media >= 4.1):
    print("seu conceito é D")

elif(4 >= media >= 0):
    print("seu conceito é E")

else:
    print("confira se colocou suas notas corretamente,lembre que cada nota deve ser de 0 a 10")
    
