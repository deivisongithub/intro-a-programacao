#Aluno : Deivison rodrigues jordao
#raiz quadrada

#Definicao de vaiaveis e entrada de dados
n = float(input("digite o numero que deseja calcular a raiz quadrada: "))
b = 2
p = (b + n/b)/2
x = 0

#Processamento
while (x == 0): 
    b = p
    p = (b + n/b)/2
    if(abs(n - p**2)  < 0.0001):
        break

#saida de dados
print("a raiz quadrada de",n,"e igual a %f" %p)