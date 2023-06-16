'''Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.'''

def contar_caracteres(cadena):
    diccionario = {}
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

cadena = input("Ingrese una cadena: ")
resultado = contar_caracteres(cadena)
print(resultado)
