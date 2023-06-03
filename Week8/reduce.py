"""Reduce es una función incorporada de Python 2, que toma como
argumento un
conjunto de valores (una lista, una tupla, o cualquier objeto iterable)
y lo "reduce"
a un único valor. Cómo se obtiene ese único valor a partir de la
colección pasada
como argumento dependerá de la función aplicada.
Por ejemplo, el siguiente código reduce la lista [1, 2, 3, 4] al número
10 aplicando
la función add(a, b), que retorna la suma de sus argumentos."""

from functools import reduce

list = [1,2,3,4,5]

def add(a,b):
    return a + b

print(reduce(add,list))
