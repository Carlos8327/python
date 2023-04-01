comeco = input().split()
codigo,qut = comeco
codigo = int(codigo)
qut = int(qut)
total = 0
if codigo == 1:
    total = 4 * qut
if codigo == 2:
    total = 4.50* qut
if codigo == 3:
    total = 5 * qut
if codigo == 4:
    total = 2* qut
if codigo == 5:
    total = 1.50* qut
    
    


print("total: R$ {:.2f}".format(total))
    
