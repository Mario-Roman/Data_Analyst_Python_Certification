#Ejercicio 4. (1.5 puntos) Calcular la media de tres números pedidos por teclado.

num1=int(input("Introduce el primer numero para la media: "))
num2=int(input("Introduce el segundo numero para la media: "))
num3=int(input("Introduce el tercer numero para la media: "))

sum_datos=num1+num2+num3


media=sum_datos/3

print(f"La media de tus 3 numeros es {media}")