#Aluno: Deivison rodrigues jordão
#Programa para comprimentar alunos de acordo com a hora do dia

#Definiçãoo das variáveis e entrada de dados
turno = str(input("digite o turno que estuda,usando M para matutino,V para Vespertino e N para noite: "))

#Processamento e saida de dados
if(turno == "M" or turno == "m"):
    print("Bom dia!")
elif(turno == "V" or turno == "v"):
    print("Boa tarde!")
elif(turno == "N" or turno == "n"):
    print("Boa noite!")
else:
    print("Valor invalido")


