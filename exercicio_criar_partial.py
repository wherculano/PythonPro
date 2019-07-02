"""
>>> double = partial_test(mult, y=2)
>>> double(2)
4
>>> double(9.5)
19.0
>>> triple = partial_test(mult, y=3)
>>> triple(3)
9
>>> triple(6)
18
"""


def mult(x, y):
    return x * y


def partial_test(func, *args, **kwargs):
    def internal_func(*internal_args, **internal_kwargs):
        return func(*args, *internal_args, **kwargs, **internal_kwargs)
    return internal_func
