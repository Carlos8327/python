import json 
arquivo = open("19_04_2023.json","r")

dicionario = json.load(arquivo)

print(type(dicionario))
print(dicionario)
