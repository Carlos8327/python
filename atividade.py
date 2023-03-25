nome =''
idade = 0
while nome != "zero" and nome != "0":
        nome =input("nome: ")
        if nome == "zero" or nome == "0":
                break     
        dataDenascimento = input("data de nascimento: ")
        dia, mes, ano = dataDenascimento.split('/')
        idade = 
        if idade == 0:
            break
        else:
            print("-"*30)
            print(f"seu nome é {nome}, sua idade é {idade} logo sua data se nacimento é {dia}/{mes}/{ano}")
            print("-"*30)
