#Ejercicio 1. (1.5 puntos) Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:  ([°F] − 32) × 5 ⁄ 9.

f=int(input("Ingresa los grados Farenheit: "))
c=None

c=(f - 32) * 5 / 9

print(f"{f} grados Farenheit convertidos a Celsius son {c}")