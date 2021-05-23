idade = 0
num_pessoas = 0
while(idade >= 0):
    idade = int(input("digite uma"
    " idade: "))
    if(idade < 0):
        break
    salario = float(input("digite o salario: "))
    if(idade > 65 and salario <= 1045):
        num_pessoas += 1

print(num_pessoas)
