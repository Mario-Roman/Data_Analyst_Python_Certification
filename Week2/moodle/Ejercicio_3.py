
#Ejercicio 3. (1.5 puntos) Calcular el perímetro y área de un rectángulo dada su base y su altura.

alt=int(input("Introduce la altura de el rectangulo: "))
bas=int(input("Introduce la base del rectangulo: "))

a=bas*alt
p= 2*(bas+alt)

print(f'El perimetro de tu rectangulo es {p} y su area es {a}')