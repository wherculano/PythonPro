"""
# ALL retorna False se houver ao menos um elemento que retorne False dentro do iterador
>>> all([True, True, True, False])
False
>>> all([1, True, 0, 'banana'])  # 0 representa o False
False
>>> all(['', 1, 2, 'verdadeiro'])  # string vazia representa False
False
>>> all(['iteravel', 1, 2, None])  # string vazia representa False
False

# ANY retorna True se houver ao menos um elemento que retorne True
>>> any(['', 0, False, True])
True

#MAP aplica uma funcao qualquer em um iterável.
>>> list(map(int, ['1','2','3']))
[1, 2, 3]

SUM efetua a soma dos elementos de um iterável
>>> sum([3,6,9])
18

#LEN retorna o tamanho de um iterável
>>> len('banana')
6

#SORTED faz a ordenacao de uma lista
>>> sorted([5, 2, 4, 1, 3])
[1, 2, 3, 4, 5]

>>> sorted([5, 2, 4, 1, 3], reverse=True)
[5, 4, 3, 2, 1]

#ZIP faz um conjunto dos elementos de cada iterável
>>> list(zip(['a','b','c'], [1, 2, 3]))
[('a', 1), ('b', 2), ('c', 3)]

#FILTER faz o filtro de cada elemento baseado na funcao passada a ele.
>>> def eh_numero(valor):
...     if str(valor).isnumeric():
...         return valor
>>> list(filter(eh_numero,['a',1,'sapato', 3, 'c', '7']))
[1, 3, '7']

>>> list(filter(lambda x: x>0, [1, -3, 10, 0, -23, 19]))
[1, 10, 19]

#REDUCE aplica uma funcao a todos os elementos a fim de agregá-los em um unico valor
>>> from functools import reduce
>>> import operator
>>> reduce(operator.sub, [1, 2, 3])  # fará a subtracao de todos os valores do iteravel
-4

#ITER 'converte' em um iterável (para ser utilizado com next)
>>> vogais = iter('aeiou')
>>> next(vogais)
'a'
>>> next(vogais)
'e'
>>> next(vogais)
'i'
>>> next(vogais)
'o'
>>> next(vogais)
'u'

#MIN retorna o menor numero do iterável
>>> min([7,3,9,1])
1

#MAX retorna o maior numero do iteravel
>>> max([3,9,1,7])
9

"""
