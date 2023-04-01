class animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass


class gato (animal):
    def falar(self):
        return 'meow'


class cachorro (animal):
    def falar(self):
        return 'woof woof'


animais = [gato('Missy'),
           cachorro('Lassie'),
           gato('Bichano')
           ]
for animal in animais:
    print(animal.nome, ":", animal.falar())
