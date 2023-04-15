'''uma função que recebe um numero float e o converte para intero'''
def float_em_int(a): 
     return int(a)
        


'''uma função que recebe um inteiro e o converta para um float com uma precisão de 4 digito após a vírgula'''
def inteiro_em_float(valor):
    
        valor = float(f"{valor:.4}")
        return valor
        


'''uma função que recebe uma lista,a converta em set e percora esse set para semostrar os item'''
def lista_em_set(listarecebe):
    lista = [listarecebe]
    trasforma_em_set = set(lista)
    return trasforma_em_set

    


'''uma função que recebe um dicionario e o converta em set,ignorando os indices(forma como assesa o item valor do dicionario)'''
def dicionario_em_set(dicionario):
    lista = set(dicionario)
    return lista


# dicio = {1: 'Carlos'}
# print(converte_diciorio_em_set_ignorando_o_valor(dicio))
