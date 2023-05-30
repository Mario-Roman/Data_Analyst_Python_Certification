#Programa que calcule el interés de una cantidad si es mayor al 30%, sino informa el importe total.

costo_objeto=float(input(f"Ingresa el costo del objeto: "))
interes=float(input(f"Ingresa el porcentaje del interes: "))
interes_solo=(0.01*interes)*costo_objeto
total=interes_solo+costo_objeto


if interes>30:
    print(f"El interes es mayor a %30.")
elif interes<=0:
    print(f"Ingresa un porcentaje mayor a 0.")
else:
    print(f"__________________________________")
    print(f"Total de articulos: ${costo_objeto}")
    print(f"Total de Intereses: ${interes_solo}")
    print(f"El importe total es: ${total}")