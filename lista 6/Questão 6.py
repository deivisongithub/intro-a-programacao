# Visualizador fibonacci
# Aluno: Deivison Rodrigues jordao

num = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (num == 1):
     print("1")

elif(num == 2):
     print("1")
     print("1")
     
elif(num == 0):
    print("e impossivel mostrar 0 termos")
    
else:
   
    print("1")
    print("1")
    
    for contador in range(2,num):
        termos = ultimo + penultimo
        penultimo = ultimo
        ultimo = termos
        print(termos)