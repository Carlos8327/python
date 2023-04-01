class Exemplo:
    def __init__(self,a = 2,b = 3):
        self.a = a
        self.b = b

    def f (self,x):
        return self.a*x+self.b

obj1 = Exemplo()
obj1.a 
obj1.b 

obj2  = Exemplo(8)
obj2.a
obj2.b

print(obj1.f(7))
print(obj2.f(4))