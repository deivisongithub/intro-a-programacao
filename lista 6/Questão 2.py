#Aluno: Deivison rodrigues jordao
#Visualizador de juros de poupanca

#Entrada de dados

deposito_inicial = float(input("Digite o valor depositado:"))
taxa_de_jurosinput = float(input("Digite a taxa de juros da poupanca: "))
taxa_de_juros = taxa_de_jurosinput / 100
rendimento_mensal = deposito_inicial

#Processamento e saida

for i in range(1,25):
    rendimento_mensal = rendimento_mensal + (rendimento_mensal * taxa_de_juros)
    
    print("seu rendimento nesse mes foi de",rendimento_mensal)

print()
print("seu rendimento total foi de ",rendimento_mensal)
print("apenas de juros voce ganhou ",rendimento_mensal - deposito_inicial)