"""Esta función trabaja de una forma muy similar a filter(), con la diferencia que en
lugar de aplicar una condición a un elemento de una lista o secuencia, aplica
una función sobre todos los elementos y como resultado se devuelve un iterable
de tipo map:"""

lista = [1,2,3]

def cuadrado(n):
    return n**2

lista2 = list(map(cuadrado, lista))

print(lista2)
