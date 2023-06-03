"""Una de las cosas mas interesantes que se puede
hacer con las funciones de orden superior es
pasarla como argumento de varias funciones como
por ejemplo map, esto nos permite sustituir los
típicos bucles de los lenguajes por construcciones
equivalentes."""

lista = [1,2,3]

lista2 = []

for i in lista:
    print(i**2)
    lista2.append(i**2)

print(lista2)