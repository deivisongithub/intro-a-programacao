#Aluno: Deivison rodrigues jordao
#Funcao que retorna N ou P

#Definicao de funcao

def funcao_N_P(argumento):
    if(argumento > 0):
        print("P")
    elif (argumento < 0):
        print("N")
    elif(argumento == 0):
        print(" 0 NAO E NEM (P) NEM (N)")

#Entrada

numero = float(input("Digite seu numero: "))

#processamento e saida

funcao_N_P(numero)