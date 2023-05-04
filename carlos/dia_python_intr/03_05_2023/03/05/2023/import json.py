import json 
arquivo = open("19_04_2023.json","r")

dicionario = json.load(arquivo)

print(type(dicionario))
print(dicionario)


print('\n\n\n\n\n\n\n',json.dumps(dicionario,indent=4))  # para ficar bunitinho 