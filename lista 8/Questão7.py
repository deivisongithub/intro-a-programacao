#Aluno: Deivison rodrigues jordao
#Imprimir por extenso

#Definicao de variaveis

aux_string = ""

#Definicao do dicionario

dicionario = {"0":"zero","1":"um","2":"dois","3":"tres","4":"quatro","5":"cinco","6":"seis","7":"sete","8":"oito","9":"nove","10":"dez","11":"onze","12":"doze","13":"treze","14":"quatorze","15":"quinze","16":"dezesseis","17":"dezessete","18":"dezoito","19":"dezenove","20":"vinte","30":"trinta","40":"quarenta","50":"cinquenta","60":"sessenta","70":"setenta","80":"oitenta","90":"noventa"}

#Entrada

numero = input("digite seu numero entre 1 e 99 : ")

#Processamento e saida

if(numero in dicionario):
    for i in numero:
        aux_string += i
    print(dicionario[aux_string])
else:
    aux_string = numero[0] + "0"
    print(dicionario[aux_string] + " e " + dicionario[numero[1]])