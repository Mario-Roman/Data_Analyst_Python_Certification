'''Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.'''

lista1=[]

for i in range(5):
    n=input("Ingresa un texto: ")
    lista1.append(n)

lista2 = lista1[:]
lista2.reverse()

print(lista1)
print(lista2)