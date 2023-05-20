#Funcion para obtener un dato real
def obtener_dato(mensaje):
    dato=float(input(mensaje))
    return dato

#Funcion para sumar dos numeros
def sumar_numeros(numero1, numero2):
    suma=numero1+numero2
    return suma

#Funcion que imprime el resultado
def imprimir_resultado(mensaje, resultado):
    print(mensaje, resultado)



#Funcion donde se colocara nuestro codigo principal de nuestro programa

def run():
    #Llamemos a la entrada de datos

    num1=obtener_dato("Hola introduzca el primer numero: ")
    num2=obtener_dato("Hola introduzca el segundo numero: ")

    #Llamar a sumar dos numeros

    suma=sumar_numeros(num1, num2)

    #Llamemos a Imprimir_resultados

    imprimir_resultado(f'El resultado de la suma de :',suma)




#Punto de inicio de nuestro programa, donde se llama la funcion principal
if __name__ == '__main__':
    run()