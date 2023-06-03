def Calculadora(operacion):
    
    def suma(n1,n2):
        print(n1+n2)
    
    def resta(n1,n2):
        print(n1-n2)
    
    def mult(n1,n2):
        print(n1*n2)

    opciones = {
        'suma':suma,
        'resta':resta,
        'multiplicacion':mult
    }

    return opciones[operacion]

Calculadora('multiplicacion')(5,6)