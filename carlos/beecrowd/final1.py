n = float(input())
h = "NOTAS:"
cem = int(n /100)
n = n - (cem*100)
cin = int (n / 50)
n = n - (cin*50)
vin = int (n/20)
n = n - (vin*20)
dez= int (n/10)
n = n - (dez*10)
cinco = int (n/5)
n = n - (cinco*5)
dois = int (n/2)
n = n - (dois*2)


j = "MOEDAS:"

um = int ( n/1)
n = n - (um*1)

centavos50= int(n/0.50)
n = n-(centavos50*0.50)

centavos25= int(n/0.25)
n = n-(centavos25*0.25)

centavos10= int(n/0.10)
n = n-(centavos10*0.10)

centavos05= int(n/0.05)
n = n-(centavos05*0.05)

centavos01= int(n/0.01)
n = n-(centavos01*0.01)




print(h)
print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{}\n{} moeda(s) de R$ 1,00\n{} moeda(s) de R$ 0,50\n{} moeda(s) de R$ 00,25\n{} moeda(s) de R$ 0,10\n{} moeda(s) de R$ 0,05\n{} moeda(s) de R$ 0,01 ".format(cem,cin,vin,dez,cinco,dois,j,um,centavos50,centavos25,centavos10,centavos05,centavos01))