def exponenciacao(base,expoente):
    resultado = base
    for i in range(expoente-1):
        resultado = resultado * base
    return resultado

A = float(input("digite a base: "))
B = int(input("digite o expoente: "))

print(exponenciacao(A,B))