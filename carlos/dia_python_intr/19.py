from funcao import calcular_idade
import json


arquivo = open("19_04_2023.json","r") 

lista = json.load(arquivo) 
for i  in lista:
    nome = i['nome']
    

    

            
    nascimento = i['nascimento']
    idade = calcular_idade(nascimento)

    if idade == -1:
                print('invalida')
                continue

    print("-"*30)
    print(f"seu nome é {nome}, sua idade é {idade}")
    print("-"*30)

    
print('fim!')
