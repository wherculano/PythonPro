"""
>>> t = Tombola()
>>> t.itens
[]
>>> t.carregada()
False
>>> t.carregar([1, 2])
>>> t.itens
[1, 2]
>>> t.carregada()
True
>>> def embaralhar_mock(lista):
...     lista[0], lista[-1] = lista[-1], lista[0]
>>> t.itens
[1, 2]
>>> t.shuffle = embaralhar_mock  # injeção de dependencia(inversão de controle)
>>> t.misturar()
>>> t.itens
[2, 1]
>>> t.sortear()
1
>>> t.carregada()
True
>>> t.sortear()
2
>>> t.carregada()
False
>>> t.sortear()
'Não há números a serem sorteados!'

"""
from random import shuffle


class Tombola:
    def __init__(self):
        self.itens = []

    def carregar(self, lista):
        self.itens = lista

    def carregada(self):
        return bool(self.itens)  # mesma coisa que verificar com "if not self.itens"

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        try:
            return self.itens.pop()  # apresenta o ultimo elemento e exclui ele
        except IndexError:
            return 'Não há números a serem sorteados!'
