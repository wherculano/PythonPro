'''
Criar um classe carro que vai possuir dois atributos compostos por outros duas classes:
1)Motor
2)Direção

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
>>>carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>>carro.calcular_velocidade()
1
>>> carro.acelerar()
>>>carro.calcular_velocidade()
2
>>> carro.frear()
>>>carro.calcular_velocidade()
0
>>>carro.calcular_direcao()
'Norte'
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Leste'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Norte'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Oeste'
'''


class Motor(object):
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        #return self.velocidade

    def frear(self):
        if self.velocidade >=2:
            self.velocidade -= 2
            # return self.velocidade
        elif self.velocidade == 1:
            self.velocidade -= 1
            # return self.velocidade
        else:
            return f'Você está parado já'


class Direcao(object):
    NORTE = 'Norte'
    SUL = 'Sul'
    LESTE = 'Leste'
    OESTE = 'Oeste'

    def __init__(self):
        self.valor = self.NORTE

    def girar_a_direita(self):
        if self.valor == self.NORTE:
            self.valor = self.LESTE
        elif self.valor == self.LESTE:
            self.valor = self.SUL
        elif self.valor == self.SUL:
            self.valor = self.OESTE
        elif self.valor == self.OESTE:
            self.valor == self.NORTE

    def girar_a_esquerda(self):
        if self.valor == self.NORTE:
            self.valor = self.OESTE
        elif self.valor == self.OESTE:
            self.valor = self.SUL
        elif self.valor == self.SUL:
            self.valor = self.LESTE
        elif self.valor == self.LESTE:
            self.valor == self.NORTE


class Carro(direcao, motor):
    def calcular_velocidade(self):
        pass

    def acelerar(self):
        pass

    def frear(self):
        pass

    def calcular_direcao(self):
        pass

    def girar_a_direita(self):
        pass

    def girar_a_esquerda(self):
        pass
