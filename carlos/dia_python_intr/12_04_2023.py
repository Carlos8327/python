#e se o usuario digitar a data em formato errado(ex."9/8/93")? tratar esta entrado

#diminuir o codigo
from datetime import date
#coloquei só para entrar no while

hoje = date.today()
nome = input("nome: ")



        
quantidade_de_caracter = 0

#enquanto o nome ou a idade for diferente de 0 mostre o nome e a idade 
while nome.lower() != "zero" and nome != "0":
       #como nome tem um elemento vago ele entra direto no while
       
       #saber a data de nascimento
        data_de_nascimento = input("data de nascimento: ")
        
        #ler quantos caracteres tem se for diferente de 10 da erro pois nao entra na base (xx/xx/xxxx) 
        if len(data_de_nascimento) != 10:
                print("erro")
                continue
        
        #caracteres que nao entram em data de nascimento
        for  caracter in data_de_nascimento:
               if caracter not in "/123456789":
                      continue
        
        #corta dia mes e ano de data de nascimento (xx/xx/xxxx)      
        data_de_nascimento = data_de_nascimento.split('/') 
        
        #dicionario do dia mes e ano
        nascimento = {
                "ano":int(data_de_nascimento[2]),
                "dia":int(data_de_nascimento[0]),
                "mes":int(data_de_nascimento[1]),
                #começa do 0 pois computador começa a ler do 0
                }
        
        #descobrir se o mes ou dia e valido de acordo com os parametros menor que 1 ou maior que 31 ou 12

        match nascimento["mes"]:
            #meses de 31 dias
            case  1, 3,5,7,8,10,12:
                if nascimento["dia"] > 1 and nascimento["dia"] < 31:
                     pass
            #meses de 30 dias      
            case 4,6,9,11:
                if nascimento["dia"] > 1 and nascimento["dia"] < 30:
                     pass
                
            #meses de 29 dias      
            case _:
                if nascimento["dia"] > 1 and nascimento["dia"] < 29:
                    pass
        

                
        #calculo para saber a idade
        idade = int(hoje.year - nascimento["ano"])
        
        #if para saber se a idade for maior que o dia mes ano de hoje ele diminuir um na idade exemplo se desse 05/07/2006
        #ele mostraria que a idade e 17 pois so olha o mes mas esse if faz ele verificar o mes dia e ano
        if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
               idade -= 1  # idade = idade - 1

        print("-"*30)
        print(f"seu nome é {nome}, sua idade é {idade} , logo sua data se nacimento é {data_de_nascimento}")
        print("-"*30)

        nome = input("nome: ") 
        if nome == int:
            print("erro ao digita ")
            continue

print('fim!')