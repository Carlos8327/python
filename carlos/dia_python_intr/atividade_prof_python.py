from datetime import date
#coloquei só para entrar no while
nome =''

#enquanto o nome ou a idade for diferente de 0 mostre o nome e a idade 
while nome != "zero" and nome != "0":
        #como nome tem um elemento vago ele entra direto no while
        
        nome =input("nome: ")
        if nome == "zero" or nome == "0":
                print("fim")
                break     
        
        dataDenascimento = input("data de nascimento: ")
        dia, mes, ano = dataDenascimento.split('/')
        ano = int(ano)
        dia = int(dia)
        mes= int(mes)
        
        
        def  calc(nasc):
              diadoano= 365.2425
              idade1 = int((date.today()-nasc).days /diadoano)
              return idade1
        
     

        
        
        print("-"*30)
        print(f"seu nome é {nome}, sua idade é ",calc(date(ano,mes,dia)) ,"logo sua data se nacimento é ",dataDenascimento)
        print("-"*30)
