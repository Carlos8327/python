a = input().split()
n1,n2,n3,n4 = a
n1= float(n1)
n2= float(n2)
n3= float(n3)
n4= float(n4)

peso2 = n1 *2
peso3 = n2 *3
peso4 = n3 *4
peso1 = n4 *1

media = (peso2+peso1+peso3+peso4)/10


if media >= 7.0:
    print("Media: {:.1f}".format(media))
    resu=print("Aluno aprovado.")
if media <= 5.0:
    print("Media: {:.1f}".format(media))
    resu=print("Aluno reprovado.")
    
else :
    if media or 5.0 or 6.9:
        resu=("Aluno em exame.")
    
        novanota=float(input())
        novamedia= (novanota+media)/2
    if novamedia >= 5.0:
        resu1=("Aluno aprovado.")
    else:
        resu1=print("Aluno reprovado.")
    
    print("Media: {:.1f}\n{}\nNota do exame: {:.1f}\n{}\nMedia final: {:.1f}".format(media,resu,novanota,resu1,novamedia))
#Aluno em exame.
#Nota do exame: 6.4
#Aluno aprovado.
#Media final: 5.9)


    
