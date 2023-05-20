#Funciones en Python
#¿ Que es una función?
#1. Una función es un bloque de Código que solo se ejecuta cuando lo llamamos.
#2. Se le puede pasar datos, los cuales se le conocen como parámetros y cuando la
#llamamos a esos mismos datos se le llaman argumentos.
#3. Una función puede devolver algún dato de interés o un print() , inclusive otra función.


'''Parámetros
Se pueden pasar información a través de parámetros.
Los argumentos se especifican después del nombre de la función, entre paréntesis.
Puede agregar tantos argumentos como desee, simplemente sepárelos con una coma.
A una función le podemos pasar mas parámetros'''

'''def mi_primer_funcion(nombre)


def saludar(nombre,apellido):
    print(f'Hola {nombre}, tu apellido es {apellido}')

saludar('Diego')
'''


#* Las funciones también pueden llevar parámetros determinados, es decir valores por
#Default en caso de que no les mandemos nada para trabajar.

'''def mi_pais(pais= 'Mexico'):
    print(f'Yo soy de {pais}')
mi_pais()'''

#Ahora que pasa si le pasamos argumentos

'''def mi_pais(pais= 'Mexico'):
    print(f'Yo soy de {pais}')

mi_pais('Venezuela')
mi_pais('Peru')
mi_pais('Costa Rica')
'''

#De una función también podemos esperar que nos regrese valores como resultados ( no solo prints)

'''def multi(x):
    return x*5

print(multi(5))'''

#La palabra reservada return se ocupa en las funciones para indicarno que no debe regresar “algo” ahi es donde la función acaba su ejecución.

#Palabra reservada Pass.
#Muchas de las veces ya tenemos en mente que necesitamos aplicar una función aunque no
#hemos definido que contenido va llevar y necesitamos avanzar con nuestro programa. Es en
#este caso que ocupamos la palabra pass.

'''def mi_funcion():
    pass'''

#Ahora ya tienes lo necesario para poder trabajar con funciones. Veamos un ejemplo de
#como podemos usar las funciones en un código

#   EJEMPLO

'''Algoritmo para suma de dos numeros'''

#Entrada de datos
numero1=float(input('Ingrese un numero: '))
numero2=float(input('Ingrese otro numero: '))

#Procesamiento de datos
suma = numero1+numero2

#Impresion de resultados
print('La suma de numeros es:', suma)
