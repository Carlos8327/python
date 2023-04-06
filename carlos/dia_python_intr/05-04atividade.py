#e se o usuario digitar a data em formato errado(ex."9/8/93")? tratar esta entrado

#diminuir o codigo
from datetime import date
#coloquei só para entrar no while

hoje = date.today()
nome = input("nome: ")

#enquanto o nome ou a idade for diferente de 0 mostre o nome e a idade 
while nome.lower() != "zero" and nome != "0":
        #como nome tem um elemento vago ele entra direto no while
        
        data_de_nascimento = input("data de nascimento: ").split('/')

        nascimento = {
                "ano": int(data_de_nascimento[2]),
                "dia":int(data_de_nascimento[0]),
                "mes":int(data_de_nascimento[1])
        }

        idade = int(hoje.year - nascimento["ano"])

        if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
               idade -= 1  # idade = idade - 1

        print("-"*30)
        print(f"seu nome é {nome}, sua idade é {idade} , logo sua data se nacimento é {data_de_nascimento}")
        print("-"*30)

        nome = input("nome: ")

print('fim!')
