"""1. Construya un programa tal que dado los datos reales A y B, escriba el resultado
de la siguiente expresión:

A=int(input("Valor de A: "))
B=int(input("Valor de B: "))

resultado=(3*A + B)**3/(7*B -1/2*A)

print(f"el resultado es {resultado}")



2. Construye un programa que, al recibir como datos el nombre del empleado y los
seis primeros sueldos del año, calcule el ingreso total y el promedio, imprima el
nombre del empleado, el ingreso total y el promedio.


emp=input("Nombre del emplreado: ")

sueldo1=int(input("Ingresa el primer sueldo: "))
sueldo2=int(input("Ingresa el segundo sueldo: "))
sueldo3=int(input("Ingresa el tercer sueldo: "))
sueldo4=int(input("Ingresa el cuarto sueldo: "))
sueldo5=int(input("Ingresa el quinto sueldo: "))
sueldo6=int(input("Ingresa el sexto sueldo: "))

total=sueldo1+sueldo2+sueldo3+sueldo4+sueldo5+sueldo6
prom=total/6

print(f"\nHola {emp} \n El ingreso total de tu salariofue de {total} y el promedio de tu salario fue de {prom}")



3. Desarrolla un algoritmo que calcule la edad de una persona con base en la
obtención año de nacimiento.

año=int(input("Digita tu año de nacimiento: "))

edad=2023-año

print(f"Tienes {edad} años")



4. Construya un programa que dato a y b reales permita calcular e imprimir los
binomios: (a + b), (a + b)**2 , (a + b)**3 , (a + b)**4 .

a=int(input("Ingrese valor de a: "))
b=int(input("Ingrese valor de b: "))

bin1=(a + b)
bin2=(a + b)**2
bin3=(a + b)**3
bin4=(a + b)**4

print(f"{bin1},{bin2},{bin3},{bin4}")


5. Construya un programa para calcular el área de un pentágono dado el lado
pentágono

import math

L=int(input("Ingrese medida de un lado del pentagono: "))
A =(1/4)*(math.sqrt(5*(5 + 2*math.sqrt(5))*L**2))

print({A})



6. Construya un programa para calcular el área de una corona circular dados el radio
mayor y radio menor.
"""
import math

R=0
r=0

A = math.pi(R**2 - r**2)


"""
7. Escriba un programa, dado como datos el nombre de un animal, su peso y longitud,
expresados estos dos últimos en libras y pies respectivamente, escriba el nombre del
animal su peso expresado en kilogramos y su longitud expresada en metros.
• 1 libra es a 0.4536 kilogramo
• 1 pie es a 0.3048 metros
9. Construya un programa que resuelva el problema que tienen en una gasolinera. Los
surtidores de esta registran lo que “surten” en galones, pero el precio de la
gasolina esta fija en litros. El diagrama de flujo debe calcular e imprimir lo que
hay que cobrarle al cliente. (El precio del litro es $22.80)
• 1 galón es 3.785 litros
10. Una persona compró una estancia en un país sudamericano. La extensión de la
estancia está especificada en acres. Construya un programa que, al recibir
como dato la extensión de la estancia en acres, calcule e imprima la extensión de
la misma en hectáreas.
• 1 acre es igual 4047 m2 .
• 1 hectárea es igual 10,000 m2 .
11. Construya un diagrama de flujo tal que, dados los tres lados de un triángulo, pueda determinar su área. Esta
la calculamos aplicando la siguiente formula:

Area = √S ⋅ (S − L1
) ⋅ (S − L2
) ⋅ (S − L3
)

S =
L1 + L2 + L3
2

12. Construye un programa que, al recibir como datos las coordenadas de los
puntos P1, P2 y P3 que corresponden a los vértices de un triángulo, calcule su
perímetro.
Formula de la distancia entre dos puntos.
d = √(x2 − x1)

2 + (y2 − y1)
2"""