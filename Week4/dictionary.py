'''
Operaciones en diccionarios
• .keys() : Retorna la clave de nuestro elemento.
• .values() : Retorna una lista de elementos (valores del diccionario).
• .items() : Devuelve lista de tuplas (primero la clave y luego el valor).
• .clear() : Elimina todos los items del diccionario.
• .pop(“n”) : Elimina el elemento ingresado.
'''
'''
#Ejemplo 1 de diccionario

# Creando un diccionario
mi_diccionario = {
'llave1': 1,
'llave2': 2,
'llave3': 3,
}
# Imprimir el diccionario
print(mi_diccionario)
# Imprimir un elemento especifico de diccionario
print(mi_diccionario['llave2'])
'''


#Ejemplo 2 de diccionario

# Creando un diccionario con la población de los países
poblacion_paises = {
'Argentina': 44938712,
'Brasil': 210147125,
'Colombia': 50372424
}

# Imprimiendo un valor específico del diccionario
print( poblacion_paises['Brasil'] )

# Imprimir las llaves del diccionario
for pais in poblacion_paises.keys():
    print(pais)

# Imprimir los valores del diccionario
for pais in poblacion_paises.values():
    print(pais)

# Imprimir llaves y valores del diccionario
for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes ')