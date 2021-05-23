#Aluno: Deivison rodrigues jordao
#Data de nascimento com mes por extenso

#Entrada,Processamento e saida

data_nascimento = input("Digite sua data de nascimento seguindo esse modelo dd/mm/aaaa: ")

if(data_nascimento[3:5] == "01"):
    data_nascimento_final = data_nascimento[0:2] + " de janeiro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "02"):
    data_nascimento_final = data_nascimento[0:2] + " de fevereiro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "03"):
    data_nascimento_final = data_nascimento[0:2] + " de marco de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "04"):
    data_nascimento_final = data_nascimento[0:2] + " de abril de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "05"):
    data_nascimento_final = data_nascimento[0:2] + " de maio de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "06"):
    data_nascimento_final = data_nascimento[0:2] + " de junho de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "07"):    
    data_nascimento_final = data_nascimento[0:2] + " de julho de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "08"):
    data_nascimento_final = data_nascimento[0:2] + " de agosto de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "09"):
    data_nascimento_final = data_nascimento[0:2] + " de setembro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "10"):
    data_nascimento_final = data_nascimento[0:2] + " de outubro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "11"):
    data_nascimento_final = data_nascimento[0:2] + " de novembro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
elif(data_nascimento[3:5] == "12"):
    data_nascimento_final = data_nascimento[0:2] + " de dezembro de " + data_nascimento[6:]
    print("sua data de nascimento e : ",data_nascimento_final)
    