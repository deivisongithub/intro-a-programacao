#Aluno:Deivison rodrigues jordao
#Desencriptador de mensagem

print("use apenas numeros de 0 a 26 e use um,e apenas um, espaço de um numero para o outro")
#Definindo variaveis
mensagem = input("digite sua mensagem: ")

auxString = ""
quantidade_de_letras = 0
lista = []

#Processamento
for i in mensagem: 
    
    if i != " ":
        auxString += i 
    else:
        lista.append(auxString)
        auxString = ""
        quantidade_de_letras = quantidade_de_letras + 1
lista.append(auxString)    

dicionariocripto = {0:" ",1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

#Saida
for i in range(quantidade_de_letras + 1):
    print(dicionariocripto[int(lista[i])],end = '')