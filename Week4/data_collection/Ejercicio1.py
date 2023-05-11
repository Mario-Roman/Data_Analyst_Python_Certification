'''Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''

import math
import random

lista=[]

for i in range(10):
    num = random.randint(1,10)
    lista.append (num)

print(lista)

for numero in lista:
    print(f'El numero es {lista}, el cuadrado es {numero**2} y el cubo es {numero**3}')
