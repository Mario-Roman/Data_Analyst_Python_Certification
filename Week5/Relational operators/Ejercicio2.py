#Programa que imprima si el número ingresado esta en el rango de 1 a 7.
num=int(input("Ingresa un numero del 1 al 7: "))

if num<1:
    print("Ingresa un numero entre 1 y 7")
elif num>7:
    print("Ingresa un numero entre 1 y 7")
else:
    print(f"El numero es escrito es: {num}")