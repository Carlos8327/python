from datetime import date
#coloquei só para entrar no while

hoje = date.today()
nome = input("nome: ")

#enquanto o nome ou a idade for diferente de 0 mostre o nome e a idade 
while nome.lower() != "zero" and nome != "0":
        #como nome tem um elemento vago ele entra direto no while
        
        data_de_nascimento = input("data de nascimento: ")

        dia_do_nascimento, mes_do_nascimento, ano_do_nascimento = data_de_nascimento.split('/')
        ano_do_nascimento = int(ano_do_nascimento)
        dia_do_nascimento = int(dia_do_nascimento)
        mes_do_nascimento = int(mes_do_nascimento)
        
        idade = int(hoje.year - ano_do_nascimento)

        if hoje < date(hoje.year, mes_do_nascimento, dia_do_nascimento):
               idade -= 1  # idade = idade - 1

        print("-"*30)
        print(f"seu nome é {nome}, sua idade é {idade} , logo sua data se nacimento é {data_de_nascimento}")
        print("-"*30)

        nome = input("nome: ")

print('fim!')
