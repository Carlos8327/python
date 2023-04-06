#e se o usuario digitar a data em formato errado(ex."9/8/93")? tratar esta entrado
from datetime import date


hoje = date.today()
nome = input("nome: ")

 
while nome.lower() != "zero" and nome != "0":
        try:
        
            data_de_nascimento = input("data de nascimento:{00}/{00}/{00}")
            dia_do_nascimento, mes_do_nascimento, ano_do_nascimento = data_de_nascimento.split('/')
            ano_do_nascimento = int(ano_do_nascimento)
            dia_do_nascimento = int(dia_do_nascimento)
            mes_do_nascimento = int(mes_do_nascimento)
        
        except:
            print("digite a data certa")
            
         
            print("digite a data certa")     
        
            idade = int(hoje.year - ano_do_nascimento)

        if hoje < date(hoje.year, mes_do_nascimento, dia_do_nascimento):
               idade -= 1  # idade = idade - 1

        print("-"*30)
        print(f"seu nome é {nome}, sua idade é {idade} , logo sua data se nacimento é {data_de_nascimento}")
        print("-"*30)

        nome = input("nome: ")

print('fim!')
