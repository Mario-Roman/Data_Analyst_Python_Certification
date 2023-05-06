"""1. Hola mundo en Python
Para eso usamos la función o comando print, para indicar a Python que debe imprimir una
cadena de caracteres(String), podemos usar "" (Comillas doble) o '' (Comillas
simples), para representar una cadena."""

print("Hola MUNDO :D")

"""2. Declaración de variables en Python
Variables
Una variable es un espacio de memoria (una caja) en el que podemos guardar y se
recupera información (números, texto, etc). Las variables se nombrar utilizando
identificadores (nombre para las variables).
En Python se crea la variable asignándole un valor:"""

numero1=11
numero2=7
numero3=numero1+numero2

"""3. Poema en Python"""

frase1="Tu dice que amas las lluvia"
frase2="Sin embargo usas un paraguas"
frase3="Cuando llueve"

print(frase1, frase2, frase3)

#Tipos de variables en Python

#int (entero)
a = 28

#float(decimales o reales)
b=1.5

#str (string o cadena de texto)
c="Hello"
c="Hello"

#boolean (verdadero o falso)
d = True

#NoneType(sin valor)
e = None

#Str
f="5"

#Lectura de datos en Python
nombre = input("Ingresa tu nombre: ")
print(nombre)

#Lectura de tipo de dato
print(type(nombre))

#Sumar dos numeros en python con el operador aritmetico +

#Declaracion de variables (Entrada y Salida)

#Entradas
numero1=None
numero2=None

#Salida
resultado=None

#Lectura de datos
numero1=float(input("Ingresa un numero: "))
numero2=float(input("Ingresa otro numero: "))

#Procesamiento de datos
resultado=numero1+numero2

#Impresion de resultados
print(resultado)

"""9. Operadores aritméticos en Python
• Suma: 1 + 2
• Resta: 3 - 4
• Multiplicación: 3 * 4
• División (con decimales): 5 / 5
• División (sin decimales): 21 // 5
• Módulo: 25 % 7
• Potencia: 2 ** 2"""

"""Jerarquía de operadores aritméticos en python
1. Paréntesis ()
2. Exponentes o raíces
3. Multiplicaciones o divisiones
4. Sumas y restas
5. Asignacion ="""


"""10 Realice un programa que pida al usuarios los datos A y B como reales, y realice:
• Suma
• Resta
• Multiplicación
• División (con decimales)
• División (sin decimales)
• Módulo
• Potencia
De estos."""


a=None
b=None

a=int(input("Ingresa un numero: "))
b=int(input("Ingresa otro numero: "))

suma=a+b
print("La suma de los dos numeros es: "+str(suma))

resta=a-b
print("La resta de los dos numeros es: "+str(resta))

multip=a*b
print("La multiplicacion de los dos numeros es: "+str(multip))

div=a/b
print("La division de los dos numeros es: "+str(div))

div2=a//b
print("La division de los dos numeros sin decimales es: "+str(div2))

mod=a%b
print("El modulo de los dos numeros es: "+str(mod))

pot=a**b
print("La potencia de los dos numeros es: "+str(pot))