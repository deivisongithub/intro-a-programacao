frase = input("digite uma string: ")
frase2 = ""
for i in frase:
    if(i == frase[0]):
        frase2 += "#"
    else:
        frase2 += i

print(frase2)