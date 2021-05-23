#Aluno: Deivison rodrigues jordao
#Cortador de branco

#Entrada

string_input = input("Digite sua string: ")

string_input_sem_branco = ""

#Processamento

for i in string_input:
    if (i != " "):
        string_input_sem_branco += i
#saida
print("Sua string sem brancos ficou: ")
print(string_input_sem_branco)