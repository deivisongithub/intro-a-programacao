#Aluno: Deivison rodrigues jordao
#validador de cpf

#Entrada

cpf = input("Digite aqui o seu cpf,usando o modelo XXX.XXX.XXX-XX como referencia: ")

#Processamento e saida
if (len(cpf) == 14):
    if(cpf[3] == "." and cpf[7] == "." and cpf[11] == "-"):
        print("Seu numero de CPF e valido")
    else:
        print("Seu numero de CPF nao e valido")
else:
    print("Seu numero de CPF e invalido")
