#Aluno: Deivison rodrigues jordão
#Programa para descriminar o salário e os descontos no salário de um funcionário

#Definição de variáveis
salario_por_hr = 0
hrs_mensais = 0
salario_bruto = salario_por_hr * hrs_mensais
imposto_de_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = (((salario_bruto - imposto_de_renda) - inss) - sindicato)

#Entrada de dados
salario_por_hr = float(input("digite o valor que voce ganha por hora: "))
hrs_mensais = float(input("digite a quantidade de horas que voce trabalha por mes: "))

#Processamento
salario_bruto = salario_por_hr * hrs_mensais
imposto_de_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = (((salario_bruto - imposto_de_renda) - inss) - sindicato)

#saída de dados
print("seu salario bruto é ",salario_bruto)
print("A quantia que foi retirada do seu salario para o imposto de renda foi ",imposto_de_renda)
print("A quantia que foi retirada do seu salario para o inss foi ",inss)
print("A quantia que foi retirada do seu salario para o sindicato foi ",sindicato)
print("seu salario liquido é ",salario_liquido)