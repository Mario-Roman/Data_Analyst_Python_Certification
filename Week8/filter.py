"""Tal como su nombre indica filter significa filtrar, y es una de mis funciones
favoritas, ya que a partir de una lista o iterador y una función condicional,
es
capaz de devolver una nueva colección con los elementos filtrados que
cumplan
la condición. Por ejemplo, supongamos que tenemos una lista de varios
números
y queremos filtrarla, quedándonos únicamente con los múltiplos de 5:"""

lista=[17,24,7,39,8,51,92]

def numero_par(num):
    if num % 2 == 0:
        return True

print(list(filter(numero_par,lista)))