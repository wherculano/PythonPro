class Arvore:
    """
        >>> for noh in Arvore(0, Arvore(-2, Arvore(-4), Arvore(-1)), Arvore(10)):
        ...     print(noh)
        -4
        -2
        -1
        0
        10
    """

    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

    # iterar por todos os nós da esquerda
    def __iter__(self):
        """Imprimir todos os nós descendentes do nó atual (do nó esquerdo)
        depois o próprio nó
        e por ultimo os nós da direita"""
        if self.esquerda is not None:
            for valor in self.esquerda:  # se há filhos à esquerda. Vai iterar em todos eles.
                yield valor  # retorna um generator dos valores atuais
        yield self.valor  # retorna valor do proprio nó corrente
        if self.direita is not None:
            yield from self.direita  # faz a mesma coisa da linha acima

#         0
#   -2          10
# -4     -1
#
