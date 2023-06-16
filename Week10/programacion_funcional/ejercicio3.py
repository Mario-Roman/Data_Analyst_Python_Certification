'''Obtener la cantidad de elementos mayores a 5 en la tupla.

tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)'''

tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
contador = 0

for elemento in tupla:
    if elemento > 5:
        contador += 1

print("Cantidad de elementos mayores a 5:", contador)
