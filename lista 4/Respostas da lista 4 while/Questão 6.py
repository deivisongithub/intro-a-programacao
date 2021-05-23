#Aluno: Deivison rodrigues jordao
#Sistema de vendas

#Difinicao de variaveis

Total_das_compras = 0
codigo = -1

#Processamento

while(codigo != 0):
    codigo = int(input("digite o codigo do produto: "))
    if(codigo == 0):
        break
    Quantidade = int(input("digite a quantidade de produtos: "))

    if(codigo == 1):
        Total_das_compras = Total_das_compras + (5.50 * Quantidade)
    elif(codigo == 2):
        Total_das_compras = Total_das_compras + (2.30 * Quantidade)
    elif(codigo == 3):
        Total_das_compras = Total_das_compras + (4.75 * Quantidade)
    elif(codigo == 4):
        Total_das_compras = Total_das_compras + (6.80 * Quantidade)
    elif(codigo == 5):
        Total_das_compras = Total_das_compras + (9.30 * Quantidade)
    elif(codigo != 0 or 1 or 2 or 3 or 4 or 5):
        print("codigo invalido")

#saida

print()
print("O total de suas compras resultou em %f " %Total_das_compras)