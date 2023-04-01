from datetime import date
data_atual = date.today()
data_nascimento= int(input("Ano de nascimento:"))
data_atual= data_atual.year
idade =data_atual-data_nascimento

print(idade)