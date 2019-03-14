"""
Criar um classe carro que vai possuir dois atributos compostos por outros duas classes:
1)Motor
2)Direçao

Motor - terá a responsabilidade de controlar a velocidade.
Oferece os seguintes atributos:
a) Atributo de dado velocidade
b) Método acelerar, que deverá incrementar a velocidade em 1 unidade
c) Método frear, que deverá decrementar a velocidade em 2 unidades.

Direção - terá a responsabilidade de controlar a direção.
Oferece os seguintes atributos:
a) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste
b) Método girar à direita
c) Método girar à esquerda
   N
O     L
   S
Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    #Testentado Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    #Testando carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)  # caso a velocidade seja < 0, o 0 sera considerado


class Direcao:
    rodar_a_direita = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rodar_a_esquerda = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rodar_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rodar_a_esquerda[self.valor]


class Carro:
    def __init__(self, *atributos):
        self.direcao, self.motor = atributos

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

#
# if __name__ == '__main__':
#     motor = Motor()
#     direcao = Direcao()
#     carro = Carro(direcao, motor)
