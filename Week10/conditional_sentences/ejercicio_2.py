def imprimir_numeros_primos(cantidad):
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < cantidad:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numero)
        numero += 1

    for primo in numeros_primos:
        print(primo)

# Pedir la cantidad de números primos al usuario
cantidad = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
imprimir_numeros_primos(cantidad)
