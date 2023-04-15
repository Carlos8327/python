from exemplo import soma_lista as s
contador = 0
lista = []
while contador < 5 :
    lista.append(int(input("digite o valor: ")))
    contador = contador+1
print(s(lista))
