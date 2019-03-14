from unittest import TestCase

from carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)  # Verifica se os valores são iguais (valor esperado, valor atual)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
