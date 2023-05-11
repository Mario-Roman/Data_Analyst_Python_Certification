'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
'''
from random import randint
notas=[randint(0,10) for i in range(5)]

print(notas)
print(f'La media es: {sum(notas)/5}')
print(f'La notas mas alta es: {max(notas)}')
print(f'La nota mas baja es: {min(notas)}')