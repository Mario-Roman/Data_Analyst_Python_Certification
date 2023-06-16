'''Vamos a crear un programa en Python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.'''
def calcular_precio_fruta():
    precios_frutas = {
        "manzana": 2.5,
        "banana": 1.0,
        "naranja": 1.75,
        "pera": 2.0,
        "kiwi": 3.0
    }

    while True:
        fruta = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ")
        if fruta.lower() == "salir":
            break

        cantidad = int(input("Ingrese la cantidad vendida: "))

        if fruta in precios_frutas:
            precio_unitario = precios_frutas[fruta]
            precio_total = precio_unitario * cantidad
            print(f"El precio total de {cantidad} {fruta}(s) es: ${precio_total:.2f}")
        else:
            print("Error: La fruta ingresada no existe.")

        print()

calcular_precio_fruta()
