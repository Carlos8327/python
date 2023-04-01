a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
aux = 0
nome= [a,b,c,d]
for i in nome:
    if i>0.0:
        aux = aux + 1 
media = aux /aux
print("{} valores positivos\n{}".format(aux,media))         
