def calcular_pago_mensual():
    pago_inicial = 10  # Pago inicial del primer mes
    total_pagado = 0  # Total pagado después de los 20 meses

    for mes in range(1, 21):
        pago_mensual = pago_inicial * (2 ** (mes - 1))
        total_pagado += pago_mensual
        print(f"Mes {mes}: Pago mensual = {pago_mensual} €")

    print(f"\nTotal pagado después de los 20 meses: {total_pagado} €")

calcular_pago_mensual()