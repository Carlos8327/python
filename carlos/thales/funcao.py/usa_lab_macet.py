from funcoes import *
a = input("digite o valor: ")
float_em_int(a)
print(" O valor em float em inteiro e :",float_em_int(a))

inteiro_em_float(a)
print( "O valor em inteiro em float é :",inteiro_em_float(a))

lista = input("digite a lista: ")
lista_em_set(lista)
print("A lista em set é :",lista_em_set(lista))

dicinario = input("digite o cionario: ")
dicionario_em_set(dicinario)
print("O dicionario em set é :", dicionario_em_set(dicinario))
