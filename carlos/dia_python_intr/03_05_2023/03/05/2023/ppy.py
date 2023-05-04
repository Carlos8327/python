from funcaoo import *
import json



arquivo = open("19_04_2023.json" ,"r")
dicionario = list(json.load(arquivo))

dicionario.append({"nome": "bele", "nascimento": "02/12/2006"})


 
for i  in dicionario:
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
with open("19_04_2023.json","w" ) as f:
    f.write(json.dumps(dicionario,indent=4))