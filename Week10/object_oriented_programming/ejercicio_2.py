'''Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.'''

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad
    
    def get_titular(self):
        return self._titular
    
    def set_titular(self, titular):
        self._titular = titular
    
    def get_cantidad(self):
        return self._cantidad
    
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    
    def mostrar(self):
        print(f"Titular: {self._titular}")
        print(f"Cantidad: {self._cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad


# Ejemplo de uso
cuenta1 = Cuenta("Mario Roman", 1000)
cuenta1.mostrar()

cuenta1.set_titular("Roman Mario")
cuenta1.set_cantidad(1500)
cuenta1.mostrar()

cuenta1.ingresar(500)
cuenta1.mostrar()

cuenta1.retirar(700)
cuenta1.mostrar()