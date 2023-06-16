'''Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.'''

import random

def generar_multiplicacion():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resultado = num1 * num2
    return num1, num2, resultado

def comprobar_respuesta(num1, num2, resultado, respuesta):
    if respuesta == resultado:
        print("¡Respuesta correcta!")
        return True
    else:
        print("Respuesta incorrecta. La respuesta correcta es:", resultado)
        return False

def main():
    aciertos = 0

    for _ in range(10):
        num1, num2, resultado = generar_multiplicacion()
        print("¿Cuánto es", num1, "x", num2, "?")
        respuesta = int(input())

        if comprobar_respuesta(num1, num2, resultado, respuesta):
            aciertos += 1

    print("Has obtenido", aciertos, "aciertos.")

if __name__ == "__main__":
    main()
