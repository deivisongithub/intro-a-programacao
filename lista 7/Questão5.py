# Aluno: Deivison Rodrigues jordao
#processador de altura e sexo

#Atribuido valores a variaveis

quantidade_mulheres = 0
quantidade_homens = 0
somatoriofeminino = 0
somatoriomasculino = 0
media_altura_feminina = 0
media_altura_masculina = 0

#Contruindo as listas

lista_altura = [None] * 10
lista_sexo = [None] * 10

for i in range(10):
    lista_altura[i] = input("digite um altura: ")
    print("lembre-se que o M e F devem ser maiusculo como pedido no enunciado")
    lista_sexo[i] = input("digite o sexo(M/F): ")

#Processamento e saida

print() # Maior e menor e seus sexos

print("A pessoa com maior altura mede ",max(lista_altura)," e o seu sexo e ",lista_sexo[lista_altura.index(max(lista_altura))])
print("A pessoa com menor altura mede ",min(lista_altura)," e o seu sexo e ",lista_sexo[lista_altura.index(min(lista_altura))])

print() # Media de altura de cada sexo

for j in range(10):
    
    if(lista_sexo[j] == "F" or lista_sexo[j] == "f"):
        somatoriofeminino = somatoriofeminino + float(lista_altura[j])
        quantidade_mulheres = quantidade_mulheres + 1
    if(lista_sexo[j] == "M" or lista_sexo[j] == "m"):
        quantidade_homens = quantidade_homens + 1
        somatoriomasculino = somatoriomasculino + float(lista_altura[j])

media_altura_feminina = somatoriofeminino / quantidade_mulheres
media_altura_masculina = somatoriomasculino / quantidade_homens

print("A media de altura do sexo masculino e ",media_altura_masculina)
print("A media de altura do sexo feminino e ",media_altura_feminina)

print() # Quantidade de pessoas de cada sexo

print("A quantidade de mulheres e de",quantidade_mulheres)
print("A quantidade de homens e de ",quantidade_homens)
        
        